.PHONY: all
all: deploy

.PHONY: deploy
deploy:
	kubectl create -f backend.yaml

.PHONY: delete
delete:
	kubectl delete --ignore-not-found -f backend.yaml
