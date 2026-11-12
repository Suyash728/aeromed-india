#!/usr/bin/env bash
# ==============================================================================
# AeroMed India - Full-Stack Local Development Runner
# Spins up FastAPI Backend (:8000) and React Vite Frontend (:5173) simultaneously
# ==============================================================================

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$PROJECT_ROOT/backend"
FRONTEND_DIR="$PROJECT_ROOT/frontend"

echo "=================================================================="
echo " AeroMed India - Starting Monorepo Development Environment"
echo "=================================================================="

# Function to clean up background processes upon exit
cleanup() {
    echo ""
    echo "Stopping development servers..."
    if [ -n "$BACKEND_PID" ]; then
        kill "$BACKEND_PID" 2>/dev/null || true
    fi
    if [ -n "$FRONTEND_PID" ]; then
        kill "$FRONTEND_PID" 2>/dev/null || true
    fi
    exit 0
}

trap cleanup SIGINT SIGTERM EXIT

# 1. Start Backend
echo "--> Starting FastAPI Backend on http://localhost:8000..."
cd "$BACKEND_DIR"

if [ -f "$BACKEND_DIR/.venv/bin/uvicorn" ]; then
    PY_UVICORN="$BACKEND_DIR/.venv/bin/uvicorn"
elif command -v uvicorn >/dev/null 2>&1; then
    PY_UVICORN="uvicorn"
else
    echo "Virtual environment not detected at backend/.venv. Setting up with uv/python..."
    python3 -m venv "$BACKEND_DIR/.venv"
    "$BACKEND_DIR/.venv/bin/pip" install -r requirements.txt
    PY_UVICORN="$BACKEND_DIR/.venv/bin/uvicorn"
fi

"$PY_UVICORN" main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!
echo "Backend running (PID: $BACKEND_PID)"
echo "Docs available at http://localhost:8000/docs"

# 2. Start Frontend
if [ -d "$FRONTEND_DIR" ] && command -v npm >/dev/null 2>&1; then
    echo "--> Starting Vite Frontend on http://localhost:5173..."
    cd "$FRONTEND_DIR"
    if [ ! -d "node_modules" ]; then
        echo "Installing frontend dependencies (npm install)..."
        npm install
    fi
    npm run dev &
    FRONTEND_PID=$!
    echo "Frontend running (PID: $FRONTEND_PID)"
else
    echo "Notice: npm not found or frontend directory missing. Backend only is active."
fi

echo "=================================================================="
echo " Ready! Press Ctrl+C to terminate both servers."
echo "=================================================================="

wait
