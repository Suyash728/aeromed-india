"""
Test fixtures: keep the suite offline and deterministic by default.

Every test runs with Open-Meteo and the Adaption client stubbed out, so results do not
depend on today's weather, network access, or an API key. Set AEROMED_LIVE_TESTS=1 to
run the same tests against the real services.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import main  # noqa: E402

LIVE = os.environ.get("AEROMED_LIVE_TESTS") == "1"

# Fixed hourly reading used for every stubbed Open-Meteo location.
STUB_CURRENT_AIR = {
    "pm2_5": 58.0, "pm10": 95.0, "nitrogen_dioxide": 28.0, "sulphur_dioxide": 15.0,
    "ozone": 30.0, "carbon_monoxide": 800.0, "us_aqi": 152,
}
STUB_CURRENT_WEATHER = {"temperature_2m": 27.5, "relative_humidity_2m": 68.0}


class _StubResponse:
    status_code = 200

    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self._payload


def _stub_get(url, params=None, timeout=None, **kwargs):
    params = params or {}
    if "air-quality-api.open-meteo.com" in url:
        n = len(str(params.get("latitude", "")).split(","))
        one = {"current": dict(STUB_CURRENT_AIR)}
        return _StubResponse([one] * n if n > 1 else one)
    if "api.open-meteo.com" in url:
        return _StubResponse({"current": dict(STUB_CURRENT_WEATHER)})
    raise AssertionError(f"Unexpected network call in offline test: {url}")


@pytest.fixture(autouse=True)
def offline_services(monkeypatch):
    main.live_map_cache.update({"timestamp": 0, "data": None})
    main.live_risk_cache.clear()
    main.triage_chat_cache.clear()
    if not LIVE:
        monkeypatch.setattr(main.requests, "get", _stub_get)
        monkeypatch.setattr(main, "get_adaption_client", lambda: None)
    yield
