.PHONY: run, create-env, install-requirements, set-env

run:
	@python3 binarytournament/main.py

create-env:
	@echo "Creating virtual environment..."
	@python3 -m venv .venv
	@echo "Virtual environment created."

set-env: create-env install-requirements
	@echo "Activating virtual environment..."
	@source .venv/bin/activate.fish 
	@echo "Virtual environment activated."

install-requirements:
	@echo "Installing requirements..."
	@pip3 install -r requirements.txt
	@echo "Requirements installed."
