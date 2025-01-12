build:
	docker compose build
run:
	docker compose --env-file .env up
down:
	docker compose down
down-v:
	docker compose down -v
migrate:
	docker compose exec app python manage.py showmigrations
	docker compose exec app python manage.py makemigrations
	docker compose exec app python manage.py migrate