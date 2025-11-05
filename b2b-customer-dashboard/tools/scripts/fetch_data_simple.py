#!/usr/bin/env python3
"""
Simple Google Sheets Data Fetcher
Fetches data without emoji output to avoid encoding issues.
"""

import json
import os
import sys
from pathlib import Path

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Error: Google API packages not installed.")
    print("Install with: pip install google-auth google-api-python-client")
    sys.exit(1)

# Configuration
CREDENTIALS_PATH = r"D:\Compass_Coding\COMPASS_AGENTS\claude-code-meta-builder\config\service-account-key.json"
SPREADSHEET_ID = "1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A"
SHEET_NAME = "2025_B2B_PotentialCustomersManagement_Upgrade"
OUTPUT_PATH = "workspace/data/real_sheets_data.json"

def fetch_data():
    """Fetch data from Google Sheets."""
    print("Authenticating with Google Sheets API...")

    try:
        # Authenticate
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_PATH,
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )
        service = build('sheets', 'v4', credentials=credentials)
        print("Authentication successful")

        # Get spreadsheet metadata to find sheets
        print(f"Fetching spreadsheet metadata...")
        spreadsheet = service.spreadsheets().get(
            spreadsheetId=SPREADSHEET_ID
        ).execute()

        # List all available sheets
        print("\nAvailable sheets:")
        for sheet in spreadsheet['sheets']:
            sheet_title = sheet['properties']['title']
            print(f"  - {sheet_title}")

        # Try to use the specified sheet name, or use first sheet
        target_sheet = SHEET_NAME
        available_sheets = [s['properties']['title'] for s in spreadsheet['sheets']]

        if SHEET_NAME not in available_sheets:
            print(f"\nWarning: Sheet '{SHEET_NAME}' not found.")
            target_sheet = available_sheets[0]
            print(f"Using first available sheet: '{target_sheet}'")
        else:
            print(f"\nUsing sheet: '{target_sheet}'")

        # Fetch data
        print(f"Fetching data from sheet: {target_sheet}...")
        range_name = f"{target_sheet}!A:ZZ"
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name
        ).execute()

        values = result.get('values', [])

        if not values:
            print("No data found in spreadsheet")
            return None

        # Convert to list of dictionaries
        headers = values[0]
        data = []

        print(f"Processing {len(values)-1} rows with {len(headers)} columns...")

        for row_idx, row in enumerate(values[1:], start=2):
            # Pad row if shorter than headers
            while len(row) < len(headers):
                row.append('')

            record = {}
            for i, header in enumerate(headers):
                record[header] = row[i] if i < len(row) else ''

            data.append(record)

        print(f"Successfully processed {len(data)} records")

        # Save metadata
        metadata = {
            'spreadsheet_id': SPREADSHEET_ID,
            'sheet_name': target_sheet,
            'total_rows': len(data),
            'total_columns': len(headers),
            'column_headers': headers,
            'available_sheets': available_sheets,
            'data': data
        }

        return metadata

    except HttpError as e:
        print(f"Google Sheets API error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Main entry point."""
    print("=" * 60)
    print("B2B Customer Data Fetcher")
    print("=" * 60)
    print()

    # Verify credentials file exists
    if not Path(CREDENTIALS_PATH).exists():
        print(f"Error: Credentials file not found: {CREDENTIALS_PATH}")
        sys.exit(1)

    # Fetch data
    metadata = fetch_data()

    if not metadata:
        print("\nFailed to fetch data")
        sys.exit(1)

    # Save to JSON
    output_file = Path(OUTPUT_PATH)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"\nSaving data to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"Data saved successfully!")
    print()
    print("Summary:")
    print(f"  - Sheet: {metadata['sheet_name']}")
    print(f"  - Total rows: {metadata['total_rows']}")
    print(f"  - Total columns: {metadata['total_columns']}")
    print(f"  - Output: {output_file}")
    print()
    print("=" * 60)

if __name__ == '__main__':
    main()
