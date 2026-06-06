"""Shared type aliases for Lambda event/response shapes.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

from typing import Any

# A Lambda event is, at the wire level, just JSON-decoded data.
LambdaEvent = dict[str, Any]

# The Lambda context object is opaque; we only ever read attributes off it,
# so a permissive alias keeps handlers honest without inventing a fake shape.
LambdaContext = Any

# API Gateway proxy integration response shape.
ProxyResponse = dict[str, Any]
