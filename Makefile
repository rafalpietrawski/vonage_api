SHELL := bash

export PYTHONPATH=.

.DEFAULT_GOAL = help

.PHONY: help
help:	## This menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: venv-create
venv-create:	## Create venv
	@python -m venv venv

.PHONY: venv-activate
venv-activate:	## Activate venv
	@source venv/bin/activate

.PHONY: venv-delete
venv-delete:	## Delete venv
	 rm -rf venv

 .PHONY: requirements.txt
requirements.txt:	## Compile requirements.txt
	@pip-compile requirements.in

.PHONY: setup
setup:	## Install project dependencies from requirements.txt
	@pip install -r ./requirements.txt

.PHONY: run
run: ## Run Script
	@python3 main.py
