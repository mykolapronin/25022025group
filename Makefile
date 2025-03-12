PHONY: test
test:
	@echo 'tests started...'
	@set PYTHONPATH=. && python -m pytest . -v


PHONY: check
check: test
	echo 'code linters started...'
	black .
	isort .
	flake8 .