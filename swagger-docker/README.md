Openstack Image Service- Glance
 
Acknowlegement:

I referenced the repo owned by Min Chen (hid-sp18-405) for the make file and docker file.

Service Descprition

As the client sends Request to the Server for list of images, the server trigger the KVM tacc 
OpenStack Server on Chameleoncloud.org. The Environment variables for this are set in 
admin-openrc.sh. 


I followed the instruction from handbook, chapter 34: REST Service Generation with Swagger
Start The Service

    clone the repository

    navigate to the directory

      cd /hid-sp18-602/swagger-docker/openstack/

    creates the swagger service from the yaml file with correct controllers

      make service

    start the service by execute:

      make start

    The following will show

      Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)



