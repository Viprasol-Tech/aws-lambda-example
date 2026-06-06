"""API Gateway proxy handler wired through the router + middleware.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

from typing import Any

from aws_lambda_example.errors import BadRequest
from aws_lambda_example.responses import json_response
from aws_lambda_example.router import Router
from aws_lambda_example.types import LambdaContext, LambdaEvent, ProxyResponse

router = Router()


@router.route("GET", "/health")
def _health(event: LambdaEvent, context: LambdaContext) -> ProxyResponse:
    return json_response({"status": "ok"})


@router.route("POST", "/echo")
def _echo(event: LambdaEvent, context: LambdaContext) -> ProxyResponse:
    body: Any = event.get("json")
    if not isinstance(body, dict):
        raise BadRequest("Expected a JSON object body")
    return json_response({"echo": body}, status_code=201)


def handler(event: LambdaEvent, context: LambdaContext = None) -> ProxyResponse:
    """Lambda entry point for API Gateway proxy integration."""
    return router.handle(event, context)
