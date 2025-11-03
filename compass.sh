#!/bin/bash
# COMPASS AGENTS CLI Wrapper for Linux/Mac
# Chạy: ./compass.sh <command> [args]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/compass.py" "$@"
