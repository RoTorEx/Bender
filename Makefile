.ONESHELL:
py := poetry run
python := $(py) python
main_dir := bot

code_dir = $(main_dir)


hello:
	@echo "Look for doc and entry correct argument."

clean:
	@find . -name \*__pycache__ -type d -exec rm -rf '{}' \;


# Linters
.PHONY: lint
lint:
	@$(py) isort $(code_dir)
	@$(py) black $(code_dir)
	@$(py) flake8 $(code_dir)
	@$(py) mypy $(code_dir)


# Alembic & migrations
.PHONY: migrate
migrate:
	@docker compose exec bot alembic revision --autogenerate

.PHONY: apply
apply:
	@docker compose exec bot alembic upgrade head

.PHONY: downgrade
downgrade:
	@docker compose exec bot alembic downgrade -1

.PHONY: history
history:
	@docker compose exec bot alembic history


# Docker compose
.PHONY: up
up:
	@docker compose up -d --build

.PHONY: reup
reup:
	@docker compose down -v
	@docker compose up -d --build

.PHONY: down
down:
	@docker compose down -v

.PHONY: log
log:
	@docker compose logs -f

