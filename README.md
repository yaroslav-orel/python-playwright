# python-playwright

## Motivation
Get familiar with Playwright for Python.

## Requirements
- docker
- allure
- make
- uv

## Setup
```
make setup
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
