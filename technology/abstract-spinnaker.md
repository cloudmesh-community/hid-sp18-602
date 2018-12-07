## Spinnaker

Spinnaker is an open source, multi-cloud continuous delivery platform
that helps you release software updates with high velocity and
confidence. It provides two core features: cluster management to view
and manage your resources in the cloud and deployment management to
construct and manage continuous delivery
workflows @hid-sp18-602-www-spinnaker-io. The main advantage of
spinnaker is, it holds a modern software development concept of
continuous delivery that is application updates should be delivered when
they are ready, instead of on a fixed schedule. Also, it improves the
speed, stability of application deployment processes along with
supporting deployments across different platforms by several different
cloud providers.

Spinnaker provides flexibility to deploy  across multiple providers such as AWS EC2, Google Kubernetes Engine etc. Automated release is the widely used for  most of the software projects these days to save time and pipelines can be created to run integration, systems tests, monitor rollouts and trigger the events. This also provides, built in best practice deployments methods such as black canary for easier rollouts and rollbacks.
 
Concepts in Spinnaker are applications, which is nothing but collections of clusters which are in turn logical grouping of servers.Load balancer and firewall are also needed here for the application. For example load balance is needed to balance the traffic with in the server groups for the instances and also health checks can be enabled at each point. Spinnaker handles the underlying architecture to verify health checks , disabling the unused server groups, it supports the class constructs, the red and black strategy with rolling back in active development is one of the start feature available.


Although the project Spinnaker first started out with Netflix and then
google joined in 2014, the Spinnaker community now includes dozens of
organizations such as Microsoft, Oracle, Target, Veritas, Schibsted,
Armory and Kenzan @hid-sp18-602-www-spinnaker-gc.
