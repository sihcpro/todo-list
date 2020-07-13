PYTHON:=PYTHONPATH=./src python
PYTEST:=PYTHONPATH=./src:./test pytest -v

run:
	$(PYTHON) -m src.app

init-db:
	$(PYTHON) -m bin.init_data

run-test:
	$(PYTEST) ./test/**/*.py
