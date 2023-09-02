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

inst:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user --force-reinstall dist/*.whl
	brain-even

calc:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user --force-reinstall dist/*whl
	brain-calc
