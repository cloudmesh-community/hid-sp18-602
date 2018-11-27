
# Scalable Microservices to Label yelp images using Kuberenets

```
See other projects how to do the author and keywords

Indiana University Bloomington
Bloomington
Indiana, 47404, USA
knaredla@iu.edu
```

---

Keywords: docker, vision, kubernetes, yelp, redis, pub/sub

---

## Introduction

:o: Can not be replicated

:o: Missing Benchmark so a comparision is highlighted (that what a benchmark is)

:o: All sections have to be revisited as sections wer done wrong possibly even in the original 
latex file. Take a look at the TOC.

The applications are growing complex, not just functionality wise but
also the data generated and used are highly increasing. This makes it
absolute necessary to break down such complex application, instead of a
monolithic application so that product deployed is much more
maintainable, scalable, reliable, independent of failure of other
functional components of the application,portable, easy to deploy on
different cloud platforms, and so on. Most of these suit of best
practices called "Twelve-Factor Apps" can be bought into production of
Software applications using technologies such Docker, Kubernetes and
Microservice architecture [@hid-sp18-602-twelve-factor]. In this
project, an application is built using a combination of these three
technologies. In the below subsections, these concepts are briefly
introduced to better understand the working of the application.

Docker
------

Modern applications are often built using different technologies with
different versions based on the application requirement. Deploying many
such application on a single Operating System could be a huge risk at
times especially when there is a conflict in dependencies between
applications. For instance, if you consider installing 2 versions of
Nginx on the same OS, there would be a conflict with the namespace,
network port making it logically cumbersome to install same soaftware
with 2 different versions. Although the concept of containerization is
old, the ability to package applications with their dependencies into
the container, making applications independent and isolated from other
applications is huge progress to deploy applications, this is achieved
with Docker container technology. Morover,it is very easy to run
multiple containers using Docker. The docker image which is a snapshot
of the container is the basis to build a container. The Docker container
image is a packaging format that contains all the dependencies necessary
for the application along with required intial steps such a swtting
environment variables, or even running command to start the application.
These images are hosted on public or private repository such as
docker.hub, google storage. There are 2 ways to build a docker image,
first is to build Dockerfile, and the second way is make changes on
previous docker image. In most cases, a Dockerfile is built on a base
image that is useful for the application and then all the required
dependecies,commnads are added. Once the docker image is ready it takes
simple commands to build the container,push the final docker image to
the storage repository, and pull the docker image whenever required.
Thus, it is easy and robust to create, distribute and run applications
using Docker Containers with docker images and docker command-line
tools. There are less or no restrictions for docker usage, as containers
can be built on any machine with Docker installed it is highly in use by
DevOps [@hid-sp18-602-docker].

Kubernetes
----------

Although Docker makes it easy to deploy and run applications using
container technology when it comes to application configuration, service
discovery, managing updates, secrets management and monitoring
containers on the cluster, a better technology is required to leverage
all of these tasks. Here comes Kubernetes, an open-source platform that
provides a high level of abstraction and orchestration of containers
deployed on one or more clusters, which in turn are treated as a single
logical machine. Usually, a cluster has single Kubernetes master nodes
that keep on running despite explicitly deleting, and zero or more
worker nodes [@hid-sp18-602-kubernetes]. The master node is responsible
for managing the cluster, whereas the worker nodes work like a VM, it
consists of one or more pods, Volume, network ID and tools to handle
container operations.

A pod is the smallest unit of Kubernetes and it consists of one or more
containers. All the containers in the pod have shared the same
filesystem and IP address, this makes the communication between
containers in a pod easy. Each of these pods created based on the scheme
which is usually in YAML or JSON file format. The scheme covers
important aspects of spec which specifies the Pod behavior, container
name, container ports. A pod without Services or Replication Controller
cannot be accessed by the external client, neither scaling and
distribution of the application are possible  [@hid-sp18-602-pods].

