"""Tests for the router and middleware.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

import json

from aws_lambda_example.errors import BadRequest
from aws_lambda_example.responses import json_response
from aws_lambda_example.router import Router
from aws_lambda_example.types import LambdaContext, LambdaEvent, ProxyResponse


def _build() -> Router:
    router = Router()

    @router.route("GET", "/ping")
    def _ping(event: LambdaEvent, context: LambdaContext) -> ProxyResponse:
        return json_response({"pong": True})

    @router.route("POST", "/data")
    def _data(event: LambdaEvent, context: LambdaContext) -> ProxyResponse:
        return json_response({"received": event["json"]})

    @router.route("GET", "/boom")
    def _boom(event: LambdaEvent, context: LambdaContext) -> ProxyResponse:
        raise BadRequest("nope")

    return router


def test_route_match() -> None:
    resp = _build().handle({"httpMethod": "GET", "path": "/ping"})
    assert resp["statusCode"] == 200
    assert json.loads(resp["body"]) == {"pong": True}


def test_json_body_parsing_middleware() -> None:
    event = {"httpMethod": "POST", "path": "/data", "body": '{"x":1}'}
    resp = _build().handle(event)
    assert json.loads(resp["body"]) == {"received": {"x": 1}}


def test_unknown_route_404() -> None:
    resp = _build().handle({"httpMethod": "GET", "path": "/missing"})
    assert resp["statusCode"] == 404
    assert json.loads(resp["body"])["code"] == "not_found"


def test_invalid_json_body_400() -> None:
    event = {"httpMethod": "POST", "path": "/data", "body": "{not json"}
    resp = _build().handle(event)
    assert resp["statusCode"] == 400


def test_http_error_to_response() -> None:
    resp = _build().handle({"httpMethod": "GET", "path": "/boom"})
    assert resp["statusCode"] == 400
    assert json.loads(resp["body"])["error"] == "nope"
