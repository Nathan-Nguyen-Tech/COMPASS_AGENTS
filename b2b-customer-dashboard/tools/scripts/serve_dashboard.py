#!/usr/bin/env python3
"""
Local Web Server for B2B Customer Dashboard

Serves the generated dashboard HTML files on localhost.

Usage:
    python serve_dashboard.py
    python serve_dashboard.py --port 8080
    python serve_dashboard.py --dashboard path/to/dashboard.html
"""

import argparse
import http.server
import socketserver
import webbrowser
from pathlib import Path
import sys


class DashboardHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler for dashboard serving."""

    def __init__(self, *args, dashboard_file=None, **kwargs):
        self.dashboard_file = dashboard_file
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """Handle GET requests."""
        # Redirect root to dashboard
        if self.path == '/':
            if self.dashboard_file and self.dashboard_file.exists():
                self.path = '/' + str(self.dashboard_file.relative_to(self.directory))

        return super().do_GET()

    def end_headers(self):
        """Add CORS headers and cache control."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()


def find_latest_dashboard(dashboards_dir: Path) -> Path:
    """Find the most recently generated dashboard file."""
    dashboard_files = list(dashboards_dir.glob('dashboard_*.html'))

    if not dashboard_files:
        # Try default dashboard.html
        default_dashboard = dashboards_dir / 'dashboard.html'
        if default_dashboard.exists():
            return default_dashboard
        return None

    # Return most recent
    latest = max(dashboard_files, key=lambda p: p.stat().st_mtime)
    return latest


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Serve B2B Customer Dashboard on local web server"
    )

    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port to serve on (default: 8000)'
    )

    parser.add_argument(
        '--dashboard',
        type=str,
        help='Path to specific dashboard file (default: latest in workspace/dashboards/generated/)'
    )

    parser.add_argument(
        '--no-browser',
        action='store_true',
        help='Do not automatically open browser'
    )

    args = parser.parse_args()

    # Determine project root
    project_root = Path(__file__).parent.parent.parent
    dashboards_dir = project_root / 'workspace' / 'dashboards' / 'generated'

    # Find dashboard file
    if args.dashboard:
        dashboard_file = Path(args.dashboard)
        if not dashboard_file.exists():
            print(f"❌ Dashboard file not found: {dashboard_file}")
            sys.exit(1)
        serve_dir = dashboard_file.parent
    else:
        dashboard_file = find_latest_dashboard(dashboards_dir)
        if not dashboard_file:
            print("❌ No dashboard found!")
            print()
            print("Generate a dashboard first:")
            print("  /generate-dashboard")
            print()
            print(f"Expected location: {dashboards_dir}")
            sys.exit(1)
        serve_dir = dashboards_dir

    print()
    print("🌐 Starting B2B Customer Dashboard Server...")
    print("━" * 60)
    print()
    print(f"📊 Dashboard: {dashboard_file.name}")
    print(f"📁 Serving from: {serve_dir}")
    print(f"🔌 Port: {args.port}")
    print()

    # Change to serve directory
    import os
    os.chdir(serve_dir)

    # Create server
    Handler = lambda *args, **kwargs: DashboardHTTPRequestHandler(
        *args,
        dashboard_file=dashboard_file,
        **kwargs
    )

    try:
        with socketserver.TCPServer(("", args.port), Handler) as httpd:
            url = f"http://localhost:{args.port}/{dashboard_file.name}"

            print("✅ Server started successfully!")
            print()
            print(f"🌐 Dashboard URL: {url}")
            print()
            print("━" * 60)
            print()
            print("📖 Instructions:")
            print("  • Open the URL above in your browser")
            print("  • Use Ctrl+C to stop the server")
            print("  • Dashboard will auto-refresh when you regenerate")
            print()
            print("━" * 60)
            print()

            # Open browser automatically
            if not args.no_browser:
                print("🔗 Opening dashboard in browser...")
                webbrowser.open(url)
                print()

            print("🟢 Server running... (Press Ctrl+C to stop)")
            print()

            # Serve forever
            httpd.serve_forever()

    except KeyboardInterrupt:
        print()
        print()
        print("🛑 Server stopped by user")
        print()
        sys.exit(0)

    except OSError as e:
        if e.errno == 10048:  # Port already in use (Windows)
            print(f"❌ Port {args.port} is already in use!")
            print()
            print("Try a different port:")
            print(f"  python serve_dashboard.py --port {args.port + 1}")
            print()
            sys.exit(1)
        else:
            raise


if __name__ == '__main__':
    main()