Services provide an external interface for one or more pods. The Service
schema definition has 3 important parameters: kind, metadata, and spec.
The kind is set to Service to indicate a Kubernetes Service, which is
deployment, pod in case of Kubernetes deployment, pod definition files.
The label app and the name constitute the metadata. The spec mapping
includes a ports mapping for port 80 with name HTTP. The selector is the
key mapping in the spec and specifies a mapping to be used for selecting
the Pods to expose via the Service. Therefore, the service diverts the
network traffic to all its pods with the same label as the label
selector specified in the Service spec, in a round-robin manner. There
are 3 different types of Service: Load Balancer, Internal IP, Node port.
If a Service type is ClusterIP, then the service is accessible only
within the cluster via its internal port. Whereas if the service type is
Node port then the service is accessible from outside the node port,
which further routes the traffic to internal port Cluster IP of the
service, that is automatically created. Similarly Load Balancer service
type also automatically creates Node port and cluster IP. It gives
access for the external user to ping the IP. In addition to this Load
Balancer has the responsibility to balance the load between all the Pods
in Service [@hid-sp18-602-services].

Another important aspect in scaling applications is Replication
Controller, which manages the replication level of Pods by setting
"replicas" in Replication Controller definition or on the command line
with the --replicas parameter. This ensures that number of Pod replicas
are running at any given time. If a replica fails or is stopped
deliberately a new replica is started automatically. With these 2
crucial features scaling and replication factor, Kubernetes keep
microservices up and running all the time. Hence, Kubernetes is
production-ready, which provides dynamic container cluster orchestration
in real time.

Kubernetes as a cluster manager provides the feasibility for deploying
Microservices by breaking an application into smaller, manageable,
scalable components that could be used by groups with different
requirements; Fault-tolerant cluster in which if a single Pod replica
fails (due to node failure,for example), another is started
automatically; Horizontal scaling in which additional or fewer replicas
of a Pod could be run by just modifying the replicas label in the
Replication Controller or using the replicas parameter in the kubectl
scale command;

Google Cloud Platform
---------------------

Google Cloud platform gives the flexibility to scale quickly and handle
intense data while having the luxury of not having to maintain the
robust infrastructure, servers, networks etc and create business
solutions. It provides Cloud shell, which comes with a package of a
command-line tool, temporary VM instance of GEC, and access to Google
API with implicit authorization [@hid-sp18-602-cloud-shell]. Also, it
supports language such as Python, Java, Go, PHP,and Ruby. Moreover, the
command-line tool exclusively supports Cloud SDK gcloud command line
tool. The other alternative to Cloud Shell is to download Google Cloud
SDK and enable Authorization through some keys.

Google API
----------

Google API is a set of application programming interface which allows
communication with google services and integration of other services. It
is great tool for developers to perform operations and use its features
easily, google map API, google Visualization API, good AJAX search are
few examples.

### Cloud Pub/Sub API

Cloud Pub/Sub API is a message passing product that is highly useful for
communication between independent applications hosted on Google Cloud
Platform. The concept of Cloud Pub/Sub has 2 endpoints sender and
receiver and having one instance cloud pub/sub would allow interaction
between many applications. The main advantage of Pub/Sub compared to
other messaging tools like RabbitMQ is it is asynchronous and decouples
publisher from Subscribers, that is any Client who subscribed as Sender
or Publisher can send, Receive messages irrespective of the client on
the other side. In this project psq: Cloud Pub/Sub, a powerful, scalable
and reliable messaging tool, implemented using Python is used. It has
features similar to rq, simpleq and celery. It forms the basis for
communication between microservices, especially main application and
frontend [@hid-sp18-602-pub-sub].

### Cloud Vision API

Cloud Vision API is the most popular API that Google has till date. It
is very easy and efficient to analyze the content of the image, which
has state-of-the art tools for Image detecting features like: face,
text, label and document text,web detection. It is further made easy to
use, through Cloud AutoML suite. Using Vision AutoML, it is just one
click away to upload images and run pre-determined, custom machine
learning models. It is built based on Google's powerful technology of
learning-to learn, neural network architecture. In fact, building custom
ML model is just few steps [@hid-sp18-602-cloud-automl]. First,
uploading training dataset with images labeled into google bucket or
human-support to label images and the ML model is trained according to
the provided dataset. And then test data is passed, and accuracy of
prediction, classification of test data set is determined. However, this
feature of Cloud AutoML is accessible to only limited customers, but the
basic feature of labeling the images such as data in Google is quite
possible through REST API and are available to use in different
programming languages [@hid-sp18-602-cloud-vision].

