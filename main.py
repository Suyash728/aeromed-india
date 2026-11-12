"""
Root Entrypoint Proxy for Render Cloud & Container Deployments.
Ensures seamless execution when Render or external hosts run `uvicorn main:app`
from the repository root directory.
"""
import os
import sys

# Add backend directory to sys.path so modules and imports resolve cleanly
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(CURRENT_DIR, "backend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# Import the FastAPI application instance from backend/main.py
from backend.main import app  # noqa: E402, F401
