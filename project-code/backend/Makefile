
.PHONY: all

all: 
	kubectl create -f mainapp_service.yml

.PHONY: clean
clean: 
	kubectl delete --ignore-not-found -f mainapp_service.yml
