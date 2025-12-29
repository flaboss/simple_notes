# Variáveis para facilitar a manutenção
PYTHON = python3
VENV = venv
BIN = $(VENV)/bin

.PHONY: help install run lint format test setup build clean

help: ## Mostra os comandos disponíveis
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Cria o venv e instala dependências
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

run: ## Executa o aplicativo
	$(BIN)/python app/main.py

lint: ## Executa o linter 
	$(BIN)/ruff check .

format:
	$(BIN)/ruff format .

test: ## Executa testes unitários (Pytest)
	$(BIN)/pip install pytest
	$(BIN)/pytest tests/

setup: ## Instala dependências e prepara o ambiente
	$(BIN)/pip install -r requirements.txt
	@if [ ! -f .env ]; then \
		echo "FIREBASE_API_KEY=\"PASTE_YOUR_API_KEY_HERE\"" > .env; \
		echo "FIREBASE_DB_URL=\"PASTE_YOUR_DATABASE_URL_HERE\"" >> .env; \
	fi

build: ## Compila o app para macOS (PyInstaller)
	@echo "Limpando builds anteriores..."
	rm -rf build dist
	$(BIN)/python -m PyInstaller --clean --noconfirm MinhasNotas.spec
	@echo "Build concluído! Verifique a pasta dist/"

clean: ## Remove arquivos temporários
	## rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete
