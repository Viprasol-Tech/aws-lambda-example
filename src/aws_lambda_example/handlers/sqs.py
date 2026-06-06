"""SQS handler with partial-batch-failure reporting.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

import json
from typing import Any

from aws_lambda_example.logging_config import get_logger
from aws_lambda_example.types import LambdaContext, LambdaEvent

_log = get_logger(__name__)


def process_record(record: dict[str, Any]) -> None:
    """Process a single SQS record.

    Raises on a malformed body so the message can be retried via the
    partial-batch-failure mechanism.
    """
    body = record.get("body", "")
    try:
        payload = json.loads(body) if body else {}
    except json.JSONDecodeError as exc:
        raise ValueError(f"record {record.get('messageId')} has invalid JSON body") from exc
    _log.info("processed message %s payload=%s", record.get("messageId"), payload)


def handler(event: LambdaEvent, context: LambdaContext = None) -> dict[str, Any]:
    """Lambda entry point for SQS; returns ``batchItemFailures``."""
    failures: list[dict[str, str]] = []
    for record in event.get("Records", []):
        try:
            process_record(record)
        except Exception as exc:
            message_id = str(record.get("messageId", ""))
            _log.warning("failed record %s: %s", message_id, exc)
            failures.append({"itemIdentifier": message_id})
    return {"batchItemFailures": failures}
