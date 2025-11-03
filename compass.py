#!/usr/bin/env python3
"""
COMPASS AGENTS CLI
==================
Command-line interface để quản lý và sử dụng các Claude Code Agents
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

# Fix encoding for Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Màu sắc cho terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Đường dẫn gốc
ROOT_DIR = Path(__file__).parent.absolute()
CONFIG_FILE = ROOT_DIR / "agents.json"

def load_config() -> Dict:
    """Load cấu hình agents từ file JSON"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"agents": []}

def save_config(config: Dict):
    """Lưu cấu hình agents"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def discover_agents() -> List[Dict]:
    """Tự động tìm và cấu hình các agents trong thư mục"""
    agents = []

    for item in ROOT_DIR.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            claude_file = item / "CLAUDE.md"
            readme_file = item / "README.md"

            if claude_file.exists():
                # Đọc thông tin từ CLAUDE.md
                with open(claude_file, 'r', encoding='utf-8') as f:
                    first_lines = f.read(500)
                    # Lấy title từ dòng đầu tiên (# Title)
                    title_line = [line for line in first_lines.split('\n') if line.startswith('#')]
                    title = title_line[0].strip('# ').strip() if title_line else item.name

                # Đọc description từ README.md nếu có
                description = ""
                if readme_file.exists():
                    with open(readme_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        # Lấy dòng mô tả đầu tiên
                        for line in lines[1:10]:  # Bỏ qua title
                            if line.strip() and not line.startswith('#'):
                                description = line.strip()
                                break

                agents.append({
                    "id": item.name,
                    "name": title,
                    "description": description,
                    "path": str(item.relative_to(ROOT_DIR)),
                    "full_path": str(item)
                })

    return agents

def print_header():
    """In header của CLI"""
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}==============================================================={Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}         COMPASS AGENTS - Agent Management CLI            {Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}==============================================================={Colors.ENDC}\n")

def cmd_list(interactive=True):
    """Liệt kê tất cả agents có sẵn"""
    config = load_config()
    agents = config.get("agents", [])

    if not agents:
        print(f"{Colors.WARNING}[!] Chua co agents nao. Chay 'compass scan' de tim agents.{Colors.ENDC}")
        return

    print(f"{Colors.OKGREEN}[*] Danh sach Agents:{Colors.ENDC}\n")

    for idx, agent in enumerate(agents, 1):
        print(f"{Colors.BOLD}{idx}. {agent['name']}{Colors.ENDC}")
        print(f"   {Colors.OKCYAN}ID:{Colors.ENDC} {agent['id']}")
        if agent.get('description'):
            print(f"   {Colors.OKCYAN}Mô tả:{Colors.ENDC} {agent['description']}")
        print(f"   {Colors.OKCYAN}Đường dẫn:{Colors.ENDC} {agent['path']}")
        print()

    # Interactive mode
    if interactive:
        print(f"{Colors.OKCYAN}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}Chon agent de chay (nhap so 1-{len(agents)}, hoac Enter de thoat):{Colors.ENDC} ", end='')

        try:
            choice = input().strip()

            if not choice:
                print(f"{Colors.WARNING}[*] Thoat.{Colors.ENDC}")
                return

            choice_num = int(choice)

            if 1 <= choice_num <= len(agents):
                selected_agent = agents[choice_num - 1]
                cmd_run(selected_agent['id'])
            else:
                print(f"{Colors.FAIL}[-] Lua chon khong hop le. Vui long chon tu 1 den {len(agents)}.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}[-] Vui long nhap so.{Colors.ENDC}")
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}[*] Thoat.{Colors.ENDC}")

def cmd_scan():
    """Quét và cập nhật danh sách agents"""
    print(f"{Colors.OKBLUE}[*] Dang quet thu muc...{Colors.ENDC}")
    agents = discover_agents()

    if not agents:
        print(f"{Colors.WARNING}[!] Khong tim thay agent nao (phai co file CLAUDE.md){Colors.ENDC}")
        return

    config = {"agents": agents}
    save_config(config)

    print(f"{Colors.OKGREEN}[+] Da tim thay {len(agents)} agents:{Colors.ENDC}\n")
    for agent in agents:
        print(f"  - {agent['name']} ({agent['id']})")

    print(f"\n{Colors.OKCYAN}[*] Da luu cau hinh vao {CONFIG_FILE}{Colors.ENDC}")

def cmd_info(agent_id: str):
    """Hiển thị thông tin chi tiết về một agent"""
    config = load_config()
    agents = config.get("agents", [])

    agent = next((a for a in agents if a['id'] == agent_id), None)

    if not agent:
        print(f"{Colors.FAIL}[-] Khong tim thay agent '{agent_id}'{Colors.ENDC}")
        print(f"{Colors.WARNING}Chay 'compass list' de xem danh sach agents{Colors.ENDC}")
        return

    print(f"\n{Colors.BOLD}{Colors.OKGREEN}=== {agent['name']} ==={Colors.ENDC}\n")
    print(f"{Colors.OKCYAN}ID:{Colors.ENDC} {agent['id']}")
    print(f"{Colors.OKCYAN}Mo ta:{Colors.ENDC} {agent.get('description', 'N/A')}")
    print(f"{Colors.OKCYAN}Duong dan:{Colors.ENDC} {agent['full_path']}")

    # Kiểm tra các file quan trọng
    agent_path = Path(agent['full_path'])
    print(f"\n{Colors.OKBLUE}[*] Cau truc:{Colors.ENDC}")

    important_files = [
        ("CLAUDE.md", "Huong dan cho Claude"),
        ("README.md", "Tai lieu du an"),
        (".claude/settings.json", "Cau hinh Claude Code"),
        ("context/", "Thu muc ngu canh"),
        ("workspace/", "Thu muc lam viec"),
        ("tools/", "Cong cu va scripts")
    ]

    for file_name, description in important_files:
        file_path = agent_path / file_name
        if file_path.exists():
            print(f"  [+] {file_name:<25} - {description}")
        else:
            print(f"  [ ] {file_name:<25} - {description}")

def cmd_open(agent_id: str):
    """Mở terminal tại thư mục agent"""
    config = load_config()
    agents = config.get("agents", [])

    agent = next((a for a in agents if a['id'] == agent_id), None)

    if not agent:
        print(f"{Colors.FAIL}[-] Khong tim thay agent '{agent_id}'{Colors.ENDC}")
        return

    agent_path = agent['full_path']

    print(f"{Colors.OKGREEN}[*] Mo terminal tai: {agent_path}{Colors.ENDC}")

    # Mở terminal tùy theo hệ điều hành
    if sys.platform == "win32":
        subprocess.run(f'start cmd /K "cd /d {agent_path}"', shell=True)
    elif sys.platform == "darwin":  # macOS
        subprocess.run(['open', '-a', 'Terminal', agent_path])
    else:  # Linux
        subprocess.run(['gnome-terminal', '--working-directory', agent_path])

def cmd_cd(agent_id: str):
    """In lệnh cd để người dùng tự chạy"""
    config = load_config()
    agents = config.get("agents", [])

    agent = next((a for a in agents if a['id'] == agent_id), None)

    if not agent:
        print(f"{Colors.FAIL}[-] Khong tim thay agent '{agent_id}'{Colors.ENDC}")
        return

    print(f"\n{Colors.OKGREEN}[*] De chuyen den thu muc agent, chay lenh:{Colors.ENDC}")
    print(f"\n  {Colors.BOLD}cd \"{agent['full_path']}\"{Colors.ENDC}\n")

def cmd_run(agent_id: str):
    """Chạy agent - Làm việc với agent trong session hiện tại"""
    config = load_config()
    agents = config.get("agents", [])

    agent = next((a for a in agents if a['id'] == agent_id), None)

    if not agent:
        print(f"{Colors.FAIL}[-] Khong tim thay agent '{agent_id}'{Colors.ENDC}")
        return

    agent_path = agent['full_path']

    print(f"\n{Colors.BOLD}{Colors.OKGREEN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}    AGENT: {agent['name']}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKGREEN}{'='*60}{Colors.ENDC}\n")

    # Đọc CLAUDE.md để hiển thị thông tin agent
    claude_file = Path(agent_path) / "CLAUDE.md"

    if claude_file.exists():
        try:
            with open(claude_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Hiển thị thông tin cơ bản
            print(f"{Colors.OKCYAN}[*] Mo ta:{Colors.ENDC}")
            if agent.get('description'):
                print(f"    {agent['description']}\n")

            print(f"{Colors.OKCYAN}[*] Thu muc:{Colors.ENDC}")
            print(f"    {agent_path}\n")

            # Tìm và hiển thị các commands nếu có
            print(f"{Colors.OKCYAN}[*] Trang thai:{Colors.ENDC}")
            print(f"    {Colors.OKGREEN}Agent da san sang trong session hien tai!{Colors.ENDC}\n")

            print(f"{Colors.OKBLUE}[*] Huong dan:{Colors.ENDC}")
            print(f"    1. Ban dang lam viec voi agent nay trong Claude Code")
            print(f"    2. Toi da doc file CLAUDE.md va hieu ro ve agent nay")
            print(f"    3. Ban co the bat dau hoi toi bat ky cau hoi nao ve agent")
            print(f"    4. Toi se hoat dong theo context va chuc nang cua agent nay\n")

            # Hiển thị một số thông tin từ CLAUDE.md
            print(f"{Colors.OKBLUE}[*] Cac chuc nang chinh:{Colors.ENDC}")

            # Tìm các dòng có emoji hoặc bullet points để hiển thị features
            lines = content.split('\n')
            features = []
            in_features = False

            for line in lines[:200]:  # Chỉ đọc 200 dòng đầu
                if any(keyword in line.lower() for keyword in ['chức năng', 'features', 'mục đích', 'workflow']):
                    in_features = True
                    continue

                if in_features and ('✅' in line or '- ' in line or '* ' in line):
                    clean_line = line.strip()
                    if clean_line and len(features) < 8:  # Giới hạn 8 features
                        features.append(clean_line)

                if in_features and line.strip() == '':
                    if features:
                        break

            if features:
                for feature in features:
                    print(f"    {feature}")
            else:
                print(f"    Xem file CLAUDE.md de biet them chi tiet")

            print(f"\n{Colors.BOLD}{Colors.OKGREEN}[+] San sang lam viec! Ban can toi giup gi?{Colors.ENDC}\n")

        except Exception as e:
            print(f"{Colors.WARNING}[!] Khong the doc CLAUDE.md: {e}{Colors.ENDC}")
            print(f"{Colors.OKGREEN}[+] Agent van san sang hoat dong!{Colors.ENDC}\n")
    else:
        print(f"{Colors.WARNING}[!] Khong tim thay file CLAUDE.md{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[+] Lam viec voi agent tai: {agent_path}{Colors.ENDC}\n")

def cmd_help():
    """Hiển thị hướng dẫn sử dụng"""
    print(f"\n{Colors.BOLD}HUONG DAN SU DUNG COMPASS CLI{Colors.ENDC}\n")

    commands = [
        ("compass scan", "Quet va cap nhat danh sach agents"),
        ("compass list", "Hien thi va chon agent de chay (interactive)"),
        ("compass run <agent-id>", "Chay agent truc tiep"),
        ("compass info <agent-id>", "Xem thong tin chi tiet ve mot agent"),
        ("compass open <agent-id>", "Mo terminal moi tai thu muc agent"),
        ("compass cd <agent-id>", "Hien thi lenh cd de chuyen den agent"),
        ("compass help", "Hien thi huong dan nay"),
    ]

    print(f"{Colors.OKCYAN}CAC LENH:{Colors.ENDC}\n")
    for cmd, desc in commands:
        print(f"  {Colors.OKGREEN}{cmd:<30}{Colors.ENDC} {desc}")

    print(f"\n{Colors.OKCYAN}VI DU:{Colors.ENDC}\n")
    print(f"  {Colors.BOLD}compass scan{Colors.ENDC}")
    print(f"  {Colors.BOLD}compass list{Colors.ENDC}")
    print(f"  {Colors.BOLD}compass info BO_KHO_MUA_HANG_THEO_TARGET{Colors.ENDC}")
    print(f"  {Colors.BOLD}compass open tech-learning-assistant{Colors.ENDC}")
    print()

def main():
    """Entry point của CLI"""
    print_header()

    # Nếu không có args, chạy interactive list
    if len(sys.argv) < 2:
        cmd_list(interactive=True)
        return

    command = sys.argv[1].lower()

    if command == "scan":
        cmd_scan()
    elif command == "list" or command == "ls":
        cmd_list()
    elif command == "run":
        if len(sys.argv) < 3:
            print(f"{Colors.FAIL}[-] Thieu agent ID. Su dung: compass run <agent-id>{Colors.ENDC}")
        else:
            cmd_run(sys.argv[2])
    elif command == "info":
        if len(sys.argv) < 3:
            print(f"{Colors.FAIL}[-] Thieu agent ID. Su dung: compass info <agent-id>{Colors.ENDC}")
        else:
            cmd_info(sys.argv[2])
    elif command == "open":
        if len(sys.argv) < 3:
            print(f"{Colors.FAIL}[-] Thieu agent ID. Su dung: compass open <agent-id>{Colors.ENDC}")
        else:
            cmd_open(sys.argv[2])
    elif command == "cd":
        if len(sys.argv) < 3:
            print(f"{Colors.FAIL}[-] Thieu agent ID. Su dung: compass cd <agent-id>{Colors.ENDC}")
        else:
            cmd_cd(sys.argv[2])
    elif command == "help" or command == "-h" or command == "--help":
        cmd_help()
    else:
        print(f"{Colors.FAIL}[-] Lenh khong hop le: {command}{Colors.ENDC}")
        cmd_help()

if __name__ == "__main__":
    main()
