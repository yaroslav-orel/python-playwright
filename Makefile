setup:
	uv run playwright install
	uv run playwright install-deps

test:
	uv run pytest

report:
	allure serve

lint:
	uv run pylint *.py



