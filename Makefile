install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*whl
lint:
	uv run ruff check VD_games
format:
	uv run ruff check --fix VD_games
	uv run ruff format VD_games

publish:
	twine upload dist/*

clean:
	rm -rf dist/ build/ *.egg-info

test:
	python -m pytest

all: clean install build
