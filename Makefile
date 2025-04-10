# 🛰️ ZEBES Makefile — Developer Operations

PROJECT_NAME=zebes
MODULE=app
DEPS_IN=requirements.in
DEPS_OUT=requirements.txt
VENV_PATH=./venv/Scripts

.PHONY: help install run dev docker docker-build lint format check-deps clean

help:
	@echo ""
	@echo "🧪 Makefile for ZEBES development"
	@echo "Available targets:"
	@echo "  install         Install dependencies from requirements.txt"
	@echo "  deps            Compile requirements.txt from requirements.in"
	@echo "  run             Run the FastAPI app with uvicorn (reload enabled)"
	@echo "  dev             Same as run"
	@echo "  docker          Run the project using docker-compose"
	@echo "  docker-build    Build the Docker image and run it"
	@echo "  lint            Run flake8, mypy and pylint"
	@echo "  format          Format code using black"
	@echo "  check-deps      Check if pip-tools and other tools are installed"
	@echo "  clean           Remove __pycache__ and *.pyc files"
	@echo ""

install:
	$(VENV_PATH)/pip install -r $(DEPS_OUT)

deps:
	$(VENV_PATH)/pip-compile $(DEPS_IN) --output-file=$(DEPS_OUT)

run:
	$(VENV_PATH)/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev: run

docker:
	docker-compose up

docker-build:
	docker-compose up --build

lint:
	$(VENV_PATH)/flake8 $(MODULE) --max-line-length=88
	$(VENV_PATH)/mypy $(MODULE) --strict
	$(VENV_PATH)/pylint $(MODULE)

format:
	$(VENV_PATH)/black $(MODULE)

check-deps:
	$(VENV_PATH)/pip show pip-tools black flake8 mypy pylint || echo "Some tools are missing."

clean:
	del /S /Q *.pyc 2>nul || true
	del /S /Q *.pyo 2>nul || true
	del /S /Q __pycache__ 2>nul || true
