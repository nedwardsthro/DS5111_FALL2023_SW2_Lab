default:
	@cat makefile
env:
	pip install -r requirements.txt
	source env/bin/activate

run:
	source env/bin/activate
	@python bin/clockdeco_param.py
.PHONY: tests
tests:
	pytest -vv tests

lint:
	pylint bin/perceptron.py
