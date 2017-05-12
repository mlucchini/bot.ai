PYTHON=python2.7
PYTHONPATH=.
WITH_PYENV=. .env/bin/activate;

default: run

.env:
	#$(PYTHON) -m venv .env
	virtualenv -p $(PYTHON) .env

build: .env
	$(WITH_PYENV) pip install -r requirements.txt
	$(WITH_PYENV) pip install -e .

run: build
	$(WITH_PYENV) $(PYTHON) botai/main.py

test:
	python setup.py nosetests

clean:
	@rm -rf .env
