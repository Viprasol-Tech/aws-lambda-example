"""A tiny router + middleware for API Gateway proxy events.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).

The router matches (method, path) pairs to handler callables, wraps them with
middleware (logging, error-to-response, JSON parsing), and returns proxy
responses. It is intentionally dependency-free and runs fully offline.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

from aws_lambda_example.errors import BadRequest, HttpError, NotFound
from aws_lambda_example.logging_config import get_logger
from aws_lambda_example.responses import error_response, json_response
from aws_lambda_example.types import LambdaContext, LambdaEvent, ProxyResponse

_log = get_logger(__name__)

# A route handler receives the event (augmented with a parsed `json` body) and
# the Lambda context, and returns a proxy response dict.
RouteHandler = Callable[[LambdaEvent, LambdaContext], ProxyResponse]


class Router:
    """Maps (method, path) to handlers and dispatches proxy events."""

    def __init__(self) -> None:
        self._routes: dict[tuple[str, str], RouteHandler] = {}

    def add(self, method: str, path: str, handler: RouteHandler) -> None:
        """Register a handler for an HTTP method + path."""
        self._routes[(method.upper(), path)] = handler

    def route(self, method: str, path: str) -> Callable[[RouteHandler], RouteHandler]:
        """Decorator form of :meth:`add`."""

        def decorator(handler: RouteHandler) -> RouteHandler:
            self.add(method, path, handler)
            return handler

        return decorator

    def dispatch(self, event: LambdaEvent, context: LambdaContext = None) -> ProxyResponse:
        """Resolve and invoke the matching handler with middleware applied."""
        method = str(event.get("httpMethod", "GET")).upper()
        path = str(event.get("path", "/"))
        _log.info("dispatch %s %s", method, path)

        handler = self._routes.get((method, path))
        if handler is None:
            raise NotFound(f"No route for {method} {path}")

        enriched = {**event, "json": _parse_json_body(event)}
        return handler(enriched, context)

    def handle(self, event: LambdaEvent, context: LambdaContext = None) -> ProxyResponse:
        """Top-level entry point: dispatch and convert errors to responses."""
        try:
            return self.dispatch(event, context)
        except HttpError as exc:
            _log.warning("http error %s: %s", exc.status_code, exc.message)
            return error_response(exc.message, status_code=exc.status_code, code=exc.code)
        except Exception as exc:
            _log.exception("unhandled error")
            return error_response(
                f"Internal server error: {exc}", status_code=500, code="internal_error"
            )


def _parse_json_body(event: LambdaEvent) -> Any:
    """Parse the request body as JSON, tolerating empty bodies."""
    body = event.get("body")
    if body is None or body == "":
        return None
    if isinstance(body, (dict, list)):
        return body
    try:
        return json.loads(body)
    except (json.JSONDecodeError, TypeError) as exc:
        raise BadRequest("Request body is not valid JSON") from exc


__all__ = ["RouteHandler", "Router", "json_response"]
