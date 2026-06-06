"""Offline tests for each handler using sample events.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

import json
from typing import Any

from aws_lambda_example.handlers import (
    api_gateway_handler,
    s3_event_handler,
    scheduled_handler,
    sqs_handler,
)


def test_api_gateway_echo(api_gateway_event: dict[str, Any]) -> None:
    resp = api_gateway_handler(api_gateway_event, None)
    assert resp["statusCode"] == 201
    body = json.loads(resp["body"])
    assert body["echo"] == {"message": "hello from viprasol"}


def test_api_gateway_health() -> None:
    resp = api_gateway_handler({"httpMethod": "GET", "path": "/health"}, None)
    assert resp["statusCode"] == 200
    assert json.loads(resp["body"]) == {"status": "ok"}


def test_sqs_success(sqs_event: dict[str, Any]) -> None:
    result = sqs_handler(sqs_event, None)
    assert result == {"batchItemFailures": []}


def test_sqs_partial_failure() -> None:
    event = {
        "Records": [
            {"messageId": "ok", "body": '{"v":1}'},
            {"messageId": "bad", "body": "{not json"},
        ]
    }
    result = sqs_handler(event, None)
    assert result["batchItemFailures"] == [{"itemIdentifier": "bad"}]


def test_s3_event_extracts_objects(s3_event: dict[str, Any]) -> None:
    result = s3_event_handler(s3_event, None)
    assert result["processed"] == 1
    # URL-decoded key (the '+' becomes a space).
    assert result["objects"][0] == {
        "bucket": "viprasol-uploads",
        "key": "incoming/report 2025.csv",
    }


def test_scheduled_handler(scheduled_event: dict[str, Any]) -> None:
    result = scheduled_handler(scheduled_event, None)
    assert result["ran"] is True
    assert result["source"] == "aws.events"
