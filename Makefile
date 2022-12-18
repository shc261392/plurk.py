VENV_DIR=.venv
VENV_PYTHON=$(VENV_DIR)/bin/python3


$(VENV_PYTHON):
ifneq ("$(wildcard $(VENV_PYTHON))","")
else
	python3 -m venv $(VENV_DIR)
endif


.PHONY: install
install: $(VENV_PYTHON) requirements.txt
	$(VENV_PYTHON) -m pip install -r requirements.txt
	$(VENV_PYTHON) -m pip install -e .


$(VENV_DIR)/bin/tox: $(VENV_PYTHON)
	$(VENV_PYTHON) -m pip install tox


.PHONY: lint
lint: $(VENV_DIR)/bin/tox
	$(VENV_DIR)/bin/tox -e flake8,pylint,bandit


.PHONY: test
test: $(VENV_DIR)/bin/tox
	$(VENV_DIR)/bin/tox -e pytest,report


.PHONY: clean
clean:
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.egg-info" -type d | xargs rm -rf
	@rm -rf build dist .pytest_cache .tox .coverage *.egg-info htmlcov
	@rm -rf $(VENV_DIR)
