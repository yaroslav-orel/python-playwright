RESULTS_DIR=allure-results

test:
	rm -rf $(RESULTS_DIR)
	pytest --alluredir $(RESULTS_DIR) || allure serve $(RESULTS_DIR)

report:
	allure serve $(RESULTS_DIR)

lint:
	pylint *.py



