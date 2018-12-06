
.PHONY: all

all:   
	kubectl create -f frontend_service.yml

.PHONY: clean

clean:
	kubectl delete pods,services,deployments --all 

