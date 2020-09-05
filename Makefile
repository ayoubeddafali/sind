.PHONY: default

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=src/ pytest

shell:
	pipenv shell --three

run:
	python main.py

image:
	docker build -t ${IMAGE_TAG} -f Dockerfile.chrome .
