.PHONY: build up down restart logs lint format test clean play

# Build the Docker image
build:
	docker compose build

# Play the game interactively
play:
	@echo "=========================================="
	@echo "Connect4 Game"
	@echo "=========================================="
	@echo ""
	@echo "Board visualization will be saved to:"
	@echo "  $(PWD)/board.html"
	@echo ""
	@echo "Open it in your browser with:"
	@echo "  file://$(PWD)/board.html"
	@echo ""
	@echo "The page will auto-refresh every second."
	@echo "Starting game..."
	@echo ""
	@docker compose run --rm app python -m src.main


# View logs
logs:
	docker compose logs -f

# Run ruff linter and mypy type checker
lint:
	docker compose run --rm app ruff check src tests
	docker compose run --rm app mypy src

# Run ruff formatter
format:
	docker compose run --rm app ruff format src tests

# Run tests
test:
	docker compose run --rm app python -m pytest tests

# Clean up containers, images, and volumes
clean:
	docker compose down -v --rmi all
