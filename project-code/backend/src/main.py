
import requests
import yelp_images
from vision import VisionApi
from kafka import KafkaConsumer,KafkaProducer
import json

producer = KafkaProducer (value_serializer=lambda m: json.dumps(m).encode('ascii'),bootstrap_servers='localhost:9092')
consumer = KafkaConsumer('SampleInput', bootstrap_servers='localhost:9092')

def label_images_task(image_urls):
    vision = VisionApi()
    result={}
    for image_url in image_urls:
        #image_content=requests.get(image_url)
       
        #print(image_url)
        label=vision.detect_labels(image_url)
        result[image_url]=label
        future = producer.send('labels', {image_url:label})
        
        

        
def get_yelp_images(term,location):
    label_images_task(yelp_images.query_api(term, location))


def callProducer(result):
    print("Msg to be sent to producer : {0}" .format(result))
    headers = {"Content-type": "application/json"}
    response = requests.post("http://localhost:4004/kafkaProducer", json.dumps(result), headers=headers)



#get_yelp_images("food","Indianapolis")

def get_input():
    #consumer call
    for message in consumer:
        data=json.loads(message.value)
        print(data)
        get_yelp_images(data['business'],data['location'])



get_input()
