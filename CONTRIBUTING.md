# Contributing

Thanks for your interest in improving Dynamic Geometry Animator! This document outlines the preferred workflow for contributing.

## Prerequisites
- Python 3.13 or newer
- [Poetry](https://python-poetry.org/) for dependency management

Install dependencies and activate the environment:

```powershell
poetry install
poetry shell
```

## Development Workflow
- Create a feature branch based on `main`.
- Keep changes focused; open separate pull requests for unrelated fixes.
- Update or add documentation whenever you introduce new features or behavioural changes.
- Add tests for new functionality when practical. Place fast, logic-only tests under `tests/`.
- Run Ruff and the test suite before opening a pull request:

```powershell
poetry run ruff check .
poetry run pytest
```

## Commit and Pull Request Guidelines
- Use clear, present-tense commit messages (e.g., "Add BetweenDot ratio helper").
- Reference related issues in your pull request description when applicable.
- Describe what changed and why, including any limitations or follow-up work.
- Ensure CI can run the Manim examples if they are part of your change; consider providing pre-rendered media when relevant.

## Questions and Support

Unsure about an idea or implementation detail? Open a discussion or draft pull request on GitHub so maintainers and contributors can help.