Redis
-----

Redis is open source in memory database and is useful as database, cache
and message broker. It has different data structures, remote, persistent
and scalable to address wide variety of problems [@hid-sp18-602-redis].
The redis-cli command line tool allows to run command and get details of
the clients link to redis-database, configuration and monitor command
allows to check how server is responding to requests from client to read
or wrtie data. The redis-py package is a python implemenation to
interact with Redis storage. With popularity of Kubernetes, The
Redis-Enterprise version is exclusively built to use with kubernetes.
The documentation provides easy steps to create Redis cluster and link
with one or more pods running on the kubernetes. All the features of
kubernetes to replicate, scale and assign port are leveraged to
Redis-cluter, this is gives immense opportunity to work with multiple
pods, connecting to one-single redis cluster, along with a private redis
container on each of the pods. Another main reason for extending redis
to kubernets is the increase in usage of its docker image hosted in
docker.hub public repository. In this project StrictRedis class of Redis
is used to connect with Redis backend storage. It gives access to simple
functions like sadd,smemeber,sget to get and set key-value pair objects
in-memory database of redis [@hid-sp18-602-redis].

Yelp Dataset
------------

Yelp provides an open-source dataset for the challenge with students and
university grads. The yelp data set is huge of nearly 2.66 gigabytes of
dataset comprised of all the text details present in yelp, this may
include all kinds of business and theri details. Apard from this, yelp
also holds photos dataset which is 7.50 gigabytes of compressed dataset,
which are purely images of count nearly 200,000, for purposes like image
analysis, apply machine learning and computer vision technologies. The
text-based dataset is usually in JSON/ CSV, SQL format that can be
downloaded from their website. In addition to this Yelp also gives
access to their data through Yelp-Fusion. Yelp Fusion provides REST API
to get access to search, business, metadata. This reduce lot of overload
of downloading un-necessary data and gives the opportunity to choose
selectively required paramets and leave the rest. This is advantageous
not just in terms of space, but also the time taken using REST API is
far more efficient and quick compared to the downloading such huge
dataset and handling them again. Therefore,in order to make use of these
REST API Authentication is required, which is recently modified to the
Private Key authentication method, which is a simple 2 step process.
Create an account, create manage app, fill in details and the private
key is generated [@hid-sp18-602-yelp].

REST API
--------

Representational state transfer (REST) is any interface between systems
based on HTTP properties, web services to obtain data and send data. It
is an architectural style that is as simple as function calls and it is
adapted in various applications. REST API is of course central theme of
this project. The main reason it is widely used across many programming
applications is it can be easily used in sync with the other
functionalities of the application. On the other hand REST API doesn't
need any software or particular usage of protocl, it simply works with
HTTP and many other protocol. In order to use for a specific server, the
package to authenticate that server would need to be installed.

There are 2 important aspects to the REST API is request and response
object. The request sent to the API usaually includes the http url that
serves as an endpoint to client or server and the parameters, header
details that has to be sent according to your need. Whereas the response
object consists of data that is returned upon the request call, is
usually in some format such as XML, JSON format. JSON is Javascript
Object Notation is a data format that is extensively used to expose API.
This can be easily imported via package json. There are many popular
function that can convert any data into JSON and vice-versa. Two of the
popluar python based JSON encoder and decoder are JSON dump and JSON
load. json.dump() function takes an json object and convert string-type
data and json.load() converts data, from file-like objects and convert
into JSON object. The response object is further stored and manipulated
according to the requirements. The general requests are GET, POST, PUT,
HEAD, DELETE, PATCH. In this project, mainly GET, POST request listed
and explained briefly.

-   **GET Request** GET Request is used to request data from a
    resources, and are stored in cache and so they have length
    restriction which makes it necessary to send limited data via GET
    Request. Hence a query string sent in the URL of a GET request has
    carfully choosen parameters that are required. The data received
    from the server with GET response is stored in response object which
    could of JSON format.

-   **POST Request** POST request is used to send data to the server,
    the data need not necessarly be the data that has to be stored in
    the server, rather it could be credential details, or simply
    acknowledgement. POST request are not cached and hence no
    restrictons on data length. The data sent to the server with POST is
    stored in the request body of the HTTP request.

