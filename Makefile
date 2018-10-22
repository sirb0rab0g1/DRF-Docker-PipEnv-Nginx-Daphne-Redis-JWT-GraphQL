help: # This help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

local: ## Starts the api container for local development
	@echo "\033[92mStarting api container for local development...\033[0m"
	docker-compose up --build api

backend: ## Start the api and nginx container
	@echo "\033[92mStarting an environment for local development...\033[0m"
	docker-compose up --build nginx

up:
	@echo "\033[92mStarting api container for local development...\033[0m"
	docker-compose up

down:  ## Stop docker containers
	docker-compose down ${args}
