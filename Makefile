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

dev-env:
	docker run -d --name test-app -p 8000:8000 yaroslavorelkh/test-me-tcm:0.1

dev-env-stop:
	docker stop test-app && docker rm test-app



