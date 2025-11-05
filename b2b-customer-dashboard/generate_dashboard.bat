@echo off
REM B2B Customer Dashboard Generator - Windows Batch Script
REM This script loads environment variables and runs the dashboard generator

REM Set working directory
cd /d "%~dp0"

REM Load environment variables from .env file
for /f "usebackq tokens=1,2 delims==" %%a in (".env") do (
    if not "%%a"=="" if not "%%b"=="" (
        set "%%a=%%b"
    )
)

REM Run dashboard generator with UTF-8 encoding
python -X utf8 tools\scripts\generate_full_dashboard.py %*
