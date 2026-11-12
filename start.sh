#!/bin/bash
# Start script for Pan-India AQI & Respiratory Surveillance API

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

PORT="${PORT:-8000}"

echo "=========================================================="
echo " Starting Pan-India AQI & Respiratory Surveillance API"
echo " Host: http://localhost:$PORT"
echo " Docs: http://localhost:$PORT/docs"
echo "=========================================================="

"$SCRIPT_DIR/.venv/bin/uvicorn" main:app --host 0.0.0.0 --port "$PORT" --reload
