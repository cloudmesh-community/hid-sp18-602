# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gcloud import pubsub
import requests
import psq

import yelp_images
from storage import Storage
from vision import VisionApi


def label_images_task(image_urls):
    vision = VisionApi()
    storage = Storage()

	for image_url in image_urls:
		image_content=request.get(image_url)
                label=vision.detect_labels(image_content)
                storage.add_labels(label)
                storage.add_image(image_url,label)


def get_yelp_images(term,location):
    for image_urls in query_api(term, location):
        q = psq.Queue(pubsub.Client(), 'images')
        q.enqueue('main.label_images_task', image_urls)

q = psq.Queue(pubsub.Client(), 'images')
