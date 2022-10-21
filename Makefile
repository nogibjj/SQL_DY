install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv *.py dblib

format:	
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib

all: install lint test