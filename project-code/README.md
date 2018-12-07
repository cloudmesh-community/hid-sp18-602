## Scalable Microservices to Label yelp images using Kuberenets 

The main purpose of the porject is to understad the Microservices
architecture using Kubernetes. In order to achieve this, an
application to label images from Yelp photos dataset is built.

* Technologies Used: Docker,Kubernetes,Redis,Cloud Vision API, Pub/Sub
  API, Cloud Shell,Python, HTML,CSS:Google Material Design

## Acknowledgement 

* Thanks to Professor Gregor Von Laszewski for support and guidance to
  do this project.


## Prequesite

* Create a service account on the Google Cloud Platform Console .

* Create a project which biling.

* Enable the Vision API.

The project can be easily replicated on Google Cloud Platform becasue it requires google api clients to use vision API. In
order to build the porject on Google console it is required to
download Cloud SDK, intialize gcloud command-line tool and set
Authentication in order to make use of Google API's.

## Project Setup

* Enter the yelplabel directory, and run the command.

   ``` make all ```

* Once the make is done, verify the pods by running 

	```kubectl get pods```

* Now,check the services by running

	```kubectl get services```

* Copy paste the external IP of the yelplabel-frontend service, which
  is type Load-Balancer and port, on to your browser, and 

* It takes few seconds for the images to load from  yelp dataset and label them
  using Vision API. Then the browser should be populated with labeled images.


