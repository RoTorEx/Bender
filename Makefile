.ONESHELL:
py := poetry run
python := $(py) python

package_dir := bot
tests_dir := tests

code_dir := $(package_dir) $(tests_dir)


define setup_env
    $(eval ENV_FILE := $(1))
    @echo " - setup env $(ENV_FILE)"
    $(eval include $(1))
    $(eval export)
endef


hello:
	@echo "Look for doc and entry correct argument."

clean:
	@find . -name \*__pycache__ -type d -exec rm -rf '{}' \;


.PHONY: migrate
migrate:
	docker-compose exec bot alembic revision --autogenerate
	docker-compose exec bot alembic upgrade head
	docker-compose exec bot alembic history

.PHONY: up
up:
	docker compose -f=docker-compose.yml --env-file=.env up -d --build

.PHONY: reup
reup:
	docker-compose down -v
	docker compose -f=docker-compose.yml --env-file=.env up -d --build

.PHONY: down
down:
	docker-compose down -v

.PHONY: log
log:
	docker-compose logs -f

