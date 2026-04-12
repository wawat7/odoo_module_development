DOCKER = docker
DOCKER_COMPOSE = $(DOCKER) compose
DB_USER = odoo
DB_NAME = odoo_development
CONTAINER_APP = odoo
CONTAINER_DB = odoo-postgres


help:
	@echo "Usage: make <command>"
	@echo "Commands:"
	@echo "  up: Start the containers"
	@echo "  down: Stop the containers"
	@echo "  restart-app: Restart the app container"
	@echo "  restart-db: Restart the db container"
	@echo "  logs-app: Show the app logs"
	@echo "  logs-db: Show the db logs"
	@echo "  bash-app: Bash into the app container"
	@echo "  bash-db: Bash into the db container"
	@echo "  psql: Psql into the db container"

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

restart-app:
	$(DOCKER) restart $(CONTAINER_APP)

restart-db:
	$(DOCKER) restart $(CONTAINER_DB)

logs-app:
	$(DOCKER) logs -f $(CONTAINER_APP)

logs-db:
	$(DOCKER) logs -f $(CONTAINER_DB)

bash-app:
	$(DOCKER) exec -it $(CONTAINER_APP) bash

bash-db:
	$(DOCKER) exec -it $(CONTAINER_DB) bash

psql:
	$(DOCKER) exec -it $(CONTAINER_DB) psql -U $(DB_USER) -d $(DB_NAME)

.PHONY: up down restart-app restart-db logs-app logs-db bash-app bash-db psql