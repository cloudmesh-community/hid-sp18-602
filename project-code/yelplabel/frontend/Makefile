
.PHONY: all

all:   
	kubectl create -f frontend_service.yml

.PHONY: clean

clean:	
	kubectl delete --ignore-not-found -f frontend_service.yml
