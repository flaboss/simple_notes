# Variáveis para facilitar a manutenção
PYTHON = python3
VENV = venv
BIN = $(VENV)/bin

.PHONY: help install run lint test clean

help: ## Mostra os comandos disponíveis
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Cria o venv e instala dependências
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

run: ## Executa o aplicativo
	$(BIN)/python main.py

lint: ## Executa o linter 
	$(BIN)/ruff check .

format:
	$(BIN)/ruff format .

test: ## Executa testes unitários (Pytest)
	$(BIN)/pip install pytest
	$(BIN)/pytest tests/

clean: ## Remove arquivos temporários
	## rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete
