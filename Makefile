build-user-service:
	docker build -t user_service -f user_service/Dockerfile .
	python3 user_service/manage.py makemigrations
	python3 user_service/manage.py migrate

build-user-interaction-service:
	docker build -t user_interaction_service -f user_interaction_service/Dockerfile .
	python3 user_interaction_service/manage.py makemigrations
	python3 user_interaction_service/manage.py migrate

build-content-service:
	docker build -t content_service -f content_service/Dockerfile .
	python3 content_service/manage.py makemigrations
	python3 content_service/manage.py migrate


build: build-user-service build-user-interaction-service build-content-service

up:
	docker-compose up

down:
	docker-compose down
	
