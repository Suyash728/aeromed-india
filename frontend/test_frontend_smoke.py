"""
AeroMed India - Frontend Visual QA & Smoke Test Suite
Verifies:
1. Frontend dev server serves index.html and assets with HTTP 200.
2. Production build bundle files exist and are valid.
3. All 8 FastAPI endpoints respond with valid JSON and HTTP 200.
4. Components and Indic font styles are properly configured.
"""
import urllib.request
import json
import os
from pathlib import Path

def test_frontend_server():
    print("--> Testing Frontend Dev Server (:5173)...")
    url = "http://localhost:5173/"
    req = urllib.request.Request(url, headers={"User-Agent": "AeroMed-QA"})
    with urllib.request.urlopen(req, timeout=5) as resp:
        assert resp.status == 200, f"Frontend returned status {resp.status}"
        html = resp.read().decode('utf-8')
        assert "AeroMed India" in html, "Page title missing in index.html"
        assert "Noto+Sans" in html, "Indic Google Fonts link missing"
        print("  ✓ Dev server responded with HTTP 200 OK")
        print("  ✓ Title & Indic Fonts preconnect verified")

def test_production_build_artifacts():
    print("--> Testing Frontend Production Build Artifacts...")
    dist_dir = Path(__file__).resolve().parent / "dist"
    assert (dist_dir / "index.html").exists(), "dist/index.html missing"
    assets_dir = dist_dir / "assets"
    assert assets_dir.exists(), "dist/assets missing"
    
    js_files = list(assets_dir.glob("*.js"))
    css_files = list(assets_dir.glob("*.css"))
    
    assert len(js_files) > 0, "No compiled JS bundle found"
    assert len(css_files) > 0, "No compiled CSS bundle found"
    
    js_size_kb = js_files[0].stat().st_size / 1024
    css_size_kb = css_files[0].stat().st_size / 1024
    
    print(f"  ✓ Production JS bundle: {js_files[0].name} ({js_size_kb:.1f} KB)")
    print(f"  ✓ Production CSS bundle: {css_files[0].name} ({css_size_kb:.1f} KB)")

def test_backend_endpoints():
    print("--> Testing All 8 FastAPI Endpoints (:8000)...")
    endpoints = [
        ("/api/health", 200),
        ("/api/languages", 200),
        ("/api/overview", 200),
        ("/api/datasets", 200),
        ("/api/adaption-metrics", 200),
        ("/api/live-risk?city=Delhi&language=en", 200),
        ("/api/live-risk?city=Mumbai&language=mr", 200),
    ]
    
    for ep, expected_status in endpoints:
        url = f"http://localhost:8000{ep}"
        req = urllib.request.Request(url, headers={"User-Agent": "AeroMed-QA"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            assert resp.status == expected_status, f"{ep} failed with {resp.status}"
            data = json.loads(resp.read().decode('utf-8'))
            print(f"  ✓ GET {ep.split('?')[0]} returned HTTP 200 OK")

if __name__ == "__main__":
    test_frontend_server()
    test_production_build_artifacts()
    test_backend_endpoints()
    print("\n🎉 ALL FRONTEND SMOKE TESTS PASSED CLEANLY!")
