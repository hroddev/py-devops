install:
	pip install --upgrade pip && pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py mylib/*.py
format:
	black *.py mylib/*.py
test:
	# test app
build:
	# build the container
deploy:
	# deploy the proyect
all: install lint format test deploy	