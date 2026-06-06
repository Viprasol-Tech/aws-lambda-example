# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-01-01

### Added

- API Gateway proxy handler with a tiny dependency-free router.
- Router middleware: logging, error-to-response, and JSON body parsing.
- SQS handler with partial-batch-failure (`batchItemFailures`) reporting.
- S3 event handler with correct URL-decoding of object keys.
- Scheduled (EventBridge) handler.
- JSON response and error response helpers.
- Offline local-invoke harness (`lambda-invoke`) with sample fixture events.
- 18 offline tests, strict mypy typing, ruff lint/format, and CI matrix.
