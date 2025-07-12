RESULTS_DIR=allure-results

test:
	pytest --alluredir $(RESULTS_DIR) --clean-alluredir || allure serve $(RESULTS_DIR)

report:
	allure serve $(RESULTS_DIR)

lint:
	pylint *.py



