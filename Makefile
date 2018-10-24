.PHONY: help run test install autorun

default: help

help: ## Show this help
	@echo "Cuboid Cryptids"
	@echo "======================"
	@echo
	@echo "Procjam 2018 project"
	@echo
	@fgrep -h " ## " $(MAKEFILE_LIST) | fgrep -v fgrep | sed -Ee 's/([a-z.]*):[^#]*##(.*)/\1##\2/' | column -t -s "##"

install: ## Install the app's dependencies
				pip3 install -r requirements.txt

run: ## Run app locally
				python3 app/main.py

autorun: ## Run app locally and restart when app files change
				bin/guard --path ./app/ --command make run

test: ## Run app's tests
				pytest
