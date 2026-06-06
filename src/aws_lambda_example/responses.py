"""Response helpers for API Gateway proxy integration.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

import json
from typing import Any

from aws_lambda_example.types import ProxyResponse

_JSON_HEADERS = {"Content-Type": "application/json"}


def json_response(
    body: Any,
    status_code: int = 200,
    *,
    headers: dict[str, str] | None = None,
) -> ProxyResponse:
    """Build an API Gateway proxy response with a JSON-encoded body."""
    merged = {**_JSON_HEADERS, **(headers or {})}
    return {
        "statusCode": status_code,
        "headers": merged,
        "body": json.dumps(body, separators=(",", ":")),
    }


def error_response(
    message: str,
    status_code: int = 400,
    *,
    code: str | None = None,
    headers: dict[str, str] | None = None,
) -> ProxyResponse:
    """Build a standardized JSON error response."""
    payload: dict[str, Any] = {"error": message}
    if code is not None:
        payload["code"] = code
    return json_response(payload, status_code=status_code, headers=headers)
