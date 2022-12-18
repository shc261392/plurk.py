VENV_DIR := venv
ifeq ($(OS),Windows_NT)
    BIN_DIR := $(VENV_DIR)/Scripts
	VENV_PYTHON := $(BIN_DIR)/python
else
    BIN_DIR := $(VENV_DIR)/bin
	VENV_PYTHON := $(BIN_DIR)/python3
endif


$(VENV_PYTHON):
ifneq ("$(wildcard $(VENV_PYTHON))","")
else
	python3 -m venv $(VENV_DIR)
endif


.PHONY: install
install: $(VENV_PYTHON) requirements.txt
	$(VENV_PYTHON) -m pip install -r requirements.txt
	$(VENV_PYTHON) -m pip install -e .


$(BIN_DIR)/tox: $(VENV_PYTHON)
	$(VENV_PYTHON) -m pip install tox


.PHONY: lint
lint: $(BIN_DIR)/tox
	$(BIN_DIR)/tox -e flake8,pylint,bandit


.PHONY: test
test: $(BIN_DIR)/tox
	$(BIN_DIR)/tox -e pytest,report


.PHONY: clean
clean:
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.egg-info" -type d | xargs rm -rf
	@rm -rf build dist .pytest_cache .tox .coverage *.egg-info htmlcov
	@rm -rf $(VENV_DIR)
