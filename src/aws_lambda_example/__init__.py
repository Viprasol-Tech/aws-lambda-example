"""AWS Lambda Example — practical handler patterns.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

from aws_lambda_example.responses import error_response, json_response
from aws_lambda_example.router import Router

__all__ = ["Router", "__version__", "error_response", "json_response"]

__version__ = "0.1.0"
