.PHONY: all
all: setup backend frontend mainapp

.PHONY: delete
delete: delete-backend delete-frontend delete-mainapp delete-setup

.PHONY: setup
setup:
	gcloud config set compute/zone us-east1-b
	gcloud container clusters create yelplabel --num-nodes 2 --scopes cloud-platform
	gcloud container clusters get-credentials yelplabel

.PHONY: backend
backend:
	$(MAKE) -C backend all

.PHONY: frontend
frontend:
	$(MAKE) -C frontend all

.PHONY: mainapp
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

.PHONY: delete-setup
delete-setup:
	gcloud container clusters delete yelplabel
