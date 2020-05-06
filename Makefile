
##### docker
IMAGE_NAME := python-api-template
CONTAINER_NAME := ${IMAGE_NAME}-container
SRC_PORT := 4600
DST_PORT := 9876

build-image:
	docker build -t ${IMAGE_NAME} ./

run-container:
	docker run -it -d \
		--name ${CONTAINER_NAME} \
		-p ${SRC_PORT}:${DST_PORT} \
		${IMAGE_NAME}

##### ci
ci: typecheck test lint

typecheck:
	@echo check types
	mypy ./python_api_template

lint:
	@echo check style
	flake8 --show-source --statistics

test:
	@echo testing
	pytest -rf --cov=./python_api_template


##### application
GUNICORN_CONFIG_PATH := config/gunicorn.py

launch:
	gunicorn app:app -c ${GUNICORN_CONFIG_PATH}

launch-develop:
	python app.py