## Approach


The main aim of the application is to label photos from Yelp dataset
retrieved on passing location and search term such as food, dinner,
using cloud vision API. The application is divided into 3 microservices
frontend, backend, and mainapp. Each of these functionalities is
explained below along with intial setup.

### Initial Setup

As mentioned above,the application requires 2 important API Cloud Vision
API and Pub/Sub API, which have to enabled for the specific project id,
the application can be started, in google cloud console. The best part
for a software developer to test the working application is to launch
directly using gcloud command-line tool, as it doesn't require
authentication setup. For Cloud SDK installed on the local environment,
setting up the authentication is crucial. For this, it is first required
to create a service account and download service account key which is
usually in JSON file format. Then set the environment variable
`GOOGLE_APPLICATION_CREDENTIALS = [PATH]`, where `PATH` is the file path
of the JSON file downloaded from Google Console Dashboard.

After setting the environment variable, it is important to activate
gcloud command line tool, with the command "gcloud init". Then it is
required to setup the cluster to run he project. The cluster is built on
Google Cloud, for billing is activated on your Service Account. To setup
the cluster, it is required to choose the compute zone. The command
"gcloud config set compute/zone \<zone-name\>" sets up the particular
zone you would want your cluster to locate at.This is important becuase
it provides less latency when connecting to the cluster from gcloud,or
via Cloud SDK. The zone-name would like east1-b,central1-a and so on,
and it is better to choose according to location, although the features
offered doesn't differ much. The actual cluster can be created using the
command "gcloud container cluster create \<cluster-name\> --num-nodes
\<num\> --scope cloud-platform". This command specifies cluster name and
the number of nodes created for each zone of that cluster. After
creating a cluster, the cluster should be authorized with the service
account, in order to get access to all the api's. Hence the command "
gcloud container clusters get-credentials \<cluster-name\>". If the
cluster is perfectly created then you should be able to get the correct
information for the cluster created by activating "kubectl
cluster-info". Since initially, there are eno pods, services,
deployments created on running the command kubectl get pods you find no
pods created. The execution section give more details on how to run the
project.

### Frontend Microservices

The frontend of the application plays a key role as the load balancer
service for the entire application. It is basically a dynamic web-page,
which allows the user to enter location, for example, San Francisco, CA
and term like food, dinner. Based on these inputs, photos are fetched.
The technologies used for the web-page along is python, html,javascript
and css. The below paragraph explains breify about each of these
technologies and how they have been used in te frontend of this
application.

-   **Python** Python web-development framework Flask is used to make
    server calls to storage.py. The flask is an opensource tool which is
    an easy to use tool for server-side scripting. It can be installed
    using pip install flask command and imported in python via Flask
    package. Because it is a micro framework it can be implemented on
    top of any backend service with no restrictions like particular
    tools,libraries, or extensions are required. Moreover, Flask
    supports RESTful requests for dispatching GET,POST. Hence it is very
    useful in our project to easily make use of API to communicate and
    recivie from backend.

-   **Javascript** JavaScript is a core-technology mainly used to build
    dynamic web-pages. There are different framworks such vue.js,
    AngularJS,ReactJS, to design creative and interactive web pages. In
    this frontend javascipt is extended via a material design file in
    storage.googleapis.com. This really reduces the time, effort and
    gives world-class view for the webpage.

-   **HTML** HTML Hypertext Markup Language is useful to add content to
    the webpage. To make the webpages dynamic and add style to the
    page,Javascript, CSS are used. The HTML is the base of the webpage
    no matter any web-technologies out there, they must be added on top
    of HTML base page.

-   **CSS**

    Cascading Style Sheets (CSS) is used for styling the HTML webpage,
    with respect to display and it is added either internal with
    \<style\>\</style\> tags or external using CSS file. The CSS for
    this project is taken from google style package,googleapis for
    fonts, material icons and for other design can be selectively picked
    from material designs stored at google storage.

