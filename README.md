<p align="center"><img src="docs/assets/logo.png" width="120"></p>

# AWS Lambda Example

> Practical AWS Lambda handler patterns — API Gateway, SQS, S3, and EventBridge — with a tiny router, middleware, response helpers, and an offline local-invoke harness.

*Built and maintained by [Viprasol Tech](https://viprasol.com) — Fintech Experts. Full-Stack Builders.*

![CI](https://img.shields.io/github/actions/workflow/status/Viprasol-Tech/aws-lambda-example/ci.yml?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue?style=flat-square)
![Ruff](https://img.shields.io/badge/lint-ruff-261230?style=flat-square)
![Telegram](https://img.shields.io/badge/Telegram-viprasol__help-26A5E4?style=flat-square)
![Stars](https://img.shields.io/github/stars/Viprasol-Tech/aws-lambda-example?style=flat-square)

Production-grade scaffolding for the four Lambda event sources you actually ship, plus the glue that makes handlers clean, testable, and observable — all runnable on your laptop with zero AWS access.

## ✨ Features

- 🌐 **API Gateway proxy handler** with a dependency-free router.
- 📨 **SQS handler** with proper partial-batch-failure (`batchItemFailures`) reporting.
- 🪣 **S3 event handler** that URL-decodes object keys correctly.
- ⏰ **Scheduled (EventBridge) handler** for cron-style invocations.
- 🧩 **Tiny router + middleware** — logging, error-to-response, and JSON body parsing.
- 📦 **Response helpers** for consistent JSON and error payloads.
- 🧪 **Offline local-invoke harness** that feeds fixture events to any handler.
- 🔌 **Lazy, optional boto3** — installs and tests run fully offline.
- ✅ **18 offline tests**, strict typing, and a green CI matrix.
- 🛡️ **MIT licensed** and ready to drop into your serverless project.

## 🚀 Quickstart

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

Invoke a handler locally with a sample event (no AWS required):

```bash
lambda-invoke api_gateway examples/api_gateway_event.json
lambda-invoke sqs examples/sqs_event.json
```

## 🧑‍💻 Usage

```python
from aws_lambda_example import Router, json_response

router = Router()


@router.route("GET", "/health")
def health(event, context):
    return json_response({"status": "ok"})


def handler(event, context):
    return router.handle(event, context)
```

The router applies JSON parsing, logging, and error-to-response middleware
automatically, so domain errors become clean HTTP responses.

## 🗺️ Roadmap

- [x] Four core handlers (API Gateway, SQS, S3, EventBridge)
- [x] Router + middleware and response helpers
- [x] Offline local-invoke harness
- [ ] WebSocket API Gateway handler
- [ ] Powertools-style metrics emitter
- [ ] SAM/Terraform deployment examples

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and our
[Code of Conduct](CODE_OF_CONDUCT.md) before opening a pull request.

## 📬 Contact — Viprasol Tech Private Limited

- 🌐 Website: [viprasol.com](https://viprasol.com)
- ✉️ Email: [support@viprasol.com](mailto:support@viprasol.com)
- 💬 Telegram: [t.me/viprasol_help](https://t.me/viprasol_help) · 📱 WhatsApp: +91 96336 52112
- 🐙 GitHub: [@Viprasol-Tech](https://github.com/Viprasol-Tech) · 💼 [LinkedIn](https://www.linkedin.com/in/viprasol/) · 𝕏 [@viprasol](https://twitter.com/viprasol)

> *Viprasol Tech — fintech software, algorithmic trading systems, MT4/MT5 bots, AI voice agents, and B2B SaaS. Need a custom build? [Get in touch](mailto:support@viprasol.com).*

## 📄 License

Released under the [MIT License](LICENSE) © 2025 Viprasol Tech Private Limited.
