"""Minimal structured-ish logging setup for Lambda.

Part of AWS Lambda Example by Viprasol Tech Private Limited (https://viprasol.com).
"""

from __future__ import annotations

import logging
import os


def get_logger(name: str = "aws_lambda_example") -> logging.Logger:
    """Return a configured logger.

    Lambda's runtime pre-configures the root logger; here we just ensure a
    sensible level and a handler when running locally (offline harness/tests).
    """
    logger = logging.getLogger(name)
    level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logger.setLevel(level)
    if not logging.getLogger().handlers and not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
        logger.addHandler(handler)
    return logger
