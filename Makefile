install:
	pip install --upgrade pip && pip install -r requirements.txt
lint:
	# sintax flake8 or pylint
format:
	# format code
test:
	# test app
deploy:
	# deploy the proyect
all: install lint format test deploy	