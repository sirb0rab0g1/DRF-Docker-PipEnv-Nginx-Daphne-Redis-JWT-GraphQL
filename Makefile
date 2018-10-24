help: # This help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

local: ## Starts the api container for local development
	@echo "\033[92mStarting api container for local development...\033[0m"
	docker-compose up --build api

backend: ## Start the api and nginx container
	@echo "\033[92mStarting an environment for local development...\033[0m"
	docker-compose up --build nginx

migrations: # ex. make migrations name=name_to_commit
	@echo "\033[92mMaking Migrations with a name of $(name) ...\033[0m"
	docker-compose run api python manage.py makemigrations --name $(name)

migrate:
	@echo "\033[92mStart Migrating...\033[0m"
	docker-compose run api python manage.py migrate

superuser:
	@echo "\033[92mCreating Super User...\033[0m"
	docker-compose run api python manage.py createsuperuser

install: #ex. make install name=name_of_package
	@echo "\033[92mInstalling Pakcage $(name)...\033[0m"
	pipenv install $(name)

uninstall:
	@echo "\033[92mUninstalling Pakcage $(name)...\033[0m"
	pipenv uninstall $(name)

up:
	@echo "\033[92mStarting api container for local development...\033[0m"
	docker-compose up

down:  ## Stop docker containers
	docker-compose down ${args}
