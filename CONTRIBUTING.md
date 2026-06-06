# Contributing

Thanks for your interest in improving **AWS Lambda Example** by
[Viprasol Tech](https://viprasol.com)!

## Development setup

```bash
python -m pip install -e ".[dev]"
```

## Checks

Before opening a pull request, make sure all checks pass locally:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src
python -m pytest
```

## Guidelines

- Keep handlers dependency-free; any `boto3` usage must stay lazy and optional.
- Add or update offline tests for any behavior change.
- Follow conventional, descriptive commit messages.
- Be respectful — see our [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting issues

Use the GitHub issue templates for bugs and feature requests. For security
matters, please follow [SECURITY.md](SECURITY.md) instead of opening a public issue.
