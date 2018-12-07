.PHONY: all
all: setup broker frontend backend

.PHONY: delete
delete: delete-backend delete-frontend delete-broker delete-setup

.PHONY: setup
setup:
	gcloud config set compute/zone us-east1-b
	gcloud container clusters create yelplabel --num-nodes 2 --scopes cloud-platform
	gcloud container clusters get-credentials yelplabel

.PHONY: broker
broker:
	$(MAKE) -C broker all

.PHONY: frontend
frontend:
	$(MAKE) -C frontend all

.PHONY: backend
backend:
	$(MAKE) -C backend all

.PHONY: delete-backend
delete-backend:
	$(MAKE) -C backend delete

.PHONY: delete-frontend
delete-frontend:
	$(MAKE) -C frontend delete

.PHONY: delete-broker
delete-broker:
	$(MAKE) -C broker delete

.PHONY: delete-setup
delete-setup:
	gcloud container clusters delete yelplabel
