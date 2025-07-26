# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

**Setup (one-time):**
```bash
make setup
```

**Running tests:**
```bash
make test
```

**Running a single test:**
```bash
make test
```

**Code formatting and linting:**
```bash
make ruff
```

**Generate Allure report:**
```bash
make report
```

## Architecture Overview

This is a Python Playwright test automation framework for testing a dockerized web application using the Page Object Model pattern.

**Key Components:**
- **testcontainers**: Automatically spins up the Docker container (`yaroslavorelkh/test-me-tcm:0.1`) during test execution
- **Page Object Model**: Located in `pages/` directory with `base_page.py` as the foundation
- **Allure reporting**: Automatically captures screenshots and videos on test failure
- **Multi-browser testing**: Configured to run on WebKit, Chromium, and Firefox
- **Concurrent execution**: Supports parallel test execution via pytest-xdist

**Test Structure:**
- Tests are in `tests/` directory
- `conftest.py` contains pytest fixtures including container setup and page object fixtures
- `config.py` defines application container and port configuration
- `pytest.ini` configures Allure reporting and browser settings

**Page Objects:**
- All page classes inherit from `BasePage` which handles container URL construction
- Page objects receive both the Playwright `Page` object and the `DockerContainer` instance
- Use `_navigate_to()` method for internal navigation within the application

**Test Execution Flow:**
1. Container starts automatically via session-scoped fixture
2. Tests use page object fixtures that include the running container
3. On failure, screenshots/videos are automatically attached to Allure reports
4. Container is cleaned up after test session

**Dependencies:**
- Python 3.13+
- uv for dependency management
- Docker for application containers
- Allure for reporting
- ruff for code formatting and linting