PHONY: test
test:
	@echo 'tests started...'
	@pytest . -v


PHONY: check
check: test
	echo 'code linters started...'
	black .
	isort .
	flake8 .