export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

style:
	flake8 .
	ruff check .
	ruff format .

db:
	docker-compose up -d db

tests:
	python3 -m pytest .

check:
	make style db tests
