"""Shared test fixtures (offline only).

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


def _load(name: str) -> dict[str, Any]:
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


@pytest.fixture
def api_gateway_event() -> dict[str, Any]:
    return _load("api_gateway_event.json")


@pytest.fixture
def sqs_event() -> dict[str, Any]:
    return _load("sqs_event.json")


@pytest.fixture
def s3_event() -> dict[str, Any]:
    return _load("s3_event.json")


@pytest.fixture
def scheduled_event() -> dict[str, Any]:
    return _load("scheduled_event.json")
