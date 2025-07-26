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
```
make report
```

## Linting & Formatting
```
make ruff
```
