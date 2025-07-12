test:
	pytest --alluredir allure-results || true
	allure serve allure-results

lint:
	pylint *.py --disable=missing-docstring || true


