# python-playwright

## Motivation
Get familiar with Playwright for Python.

## Requirements
- Docker

## Setup
```
curl -LsSf https://astral.sh/uv/install.sh | sh      # Install uv
uv venv --python 3.13                                # Create a virtual environment
uv sync                                              # Install dependencies
uvx playwright install                               # Install Playwright browsers
```

## Running the tests
```
make test
```
## Generating the report
In case of test failure, report will be generated and served automatically, but you can also generate it manually by running:
```
make report
```
## Linting
Before commiting code, you should run the linter to ensure code quality:
```
make lint
```
