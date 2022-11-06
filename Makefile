install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv *.py 

format:	
	black *.py *.ipynb

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py 

all: install lint test