default:
    @cat makefile
env:
    source env/bin/activate
    pip install -r requirements.txt

run:
    @python bin/clockdeco_param.py

< your code here so the following task ALWAYS gets called, even though the directory exists >

.PHONY: tests
tests:
    pytest -vv tests
