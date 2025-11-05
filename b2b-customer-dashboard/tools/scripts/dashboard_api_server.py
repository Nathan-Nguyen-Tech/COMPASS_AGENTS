#!/usr/bin/env python3
"""
Dashboard API Server

Lightweight Flask server to provide API endpoints for interactive dashboard.
Allows dashboard to trigger data refresh and filter changes via AJAX.

Usage:
    python dashboard_api_server.py
    # Server runs on http://localhost:5000
"""

import os
import sys
import json
import subprocess
import threading
from pathlib import Path
from datetime import datetime
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent.parent
DASHBOARD_DIR = PROJECT_ROOT / "workspace" / "dashboards" / "generated"
DATA_DIR = PROJECT_ROOT / "workspace" / "data"
SCRIPTS_DIR = PROJECT_ROOT / "tools" / "scripts"

# Global state
generation_status = {
    'is_generating': False,
    'progress': '',
    'error': None,
    'last_generated': None
}


def run_dashboard_generation(dashboard_type='monthly', year=None, month=None, quarter=None, refresh_data=False):
    """Run dashboard generation in background thread."""
    global generation_status

    generation_status['is_generating'] = True
    generation_status['progress'] = 'Starting generation...'
    generation_status['error'] = None

    try:
        # Build command
        if refresh_data:
            # Fetch fresh data from Google Sheets
            generation_status['progress'] = 'Fetching data from Google Sheets...'
            cmd = [
                sys.executable,
                str(SCRIPTS_DIR / 'generate_full_dashboard.py'),
                '--type', dashboard_type
            ]
        else:
            # Use cached data
            generation_status['progress'] = 'Using cached data...'
            cmd = [
                sys.executable,
                str(SCRIPTS_DIR / 'generate_full_dashboard.py'),
                '--cache-data',
                '--type', dashboard_type
            ]

        # Add filters
        if year:
            cmd.extend(['--year', str(year)])
        if month and dashboard_type == 'monthly':
            cmd.extend(['--month', str(month)])
        if quarter and dashboard_type == 'quarterly':
            cmd.extend(['--quarter', str(quarter)])

        cmd.extend(['--output', str(DASHBOARD_DIR / 'dashboard.html')])

        # Run generation
        generation_status['progress'] = 'Generating dashboard...'
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=180,  # 3 minutes timeout
            cwd=str(PROJECT_ROOT)
        )

        if result.returncode == 0:
            generation_status['progress'] = 'Dashboard generated successfully!'
            generation_status['last_generated'] = datetime.now().isoformat()
        else:
            generation_status['error'] = f"Generation failed: {result.stderr}"
            generation_status['progress'] = 'Generation failed'

    except subprocess.TimeoutExpired:
        generation_status['error'] = 'Generation timeout (>3 minutes)'
        generation_status['progress'] = 'Timeout'
    except Exception as e:
        generation_status['error'] = str(e)
        generation_status['progress'] = 'Error occurred'
    finally:
        generation_status['is_generating'] = False


@app.route('/')
def index():
    """Serve dashboard HTML."""
    return send_from_directory(DASHBOARD_DIR, 'dashboard.html')


@app.route('/api/status')
def get_status():
    """Get current generation status."""
    return jsonify(generation_status)


@app.route('/api/generate', methods=['POST'])
def generate_dashboard():
    """
    Trigger dashboard generation with filters.

    Request body:
    {
        "type": "monthly" | "quarterly",
        "year": 2025,
        "month": 6,  // if type=monthly
        "quarter": 2  // if type=quarterly
    }
    """
    if generation_status['is_generating']:
        return jsonify({
            'success': False,
            'error': 'Dashboard generation already in progress'
        }), 429

    data = request.get_json() or {}
    dashboard_type = data.get('type', 'monthly')
    year = data.get('year')
    month = data.get('month')
    quarter = data.get('quarter')

    # Start generation in background thread
    thread = threading.Thread(
        target=run_dashboard_generation,
        args=(dashboard_type, year, month, quarter, False)
    )
    thread.daemon = True
    thread.start()

    return jsonify({
        'success': True,
        'message': 'Dashboard generation started',
        'status_url': '/api/status'
    })


@app.route('/api/refresh', methods=['POST'])
def refresh_data():
    """
    Refresh data from Google Sheets and regenerate dashboard.
    """
    if generation_status['is_generating']:
        return jsonify({
            'success': False,
            'error': 'Dashboard generation already in progress'
        }), 429

    data = request.get_json() or {}
    dashboard_type = data.get('type', 'monthly')
    year = data.get('year')
    month = data.get('month')
    quarter = data.get('quarter')

    # Start generation with data refresh in background thread
    thread = threading.Thread(
        target=run_dashboard_generation,
        args=(dashboard_type, year, month, quarter, True)
    )
    thread.daemon = True
    thread.start()

    return jsonify({
        'success': True,
        'message': 'Data refresh and dashboard generation started',
        'status_url': '/api/status'
    })


@app.route('/api/data-info')
def get_data_info():
    """Get information about cached data."""
    data_file = DATA_DIR / 'real_data.json'

    if not data_file.exists():
        return jsonify({
            'exists': False,
            'error': 'No cached data found'
        })

    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        stats = data_file.stat()

        return jsonify({
            'exists': True,
            'record_count': len(data),
            'file_size': stats.st_size,
            'last_modified': datetime.fromtimestamp(stats.st_mtime).isoformat()
        })
    except Exception as e:
        return jsonify({
            'exists': True,
            'error': str(e)
        })


def main():
    """Start the API server."""
    print("=" * 70)
    print("DASHBOARD API SERVER")
    print("=" * 70)
    print()
    print("Server starting...")
    print(f"Dashboard directory: {DASHBOARD_DIR}")
    print(f"Data directory: {DATA_DIR}")
    print()
    print("API Endpoints:")
    print("  GET  /                 - View dashboard")
    print("  GET  /api/status       - Get generation status")
    print("  POST /api/generate     - Generate dashboard with filters")
    print("  POST /api/refresh      - Refresh data and regenerate")
    print("  GET  /api/data-info    - Get cached data info")
    print()
    print("=" * 70)
    print()
    print("Dashboard will be available at:")
    print("  http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    print("=" * 70)

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        threaded=True
    )


if __name__ == '__main__':
    main()
