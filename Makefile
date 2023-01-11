# virtualenv path
VENV_DIR       = .venv
VENV_PYTHON    = $(VENV_DIR)/bin/python3

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
	$(VENV_PYTHON) -m pip install -r requirements.txt
	$(VENV_PYTHON) -m pip install -e .

$(VENV_DIR)/bin/tox: $(VENV_PYTHON)
	$(VENV_PYTHON) -m pip install tox

$(VENV_DIR)/bin/$(SPHINXBUILD): $(VENV_PYTHON)
	$(VENV_PYTHON) -m pip install sphinx

.PHONY: lint
lint: $(VENV_DIR)/bin/tox
	$(VENV_DIR)/bin/tox -e flake8,pylint,bandit

.PHONY: test
test: $(VENV_DIR)/bin/tox
	$(VENV_DIR)/bin/tox -e pytest,report

.PHONY: docs
docs: $(VENV_DIR)/bin/$(SPHINXBUILD)
	cd docs && make html

.PHONY: clean
clean:
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.egg-info" -type d | xargs rm -rf
	@rm -rf build dist .pytest_cache .tox .coverage *.egg-info htmlcov
	@rm -rf $(VENV_DIR)
	cd docs && make clean
