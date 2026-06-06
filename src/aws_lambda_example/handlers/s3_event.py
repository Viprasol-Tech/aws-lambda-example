"""S3 event handler.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).

Demonstrates *lazy, optional* boto3 usage: the client is only imported and
constructed inside :func:`fetch_object`, which the offline tests never call.
"""

from __future__ import annotations

from typing import Any
from urllib.parse import unquote_plus

from aws_lambda_example.logging_config import get_logger
from aws_lambda_example.types import LambdaContext, LambdaEvent

_log = get_logger(__name__)


def extract_objects(event: LambdaEvent) -> list[dict[str, str]]:
    """Pull (bucket, key) pairs out of an S3 notification event."""
    objects: list[dict[str, str]] = []
    for record in event.get("Records", []):
        s3 = record.get("s3", {})
        bucket = s3.get("bucket", {}).get("name", "")
        raw_key = s3.get("object", {}).get("key", "")
        objects.append({"bucket": bucket, "key": unquote_plus(raw_key)})
    return objects


def fetch_object(bucket: str, key: str) -> bytes:
    """Fetch an object's bytes from S3 (requires the optional ``aws`` extra).

    boto3 is imported lazily so the package installs and tests run offline.
    """
    import boto3

    client = boto3.client("s3")
    response: dict[str, Any] = client.get_object(Bucket=bucket, Key=key)
    body: bytes = response["Body"].read()
    return body


def handler(event: LambdaEvent, context: LambdaContext = None) -> dict[str, Any]:
    """Lambda entry point for S3 events; returns a summary of objects seen."""
    objects = extract_objects(event)
    for obj in objects:
        _log.info("s3 object created s3://%s/%s", obj["bucket"], obj["key"])
    return {"processed": len(objects), "objects": objects}
