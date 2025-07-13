test:
	uv run pytest ||  uv run allure serve

report:
	uv run allure serve

lint:
	uv run pylint *.py



