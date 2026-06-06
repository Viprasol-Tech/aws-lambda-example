"""Tests for the offline local-invoke harness.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from aws_lambda_example.harness import HandlerName, invoke, load_event, main

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


def test_load_event_roundtrip() -> None:
    event = load_event(EXAMPLES / "scheduled_event.json")
    assert event["source"] == "aws.events"


def test_invoke_scheduled() -> None:
    event = load_event(EXAMPLES / "scheduled_event.json")
    result = invoke(HandlerName.SCHEDULED, event)
    assert result["ran"] is True


def test_main_runs_offline(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["sqs", str(EXAMPLES / "sqs_event.json")])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "batchItemFailures" in out


def test_handler_names_complete() -> None:
    assert {h.value for h in HandlerName} == {"api_gateway", "sqs", "s3", "scheduled"}
