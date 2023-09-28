default:
	@cat makefile
env:
	pip install -r requirements.txt
	source env/bin/activate

run:
	@python bin/clockdeco_param.py
.PHONY: tests
tests:
	pytest -vv tests
