.PHONY: all
all: backend frontend main

.PHONY: delete
delete: delete-backend delete-frontend delete-main

.PHONY: backend
redis:
	$(MAKE) -C backend all

.PHONY:  frontend
webapp:
	$(MAKE) -C frontend all

.PHONY: main
worker:
	$(MAKE) -C main all

.PHONY: delete-backend
delete-redis:
	$(MAKE) -C backend delete

.PHONY: delete-frontend
delete-webapp:
	$(MAKE) -C frontend delete

.PHONY: delete-main
delete-worker:
	$(MAKE) -C main delete
