PYTHON:=PYTHONPATH=./src python

run:
	$(PYTHON) -m src.app

init-db:
	$(PYTHON) -m bin.init_data