In this frontend, the main.py imports flask and it is the main program
that connect the frontend and server calls to the storage.py where
StrictRedis of REdis is imported and labels, respective imageurl stored
are retrieved. The received data from storage,py are then passed on the
web page via `render_template()`, this will send the the html page to
view and also passes the data required. There are 2 views enabled in the
webpage. The intial view consists of 2 input text box for user to enter
location and category. This information is routed to `get_yelp_images()`
function in mainapp via pubsub client. This enables the whole process of
extracting photos of the top 10 business from the search results based
on the location and term and then store their urls with annotations
detected using vision api, in redis storage. After that process ends and
the redis storage now has the relevant data, the 2nd view is activated
with the labels and images as the storage.py functions in the forntend
responds. Thus each of the services are very much linked to the frontend
service, it is like the start and endpoint of the project. Once the
images with labels are loaded, how many ever times you refresh you don't
see a change in the display because the data retrievd via storage.py
doesn't change. As the frontend service is deployed as a load-balancer
service an external IP is provided which enables user to access outside
of the cluster through a web-browser.

### Backend Microservice

The backend of the application is the storage service through Redis
which is important for storage of images and their respective labels
determined using Cloud Vision API [@hid-sp18-602-redis]. The redis is
accessible through redis image specified in backend.yaml file. The data
is stored into redis instance via Mainapp and retrieved in frontend in
order to populate the page with resulting images-label pair.

### Mainapp Microservice

The mainapp provides the actual functionality of the application,
starting from scraping the data to generating the desired output. The
major functionalities involved in the service is divided into
main.py,`yelp_label.py`, vision.py and storage.py. Each is further
modularized with function, which are briefly explained in below
paragraphs.

