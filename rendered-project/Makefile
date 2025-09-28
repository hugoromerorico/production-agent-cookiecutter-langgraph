IMAGE_NAME ?= rendered-project

.PHONY: dev api-dev run docker-build docker-run

dev:
	uv run langgraph dev

api-dev:
	uv run fastapi dev app/main.py

run:
	uv run -m app.main

docker-build:
	docker build \
		-t $(IMAGE_NAME):latest .

docker-run: docker-build

	docker run \
		--rm \
		-p 8080:8080 \
		-e ENVIRONMENT=docker \
		--env-file=${PWD}/.env \
		$(IMAGE_NAME):latest \
