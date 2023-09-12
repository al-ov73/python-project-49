brain-games:
	poetry run brain-games

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games


game-install:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user --force-reinstall dist/*.whl

even:
	brain-even

calc:
	brain-calc

gcd:
	brain-gcd

progression:
	brain-progression

prime:
	brain-prime
