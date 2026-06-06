"""Local-invoke harness — feed sample/fixture events to handlers offline.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).

Usage:
    lambda-invoke api_gateway examples/api_gateway_event.json
    python -m aws_lambda_example.harness sqs examples/sqs_event.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable
from enum import StrEnum
from pathlib import Path
from typing import Any

from aws_lambda_example.handlers import (
    api_gateway_handler,
    s3_event_handler,
    scheduled_handler,
    sqs_handler,
)
from aws_lambda_example.types import LambdaContext, LambdaEvent

Handler = Callable[[LambdaEvent, LambdaContext], Any]


class HandlerName(StrEnum):
    """Names selectable on the harness command line."""

    API_GATEWAY = "api_gateway"
    SQS = "sqs"
    S3 = "s3"
    SCHEDULED = "scheduled"


HANDLERS: dict[HandlerName, Handler] = {
    HandlerName.API_GATEWAY: api_gateway_handler,
    HandlerName.SQS: sqs_handler,
    HandlerName.S3: s3_event_handler,
    HandlerName.SCHEDULED: scheduled_handler,
}


def load_event(path: str | Path) -> LambdaEvent:
    """Load a JSON event fixture from disk."""
    data: LambdaEvent = json.loads(Path(path).read_text(encoding="utf-8"))
    return data


def invoke(name: HandlerName, event: LambdaEvent) -> Any:
    """Invoke a named handler with the given event (no AWS calls)."""
    return HANDLERS[name](event, None)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for the local-invoke harness."""
    parser = argparse.ArgumentParser(description="Invoke a Lambda handler with a fixture event.")
    parser.add_argument("handler", choices=[h.value for h in HandlerName], help="handler to run")
    parser.add_argument("event", help="path to a JSON event fixture")
    args = parser.parse_args(argv)

    name = HandlerName(args.handler)
    event = load_event(args.event)
    result = invoke(name, event)
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
