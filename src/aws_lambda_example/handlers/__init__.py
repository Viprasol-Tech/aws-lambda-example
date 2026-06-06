"""Lambda handler entry points.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

from aws_lambda_example.handlers.api_gateway import handler as api_gateway_handler
from aws_lambda_example.handlers.s3_event import handler as s3_event_handler
from aws_lambda_example.handlers.scheduled import handler as scheduled_handler
from aws_lambda_example.handlers.sqs import handler as sqs_handler

__all__ = [
    "api_gateway_handler",
    "s3_event_handler",
    "scheduled_handler",
    "sqs_handler",
]
