SRCPATH := $(shell pwd)
PROJECTNAME := $(shell basename $CURDIR)

define HELP
Manage $(PROJECTNAME). Usage:

make run        - Run $(PROJECTNAME).
make deploy     - Pull latest build and deploy to production.
make update     - Update pip dependencies via Python Poetry.
make format     - Format code with Python's `Black` library.
make lint       - Check code formatting with flake8
make clean      - Remove cached files and lock files.
endef
export HELP


.PHONY: run restart deploy update format lint clean help

requirements: .requirements.txt
env: ./.venv/bin/activate


.requirements.txt: requirements.txt
	$(shell . .venv/bin/activate && pip install -r requirements.txt)


all help:
	@echo "$$HELP"


.PHONY: run
run: env
	python main.py


.PHONY: deploy
deploy:
	$(shell . ./deploy.sh)


.PHONY: update
update: env
	.venv/bin/python3 -m pip install --upgrade pip setuptools wheel
	poetry update
	poetry export -f requirements.txt --output requirements.txt --without-hashes


.PHONY: format
format: env
	isort -rc --multi-line=3 .
	black .


.PHONY: lint
lint:
	flake8 . --count \
			--select=E9,F63,F7,F82 \
			--exclude .git,.github,__pycache__,.pytest_cache,.venv,logs,creds,.venv,docs,logs \
			--show-source \
			--statistics


.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name 'poetry.lock' -delete
	find . -name 'Pipefile.lock' -delete
	find . -name '*.log' -delete
	find . -wholename 'logs/*.json' -delete
	find . -wholename '.pytest_cache' -delete
	find . -wholename '*/.pytest_cache' -delete
	find . -wholename '*/logs/*.json' -delete
	find . -wholename '.webassets-cache/*' -delete