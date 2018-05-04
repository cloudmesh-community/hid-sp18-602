status: 70%

##Acknowledgement 

* Thanks to Professor Gregor Von Laszewski for support and guidance to do this project. 

##Description:

The main purpose of the porject is to understad the Microservices architecture using Kubernetes. In order to achieve this, an application
to label images from Yelp photos dataset is built.

* Technologies Used: Docker,Kubernetes,Redis,Cloud Vision API, Pub/Sub API, Cloud Shell,Python, HTML,CSS:Google Material Design

## Prequesite

* Create a service account on the Google Cloud Platform Console .

* Create a project which biling.

* Enable the Vision and Pub/Sub APIs.

The project is done using Cloud Shell in Google Cloud Platform. In order to build the porject on Google console it is required to download 
Cloud SDK, intialize gcloud command-line tool and set Authentication in order to make use of Google API's.

## Initial Setup

* Create a Container Engine

	```gcloud config set compute/zone us-east1-f```

* Create a cluster using gcloud

 	```gcloud container clusters create yelplabel --num-nodes 2 --scopes cloud-platform```
	
* Set up the kubectl command-line tool to use the container's credentials

 ```gcloud container clusters get-credentials yelplabel```

* Enter the yelplabel directory, and run the command. This will build Docker images and create pods,services,deployments for all the 3 microservices

   ``` make all ```

* Once the make is done, verify the pods by running 

	```kubectl get pods```

* Now,check the services by running

	```kubectl get services```

* Copy paste the external IP of the yelplabel-frontend service, which is type Load-Balancer, on to your browser, and click then Start the Labeling button.

* It takes some time to retreive all the data from yelp and label them using Vision API. After, few minutes, the browser will be populated with labeled photos from yelp dataset

##References

https://classroom.udacity.com/courses/ud615

https://cloud.google.com/vision/docs/

https://www.yelp.com/developers/documentation/v3/get_started

https://github.com/GoogleCloudPlatform/psq