The `yelp_images.py` has 4 functions `query_api()`, `get_business()`,
`search()` and `request()`; As the given location and term are passed to
`query_api`, it sends the information to search function. The search
function sends a GET request (GET
https://api.yelp.com/v3/businesses/search) with parameters term,location
and search limit equal to 10 in the json object. The JSON object
response for the GET request is a dictonary type and is returned to
calling function. The `query_api()` stores each buisness list into
businesses dictonary. This business ist consist of several other
parameter like rating, price, id, categories, location details,
reviewcount and so on. But yelp-fusion offers an exclusive option to get
more details of each business via GET Request (GET
https://api.yelp.com/v3/businesses/id) with business id. Therefore, for
each business, business id is extracted and passed to `get_business`. In
this function, request is sent with business path
https://api.yelp.com/v3/businesses/ and business id is appended to form
the appropriate url for the request. The response object for this
request consists of details specific to that business only, which
includes open hours, photos and reviews. For this project, we require
only photos of each business, hence the urls of the photos for all the
businesses are appended to a list. All the photos are returned to the
calling function in main.py.

In vision.py, the authorization to access Vision api is set through
Google Credentials python package. The authorization done at this step
isn't specific to vision api rather it is common to access almost any
Google API. Now, for image passed to the `detect_labels()`, a post
request is sent to Vision API to annotate the image, by particular
mentioning the label detection feature and the the image url for that
image. It is important to specify the feature, or any further details of
the image as it imporves Machine Learning model for the analysis of the
photo by adding weightage to each of the parameters. Along with the
label which is a description parameter of string type, response object
consists of details of the image such as score, confidence, location,
and so on. The label annotation is return to the calling function for
the sent image url.

In storage.py, StrictRedis class is imported to instantiate redis
object. The redis in memory storage is very useful because of it's
ability to store objects in key-value pair. Taking advantage of this all
labels are stored with labels as key and label name as the value. Also
for each label as key the image url is stored as value . This makes very
easy to retrieve data in the frontend service,by just simply looking for
the associated imageurl for the label in the list of
labels [@hid-sp18-602-redis-implementation].The `add_labels` function
stores all the annotated label for photos into a labels list and
`add_image` fucntion stores label and photo as key-value pair.

To summarize, main.py brings together all the above functionalities, it
retrieves the data from `yelp_images.py`, passes photos to vision.py to
label each one of them and stores using storage.py. As pub/sub enqueues
the whole process in main.py, once the task is done, the frontend gets
triggered.

### Pods, Services, Deployments

There is one yaml file for each of the microservice, which includes
schema for service as well as deploymenet. The kubectl create -f
\<file.yaml\> command included in the Makefile creates the pods,service
and deployments. As discussed above the important parameter in general
are type, label selector, replica, container image and the port where
they are exposed. In this application the frontend service is created as
type load balancer. This exposes the service outside of the cluster
through an external IP. Once each of the pods are deployed, the
application is production ready. The scalability is maintained with
replica factor, which ensures deletion or failure of one or 2 pods
doesn't stop the application from running. Also the constant updates are
made easy with rollback.

## Execution

The execution of the application is incorporated through Makefile. Just
by running make all inside yelplabel directory, will spin the docker
container images, creation of pods,services and deployments. By
executing the command "kubectl get pods" list all the pods created and
"kubectl get services" will show the services up and running with their
given IP address. The external IP of the frontend service, is available
to curl or run in the browser. This is also the load-balancer for the
application, so on request the traffic is diverted to other services
within the internal port and the entire application is up and running.
In order to delete all changes you can run the command,where as in order
to delete services,pods and deployments you can run the command "kubectl
delete --all" pods,servies,deployments.

Challenges
----------

As there are lot of advanced technology out which share same sort of
features it is debatable to choose the right technology stack in order
to develop an application, that atleast meet the requirements and
dvelopemnt practices mentioned in 12app-factor. For instance, this
application can be implemented with Google Bucket Storage instead of
Redis as it also satisfies with key-value kind of storage system. The
debug aspect is the challenge because of the layers of abstraction over
the microservices, the deployments and everything works fine if there
exists an error within one of the microservices, which gets hard to
figure out at times. To an extent we can make use of kubectl logs and
google cloud provide error report.

## Results

The results of the project is to display labeled images from Yelp photos
dataset. And this ahiecved by populating the browser with the label and
imageurl pair retrieved from redis. As the cloud-vision api is a
pre-trained model on huge dataset of Google, the label detection is
done, in less amount of time and with high-accuracy rate in terms of
average score is 0.75. For this application, only photos of top 10
business for the search results are choosen and the image.annotate
request is reiterated for 3 times to make sure best label suitable label
is detected for the image, if not in a single request.

Benchmark
---------

Deploying the application is made easy with the use of Docker and
Kubernetes. The Makefile and Docker file included installs all the
necessary dependecies to creating pods,services and deployments. This
takes around 2-3 minutes to generate the external IP address.The runtime
analysis of the application, depends on the dataset volume for the given
input, as a result it takes few minutes for the label-detection and
showcasing the results on the browser. The benchmark for this project
extensively depends on Cloud Vision API and Redis Storage. As Redis
operates as in-memory database with key-value storage it servers the
applications purpose in retrieving,storing labels,imageurl in efficient
amount of time. Whereas the Cloud vision API although it has good
reputation to show accurate results, the bath processing for the images
is limited. Moroever, the challenge with yelp photos is to able to
distinguish between different varities of in food catgoery, for
instance.

## Conclusion

Thus application to scrape data from yelp-fust thion API and detect
label using Cloud Vision api, which is neatly displayed on a browser
with the support of redis storage technology, follows MVC architecture
workflow which important dier in application deployment. With Kubernetes
not just orchestration of docker components but the flexibility,
scalability for the deployment of microservices is highly achieved.

## Future Scope

:o: this is not an experinece report. If you do a future scope we will keep the incomplete till you finished it.
Otherwise the section is called limitations or something like that

I attempted to make use of Cloud AutoML, Vision API to label MNIST
dataset as a part of this project, but unfortunately teh cloud AutoML
gives access to specific user to customize the pre-trained ML model
based on Google Cloud Vision. 

:o: We do not understand thsi limitation

This is a huge dataset of NIST authorized
handwritten dataset, highly used for testing the accuracy of ML models
for Computer Vision and Image Analysis. Using the same or more
technology stack, I would like to work on MNIST dataset to detect and
label handwritten images as side-project,irrespective of my class
schedule, during upcoming semester with the guidance of the professor
Dr.Gregor von Laszewski.

:o: certainly you can do this, you will have to take an indepoendent study.
Its like the class with 100% focus on report.

## Acknowledgement

The authors would like to thank Dr.Gregor von Laszewski for his support
and suggestions to write this paper.

