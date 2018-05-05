.PHONY: all
all: backend frontend main

.PHONY: delete
delete: delete-backend delete-frontend delete-main

.PHONY: backend
backend:
	$(MAKE) -C backend all

.PHONY: frontend
frontend:
	$(MAKE) -C frontend all

.PHONY: main
main:
	$(MAKE) -C mainapp all

.PHONY: delete-backend
delete-redis:
	$(MAKE) -C backend delete

.PHONY: delete-frontend
delete-webapp:
	$(MAKE) -C frontend delete

.PHONY: delete-main
delete-worker:
	$(MAKE) -C main delete
