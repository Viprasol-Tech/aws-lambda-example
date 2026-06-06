"""Scheduled (EventBridge) handler.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

from typing import Any

from aws_lambda_example.logging_config import get_logger
from aws_lambda_example.types import LambdaContext, LambdaEvent

_log = get_logger(__name__)


def handler(event: LambdaEvent, context: LambdaContext = None) -> dict[str, Any]:
    """Lambda entry point for EventBridge scheduled rules."""
    detail_type = event.get("detail-type", "Scheduled Event")
    source = event.get("source", "aws.events")
    scheduled_at = event.get("time", "")
    _log.info("scheduled tick source=%s detail-type=%s time=%s", source, detail_type, scheduled_at)
    return {
        "ran": True,
        "source": source,
        "detail_type": detail_type,
        "scheduled_at": scheduled_at,
    }
