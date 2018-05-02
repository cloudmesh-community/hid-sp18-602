GCLOUD_PROJECT:=$(shell gcloud config list project --format="value(core.project)")

.PHONY: all
all: deploy

.PHONY: build
build:
	docker build -t gcr.io/$(GCLOUD_PROJECT)/yelplabel-mainapp .

.PHONY: push
push: build
	gcloud docker -- push gcr.io/$(GCLOUD_PROJECT)/yelplabel-mainapp


.PHONY: deploy
deploy: push 
	kubectl create -f mainapp.yaml

.PHONY: delete
delete: template
	kubectl delete --ignore-not-found -f mainapp.yaml
