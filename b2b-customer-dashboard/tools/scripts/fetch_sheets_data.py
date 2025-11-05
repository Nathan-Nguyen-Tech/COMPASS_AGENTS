#!/usr/bin/env python3
"""
Google Sheets Data Fetcher

Fetches data from Google Sheets using service account credentials.
Designed to work with the B2B Customer Dashboard project.

Usage:
    python fetch_sheets_data.py
    python fetch_sheets_data.py --output data.json
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("ERROR - Google API packages not installed.")
    print("Install with: pip install google-auth google-api-python-client")
    sys.exit(1)


class GoogleSheetsFetcher:
    """Fetch data from Google Sheets using service account."""

    def __init__(self, credentials_path: str):
        """
        Initialize fetcher with service account credentials.

        Args:
            credentials_path: Path to service account JSON file
        """
        self.credentials_path = credentials_path
        self.service = None
        self._authenticate()

    def _authenticate(self):
        """Authenticate with Google Sheets API."""
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_path,
                scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
            )
            self.service = build('sheets', 'v4', credentials=credentials)
            print("OK - Authenticated with Google Sheets API")
        except Exception as e:
            print(f"ERROR - Authentication failed: {e}")
            sys.exit(1)

    def fetch_spreadsheet(self, spreadsheet_id: str, sheet_name: str = None) -> List[Dict[str, Any]]:
        """
        Fetch data from a Google Spreadsheet.

        Args:
            spreadsheet_id: Google Sheets spreadsheet ID
            sheet_name: Optional sheet name (uses first sheet if not specified)

        Returns:
            List of dictionaries (one per row)
        """
        try:
            # Get spreadsheet metadata
            spreadsheet = self.service.spreadsheets().get(
                spreadsheetId=spreadsheet_id
            ).execute()

            # Determine sheet name
            if not sheet_name:
                sheet_name = spreadsheet['sheets'][0]['properties']['title']

            print(f"Fetching data from sheet: {sheet_name}")

            # Fetch data
            range_name = f"{sheet_name}!A:ZZ"  # All columns
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=range_name
            ).execute()

            values = result.get('values', [])

            if not values:
                print("WARNING - No data found in spreadsheet")
                return []

            # Convert to list of dictionaries
            headers = values[0]
            data = []

            for row in values[1:]:
                # Pad row if it's shorter than headers
                while len(row) < len(headers):
                    row.append('')

                record = {}
                for i, header in enumerate(headers):
                    record[header] = row[i] if i < len(row) else ''

                data.append(record)

            print(f"OK - Fetched {len(data)} records with {len(headers)} columns")

            return data

        except HttpError as e:
            print(f"ERROR - Google Sheets API error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"ERROR - Error fetching data: {e}")
            sys.exit(1)

    def save_to_json(self, data: List[Dict], output_path: str):
        """Save data to JSON file."""
        try:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"OK - Data saved to: {output_file}")
        except Exception as e:
            print(f"ERROR - Error saving data: {e}")
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch data from Google Sheets"
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
        help='Sheet name (optional, uses first sheet if not specified)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='workspace/data/sheets_data.json',
        help='Output JSON file path'
    )

    args = parser.parse_args()

    # Get configuration from environment or args
    credentials_path = args.credentials or os.getenv('GDRIVE_CREDENTIALS_PATH')
    spreadsheet_id = args.spreadsheet_id or os.getenv('SPREADSHEET_ID')
    sheet_name = args.sheet_name or os.getenv('SPREADSHEET_NAME')

    if not credentials_path:
        print("ERROR - Credentials path not provided")
        print("Set GDRIVE_CREDENTIALS_PATH environment variable or use --credentials")
        sys.exit(1)

    if not spreadsheet_id:
        print("ERROR - Spreadsheet ID not provided")
        print("Set SPREADSHEET_ID environment variable or use --spreadsheet-id")
        sys.exit(1)

    # Verify credentials file exists
    if not Path(credentials_path).exists():
        print(f"ERROR - Credentials file not found: {credentials_path}")
        sys.exit(1)

    print("B2B Customer Data Fetcher")
    print("=" * 50)
    print(f"Credentials: {credentials_path}")
    print(f"Spreadsheet ID: {spreadsheet_id}")
    print(f"Sheet Name: {sheet_name or '(first sheet)'}")
    print(f"Output: {args.output}")
    print("=" * 50)

    # Fetch data
    fetcher = GoogleSheetsFetcher(credentials_path)
    data = fetcher.fetch_spreadsheet(spreadsheet_id, sheet_name)

    # Save to JSON
    fetcher.save_to_json(data, args.output)

    print()
    print("Data fetch complete!")
    print()


if __name__ == '__main__':
    main()
