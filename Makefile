build-user-service:
	docker build -t user_service -f user_service/Dockerfile .

build-user-interaction-service:
	docker build -t user_interaction_service -f user_interaction_service/Dockerfile .

build-content-service:
	docker build -t content_service -f content_service/Dockerfile .


build: build-user-service build-user-interaction-service build-content-service

up:
	docker-compose up

down:
	docker-compose down
