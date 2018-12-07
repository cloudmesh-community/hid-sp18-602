# Cloud AutoML  :smiley: sp18-616-02 

| Keerthi Naredla
| knaredla@iu.edu
| Indiana University, Bloomington
| hid : sp18-616-02
| github: [:cloud:](https://github.com/cloudmesh-community/hid-sp18-602/edit/master/paper/paper.md)


---

Keywords: Cloud AutoML, Neural, Google Cloud, Vision

---

Cloud AutoML is the state-of -the -art tool to design high-quality
training and large-scale capable custom ML models. Using this, a user
with no or less ML knowledge can build ML model in short span of time,
low-cost hardware and infrastructure. It is a revolution by Google team
to get ML to small businesses with less AI/ML expertises. It is based on
2 important technologies transfer learning and neural architecture
search technology. The Neural Architecture search uses the concept of
learning to learn or meta learning with an auto-regressive controller
which builds a neural network on learning from feedback of child
network. As it is immensly expensive to compute and execute deep neural
networks, Google Cloud Services such as Google Compute Engine, Google
Cloud Storage support Cloud AutoML. In additon to this, Google API’s
provide the ability to customize pre-trained models in Cloud AutoML.
This section gives a brief introduction to Cloud AutoML, the technology
behind its functioning,and the importance of Google Cloud in Cloud
AutoML.

## Introduction

Cloud AutoML is an innovative tool with simple graphical user interface
to train and test users custom machine learning models. This is a result
of collaborative effort of Google Cloud AI, Google Brain and other
Google AI teams. The main purpose of developing Cloud AutoML is to
enable users and businesses with limited machine learning expertise to
easily build and train high quality custom ML models. It is built on
Google learning to learn, transfer learning, and Neural Architecture
Search technologies @hid-sp18-602-cloud-automl-launch.

Cloud AutoML is a suit of Machine Learning products. Google has recently
launched first product under Cloud AutoML: AutoML Vision which is a
service to access a pre-trained model or create a custom ML models using
Google Cloud Services, for image recognition, detecting image content,
classifying images and image-based recommendation system. It offers
drag-and-drop interface to upload images, train and manage models.
Similarly Google is working to support integration of it’s poweful API’s
into Cloud AutoML. Few of the API’s that are in real demand are, Google
Cloud Video Intelligence API which makes videos searchable, Google
Text-to-Speech, Speech-to-Text which is highly used in smart-home
devices, automation tasks, Natural Language API which is useful for
text-analysis, extracting useful information from users, Google
Translation which is useful for language detection ,conversion and
Google DialogFlow which highly improves interaction and conversation
with voice assistants. Thus using Cloud AutoML, a business can customize
ML model according to their needs by selecting any one or a combination
of these API’s  @hid-sp18-602-cloud-automl-main.

Just like cloud servers are used by several companies, small and big,
without any knowledge of underlying complexity involved in storing,
distribution and processing, the cloud automl can be used to build
customized neural network that serves the purpose without actually
understanding the complexity of generating a model
 @hid-sp18-602-cloud-automl-impact. Not only that, it is time-efficient
and high-accurate because the base model is already pre-trained on
immense data-archives and the resources used by Google. Also, AutoML
generated models run instantly on Cloud ML infrastructure leveraging the
hardware and powering Google’s own cloud.

With these major advantages, Cloud AutoML Vision is already in use by
many good companies across the globe. For instance, shopDisney uses
label-detecting feature with Cloud AutoML technology to build vision
models in order to label products with Disney characters, and product
categories. Also, these annotations are integrated into search engine
for better product recommendations. Urban outfitters use cloud automl to
automate product attribution process to recognize products like patterns
and dressstyles, which is very useful in terms of accurate search
results, product recommendation. Zoological Society of London are
actively using AutoML Vision to categorize different animals from the
images captured in order to analyze and understand animal motions,
distribution and human impact on
wildlife @hid-sp18-602-cloud-automl-launch.

## Mechnism

This is section is based on Google’s 2017 paper on Neural Architecture
Search with Reinforcement Learning, by Bareet Zoph,Quoc V.Le Google
Brain Team @hid-sp18-602-cloud-automl-mechanism. Neural Architecture
Search with reinforcement learning is the basis of the Google Automl. In
addition to this, the concept of Transfer learning which is to make use
of pre-trained models, in order to build a custom model with small
changes to base model, is the motivation for Cloud
AutoML @hid-sp18-602-transfer-learning. Many of the previously proposed
methods like Hyperparameter optimization, Neuro-evolution algorithm,
sequence-to-sequence learning lack some of the core concepts like able
to generate variable-length network, able to work at large-scale,
learning from reward signal without any supervised/manual intervention,
making use of previously learnt information or feedback framework which
is also called learning to learn or meta learning.

A recurrent neural network trained with reinforcement learning generates
a convolutional architecture. In this model, the concept of
reinforcement learning has a RNN called controller which is used to
generate a variable-length string, by constantly training the network
with results of child-network on the validation-set. And the result
which is in fact know as reward signal is processed through policy
gradient-method to further update the controller. With increase in
number of iterations of this process, the neural network grows,
resulting in higher accuracy. The key additions to this neural search
architecture model are: (1) Parameter-server scheme which uses
distributed training of child network and allows asynchronous updates to
the controller. This parallelism speed up the training process,rather
than spending hours on each child network. (2) Skip connections and
branching layers are used by the controller in order to increase the
search space and also the complexity of the architecture as a whole
rather than standard RNN.That is with skip connections the controller
can decide on what input layers should link to the current layer, rather
than choosing just the previous layer.

Using Neural Architecture Search the novel model built on CIFAR-10
dataset is called ConvNet for image-recoginition, has 3.65 test set
error,that is 1.05x faster than best human-invented models and novel
recurrent cell designed for Natural Lanaguage Processing on Penn
Treebank dataset, results in 3.6 perplexity better than any previous
RNN, LSTM models. Usually, to build ML models for such large datasets
take not only enormous amount of time but also immense effort of ML
experts would result in better architecture. But with the concept of
Neural Architecture Search, a machine can generate a recurrent neural
network that is far better than experts built state-of-the art models.
Hence Neural Architecture Search achives building best models from
scratch, with less human intervention, less time and high test set
accuracy @hid-sp18-602-cloud-automl-mechanism.

## Role of Google Cloud

Google Cloud is the one of prerequisites for functioning of Cloud AI
services such as Cloud ML Engine, Dialogflow,Google Cloud Job Search and
Discovery and other Google API’s. Using Cloud Machine Learning Engine,
data scientist and ML expertise can work together to design a ML model
with help of Tensorflow and then train, test the model on large scale
processed data deployed on a cluster
 @hid-sp18-602-cloud-mlengine-training.

Although Cloud ML Engine supports training of the model to the extent of
high accurate prediction rate, we need Google Cloud Storage for storing
input data for training and testing, staging all the dependencies of the
custom ML model into a trainer package, writing training artifact and
storing training and prediction output
files @hid-sp18-602-google-cloud-storage. Similarly, Customized Cloud
Vision models which are usually deep neural networks have several
millions of nodes, that need to undergo multiple training cycles to
acquire high performance, high accuracy, and this results in
computationally intensive even with special hardware infrastructure
 @hid-sp18-602-cloud-ai. Fei-Fei-Li, Cheif Scientist Google Cloud AI,
mentioned that “Google’s infrastructure is the solution to speed
training times. Google has specialized ASIC, GPU and TP hardware in its
cloud to accelerate training and improve the ROI with on-demand cloud
resource utilization” @hid-sp18-602-cloud-ai.

Google’s Cloud TPU:Tensor Processing Unit is crucial for lowering the
time required to train comutationally intensive models. It is built with
application-specific integrated circuits, and consists of 180 teraflops
computing power with 64 gigabytes of high-bandwidth storage
memory @hid-sp18-602-cloud-tpu-overview. It is flexible to shift models
running on Tensorflow to Cloud TPU. And it is important to consider
Cloud TPU, especially if the training dataset is huge, increasing, and
model takes several cycles to achive accurate prediction, as it
leverages requirement of local datacenters setup. Also with XLA
just-in-time compiler and Cloud TPU hardware which has matrix unit (MXU)
it is possible to train large models with very large batch size that
typically takes months and years in few weeks or months. But Cloud TPU
cannot be used if the neural network isn’t built using Tensorflow or the
main training loop of tensorflow program consists of operations, in that
case GPU: Graphic Processing Units can be used instead of TPU. GPU’s are
also useful to accelerate machine learning workload and these can be
simply added to VM instance on which model is
running @hid-sp18-602-cloud-tpu. Therefore, it is important to note that
TPU’s are not the only option,rather Google makes use of GPU, CPU’s to
run machine learning worklaods on Compute Engine when required. Thus,
Gloogle Cloud Services comes with all of these resouces which play a key
role in Cloud Automl and other Cloud AI products.

## Conclusion

Cloud AutoML is certainly a mission to get profound concepts ML,AI, deep
learning neural networks into usage for any company. Google terms this
mission as “democratizing AI, point-and -click AI for all”, as it is not
just about leveraging the technology to build deep layers of neural
network but it is also about leveraging the the infrastructure through
Googgle Cloud Services especially Cloud TPU, required for getting the ML
model into production in large scale and accuracy.

Moreover, with powerful Google API’s such as NLP, Speech, Vision,
Translation, building customized ML models becomes feasible and
flexible. Thus Google’s Cloud AutoML is sucessful in solving the issue
of requiring highly skilled and experianced Machine learning experts to
develop advanced neural networks and significant amount of time taken to
build such models manaully can now be machine-generated with Neural
Architecture Search with Reinforcement Learning and reused with Transfer
Learning. Hence any company can have AI/ML products that could match the
quality and speed of Google AI products.

The authors would like to thank Dr.Gregor von Laszewski for his support
and suggestions to write this paper.
