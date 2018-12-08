#!/bin/bash

export OS_USERNAME="nkeerthi"
export OS_PROJECT_ID="CH-819337"
export OS_PROJECT_NAME="CH-819337"
export OS_AUTH_URL="https://openstack.tacc.chameleoncloud.org:5000/v2.0"
echo "please enter your  openstack password"
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT
export OS_IDENTITY_API_VERSION="2"
2"

