SRC_PORT := 4600
DST_PORT := 8000

##### docker
IMAGE_NAME := {{ cookiecutter.project_slug }}
CONTAINER_NAME := ${IMAGE_NAME}-container

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
	mypy ./{{ cookiecutter.project_slug }} 

lint:
	@echo check style
	flake8 --show-source --statistics

test:
	@echo testing
	pytest -rf --cov=./{{ cookiecutter.project_slug }} 


##### k8s
MANIFEST_PATH = $(shell pwd)/k8s
ENVIRONMENT := local

deploy:
	kubectl apply -k ${MANIFEST_PATH}/overlays/${ENVIRONMENT}/

# TODO: prevent operation mistaken
destory:
	kubectl delete -k ${MANIFEST_PATH}/overlays/${ENVIRONMENT}/

port-forward:
	kubectl port-forward service/{{ cookiecutter.project_slug | kebabcase }}-service ${SRC_PORT}:${DST_PORT}

##### application
launch:
	uvicorn app:app --host 0.0.0.0 --port ${DST_PORT}

launch-develop:
	python app.py
