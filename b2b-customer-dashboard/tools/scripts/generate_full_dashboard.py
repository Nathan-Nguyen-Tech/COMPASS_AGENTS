#!/usr/bin/env python3
"""
Full Dashboard Generator

Orchestrates the complete dashboard generation process:
1. Fetch data from Google Sheets
2. Process and filter data
3. Generate all charts
4. Create HTML dashboard

Usage:
    python generate_full_dashboard.py
    python generate_full_dashboard.py --type monthly --year 2025
"""

import argparse
import json
import os
import sys
import webbrowser
from pathlib import Path
from datetime import datetime

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from fetch_sheets_data import GoogleSheetsFetcher
    from dashboard_generator import DashboardGenerator
except ImportError as e:
    print(f"ERROR - Import error: {e}")
    print("Make sure all required scripts are in the same directory")
    sys.exit(1)


def main():
    """Main orchestration function."""
    parser = argparse.ArgumentParser(
        description="Generate complete B2B Customer Dashboard from Google Sheets"
    )

    parser.add_argument(
        '--credentials',
        type=str,
        help='Path to service account credentials JSON'
    )

    parser.add_argument(
        '--spreadsheet-id',
        type=str,
        help='Google Sheets spreadsheet ID'
    )

    parser.add_argument(
        '--sheet-name',
        type=str,
        help='Sheet name (optional)'
    )

    parser.add_argument(
        '--type',
        type=str,
        choices=['monthly', 'quarterly'],
        default='monthly',
        help='Dashboard type (default: monthly)'
    )

    parser.add_argument(
        '--year',
        type=int,
        help='Year filter (e.g., 2025)'
    )

    parser.add_argument(
        '--month',
        type=int,
        choices=range(1, 13),
        help='Month filter (1-12)'
    )

    parser.add_argument(
        '--quarter',
        type=int,
        choices=range(1, 5),
        help='Quarter filter (1-4)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output HTML file path'
    )

    parser.add_argument(
        '--cache-data',
        action='store_true',
        help='Cache fetched data for faster regeneration'
    )

    parser.add_argument(
        '--no-browser',
        action='store_true',
        help='Do not automatically open dashboard in browser'
    )

    args = parser.parse_args()

    # Get configuration from environment or args
    credentials_path = args.credentials or os.getenv('GDRIVE_CREDENTIALS_PATH')
    spreadsheet_id = args.spreadsheet_id or os.getenv('SPREADSHEET_ID')
    sheet_name = args.sheet_name or os.getenv('SPREADSHEET_NAME')

    # Use real_data.json as the cache file (standard location)
    cache_file = Path(__file__).parent.parent.parent / "workspace" / "data" / "real_data.json"

    # Validate required parameters (skip if using cached data and cache exists)
    if args.cache_data and cache_file.exists():
        # Using cached data - credentials not required
        pass
    else:
        # Fetching fresh data - credentials required
        if not credentials_path:
            print("ERROR - Credentials path not provided")
            print("Set GDRIVE_CREDENTIALS_PATH environment variable or use --credentials")
            print()
            print("TIP: If you want to use cached data, run:")
            print("  python tools/scripts/generate_full_dashboard.py --cache-data")
            sys.exit(1)

        if not spreadsheet_id:
            print("ERROR - Spreadsheet ID not provided")
            print("Set SPREADSHEET_ID environment variable or use --spreadsheet-id")
            sys.exit(1)

        if not Path(credentials_path).exists():
            print(f"ERROR - Credentials file not found: {credentials_path}")
            sys.exit(1)

    # Print configuration
    print("=" * 70)
    print("B2B CUSTOMER DASHBOARD GENERATOR")
    print("=" * 70)
    print()
    print(f"Data Source: Google Sheets")
    print(f"  Spreadsheet ID: {spreadsheet_id}")
    print(f"  Sheet Name: {sheet_name or '(first sheet)'}")
    print()
    print(f"Dashboard Configuration:")
    print(f"  Type: {args.type.capitalize()}")
    if args.year:
        print(f"  Year: {args.year}")
    if args.month:
        print(f"  Month: {args.month}")
    if args.quarter:
        print(f"  Quarter: Q{args.quarter}")
    if not args.year and not args.month and not args.quarter:
        print(f"  Filters: None (showing all data)")
    print()
    print("=" * 70)
    print()

    # Step 1: Fetch data from Google Sheets
    print("STEP 1/3: Fetching data from Google Sheets...")
    print("-" * 70)

    if args.cache_data and cache_file.exists():
        print(f"Using cached data from: {cache_file}")
        with open(cache_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"OK - Loaded {len(data)} records from cache")
    else:
        fetcher = GoogleSheetsFetcher(credentials_path)
        data = fetcher.fetch_spreadsheet(spreadsheet_id, sheet_name)

        # Always save to real_data.json for consistency
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"OK - Data saved to: {cache_file}")

    print()

    # Step 2: Generate dashboard
    print("STEP 2/3: Generating interactive dashboard...")
    print("-" * 70)

    generator = DashboardGenerator()
    output_path = generator.generate(
        data=data,
        dashboard_type=args.type,
        year=args.year,
        month=args.month,
        quarter=args.quarter,
        output_path=args.output
    )

    if not output_path:
        print("ERROR - Dashboard generation failed")
        sys.exit(1)

    print()

    # Step 3: Summary and next steps
    print("STEP 3/3: Dashboard ready!")
    print("-" * 70)
    print()
    print("OK - Dashboard generated successfully!")
    print()
    print(f"File Location:")
    print(f"  {Path(output_path).absolute()}")
    print()
    print(f"Open in Browser:")
    print(f"  file:///{Path(output_path).absolute().as_posix()}")
    print()
    print(f"Quick View (Start Web Server):")
    print(f"  python tools/scripts/serve_dashboard.py")
    print()
    print(f"Refresh with Latest Data:")
    print(f"  python {Path(__file__).name}")
    print()
    print(f"Use Cached Data (Faster):")
    print(f"  python {Path(__file__).name} --cache-data")
    print()

    # Auto-open dashboard in browser (unless --no-browser flag)
    if not args.no_browser:
        print("Opening dashboard in browser...")
        try:
            webbrowser.open(f'file:///{Path(output_path).absolute().as_posix()}')
            print("OK - Dashboard opened in your default browser!")
        except Exception as e:
            print(f"WARNING - Could not open browser automatically: {e}")
            print(f"Please open manually: {Path(output_path).absolute()}")
        print()

    print("=" * 70)
    print()


if __name__ == '__main__':
    main()
