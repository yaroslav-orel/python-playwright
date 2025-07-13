# python-playwright

## Description
This repository contains a set of tests written in Python for a dockerized application.
Main features:
- Dependency and virtual environment management via `uv`
- Application deployment during test execution via `testcontainers` 
- Reports by `Allure` with screenshots and videos on failure
- Concurrent test execution support

## Requirements
- docker
- allure
- make
- uv

## Setup [one-time]
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
