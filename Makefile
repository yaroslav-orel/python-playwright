test:
	pytest

lint:
	pylint *.py --disable=missing-docstring || true


