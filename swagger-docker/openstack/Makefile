SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=swagger.yaml
CONFIGFILE=admin-openrc.sh
DESTDIR=server/glance/flaskConnexion
CREATED=server

all: service start 
	@echo "DONE"

docker-all: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build -t knaredla/openstack .
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull knaredla/openstack
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -p 8080:8080 knaredla/openstack

docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f knaredla/openstack
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)

service: dest
	@echo "creating the service..."
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython3=true
	rm *.jar

	pip install python-openstackclient
	pip install python-glanceclient
	pip install python-keystoneclient

	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cp $(CONFIGFILE) $(DESTDIR)/swagger_server/controllers
	cd $(DESTDIR)/swagger_server/controllers && source admin-openrc.sh


	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install

start:  
	@echo "starting the service..."
	cd $(DESTDIR) && python -m swagger_server

test:
	curl http://localhost:8080/api/list_images/


stop:
	@echo "stopping the service"
	ps -ef | grep swagger_server | grep -v "grep" | awk '{print $$2}' | xargs kill -9
	@echo "service stopped"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)
