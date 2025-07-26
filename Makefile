setup:
	uv run playwright install
	uv run playwright install-deps

test:
	uv run pytest

report:
	allure serve

ruff:
    uv run ruff format
	uv run ruff check --fix



