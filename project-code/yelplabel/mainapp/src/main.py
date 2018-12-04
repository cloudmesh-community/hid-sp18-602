
import requests
import yelp_images
from vision import VisionApi
from kafka import KafkaConsumer
import json


def label_images_task(image_urls):
    vision = VisionApi()
    result={}
    for image_url in image_urls:
        #image_content=requests.get(image_url)
       
        #print(image_url)
        label=vision.detect_labels(image_url)
        result[image_url]=label
    return result

        
def get_yelp_images(term,location):
    result=label_images_task(yelp_images.query_api(term, location))
    response={
            'topic': 'labels',
            'data':result
            }
    callProducer(response)

def callProducer(result):
    print("Msg to be sent to producer : {0}" .format(result))
    headers = {"Content-type": "application/json"}
    response = requests.post("http://localhost:4004/kafkaProducer", json.dumps(result), headers=headers)



#get_yelp_images("food","Indianapolis")

def get_input():
    #consumer call
    consumer = KafkaConsumer('SampleInput', bootstrap_servers='localhost:9092')
    for message in consumer:
        data=json.loads(message.value)
        get_yelp_images(data['business'],data['location'])



get_input()
