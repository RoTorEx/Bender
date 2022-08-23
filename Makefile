entrypoint:
	@echo "Available only 'run' and 'run-up' methods."

clean:
	@find . -name \*__pycache__ -type d -exec rm -rf '{}' \;

start:
	@poetry run python -m bot

up:
	@docker-compose up -d --build

down:
	@docker-compose down -v

reup: down up
