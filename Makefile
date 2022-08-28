entrypoint:
	@echo "Look for doc and entry correct argument."

clean:
	@find . -name \*__pycache__ -type d -exec rm -rf '{}' \;

run:
	@poetry run python -m bot

up:
	@docker-compose up -d --build

down:
	@docker-compose down -v

reup: down up

log:
	@docker-compose logs -f