# virtualenv path
VENV_DIR       = .venv
VENV_PYTHON    = $(VENV_DIR)/bin/python3
VENV_TEST_DIR  = .venv_test
VENV_TEST_PYTHON = $(VENV_TEST_DIR)/bin/python3

# sphinx
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR      = src
BUILDDIR       = docs/_build

$(VENV_PYTHON):
ifneq ("$(wildcard $(VENV_PYTHON))","")
else
	python3 -m venv $(VENV_DIR)
endif

.PHONY: install
install: $(VENV_PYTHON) requirements.txt
	$(VENV_PYTHON) -m pip install -U setuptools>=64.0 pip wheel
	$(VENV_PYTHON) -m pip install -r requirements.txt
	$(VENV_PYTHON) -m pip install -e .

$(VENV_TEST_PYTHON):
ifneq ("$(wildcard $(VENV_TEST_PYTHON))","")
else
	python3 -m venv $(VENV_TEST_DIR)
endif

.PHONY: install-dev
install-dev: $(VENV_TEST_PYTHON)
	$(VENV_TEST_PYTHON) -m pip install -U pip setuptools wheel
	$(VENV_TEST_PYTHON) -m pip install -e .[test,lint]

$(VENV_DIR)/bin/$(SPHINXBUILD): $(VENV_PYTHON)
	$(VENV_PYTHON) -m pip install -U pip
	$(VENV_PYTHON) -m pip install -r docs-requirements.txt

.PHONY: lint
lint: install-dev
	$(VENV_TEST_PYTHON) -m flake8 src tests
	$(VENV_TEST_PYTHON) -m pylint src
	$(VENV_TEST_PYTHON) -m bandit -r src

.PHONY: test
test: install-dev
	$(VENV_TEST_PYTHON) -m coverage run --source=src -m pytest
	$(VENV_TEST_PYTHON) -m coverage report -m

.PHONY: docs
docs: $(VENV_DIR)/bin/$(SPHINXBUILD)
	cd docs && make html

.PHONY: clean
clean:
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.egg-info" -type d | xargs rm -rf
	@rm -rf build dist .pytest_cache .tox .coverage *.egg-info htmlcov
	@rm -rf $(VENV_DIR) $(VENV_TEST_DIR)
	cd docs && make clean
