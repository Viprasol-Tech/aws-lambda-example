"""Domain errors that the router maps to HTTP responses.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations


class HttpError(Exception):
    """An error carrying an HTTP status code, rendered by the router."""

    status_code: int = 500
    code: str | None = None

    def __init__(self, message: str, *, status_code: int | None = None, code: str | None = None):
        super().__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        if code is not None:
            self.code = code


class BadRequest(HttpError):
    """400 — the request was malformed or failed validation."""

    status_code = 400
    code = "bad_request"


class NotFound(HttpError):
    """404 — no route matched the request."""

    status_code = 404
    code = "not_found"
