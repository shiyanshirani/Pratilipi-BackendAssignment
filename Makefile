build-user-service:
	python3 user_service/manage.py makemigrations
	python3 user_service/manage.py migrate
	docker build -t user_service -f user_service/Dockerfile .

build-user-interaction-service:
	python3 user_interaction_service/manage.py makemigrations
	python3 user_interaction_service/manage.py migrate
	docker build -t user_interaction_service -f user_interaction_service/Dockerfile .

build-content-service:
	python3 content_service/manage.py makemigrations
	python3 content_service/manage.py migrate
	docker build -t content_service -f content_service/Dockerfile .


build: build-user-service build-user-interaction-service build-content-service

up:
	docker-compose up

down:
	docker-compose down
	
