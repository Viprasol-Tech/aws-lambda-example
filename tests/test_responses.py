"""Tests for response helpers.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

import json

from aws_lambda_example.responses import error_response, json_response


def test_json_response_defaults() -> None:
    resp = json_response({"a": 1})
    assert resp["statusCode"] == 200
    assert resp["headers"]["Content-Type"] == "application/json"
    assert json.loads(resp["body"]) == {"a": 1}


def test_json_response_custom_status_and_headers() -> None:
    resp = json_response({"ok": True}, status_code=201, headers={"X-Trace": "abc"})
    assert resp["statusCode"] == 201
    assert resp["headers"]["X-Trace"] == "abc"


def test_error_response_includes_code() -> None:
    resp = error_response("nope", status_code=404, code="not_found")
    assert resp["statusCode"] == 404
    body = json.loads(resp["body"])
    assert body == {"error": "nope", "code": "not_found"}
