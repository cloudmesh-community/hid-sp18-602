from flask import Flask, render_template
from flask import request
from kafka import KafkaConsumer

import requests
import sys
import json

app = Flask(__name__)


@app.route('/')
def index():
    images_labels={u'https://s3-media1.fl.yelpcdn.com/bphoto/R8DJPyfrNoRpM-kUCOYM0Q/o.jpg': u'dish', 
          u'https://s3-media2.fl.yelpcdn.com/bphoto/yOVE7bXv5iZtlbBIPaSUIw/o.jpg': u'recreation', 
          u'https://s3-media4.fl.yelpcdn.com/bphoto/1B5xfxIO3WoqSrJrvxQMlA/o.jpg': u'dish',
          u'https://s3-media1.fl.yelpcdn.com/bphoto/dt_Ewi4fbXb7_Qli09OF6Q/o.jpg': u'room'}
    return render_template('display_results.html',images_labels=images_labels)
   
@app.route('/inputs',methods = ['POST'])
def inputs():
    query={
            'topic':'SampleInput',
            'data': {
                'business' : request.form['business'],
                'location' : request.form['location']
                }
          }
    callProducer(query)
    results()

@app.route('/results')
def results():
    #consumer call
    consumer = KafkaConsumer('labels', bootstrap_servers='localhost:9092')
    for message in consumer:
        data=json.loads(message.value)
        #print(data)
        #images_labels={}
        #for key,value in data:
         #   images_labels[key]=value
        #print(images_labels)
    return render_template("display_results.html",images_labels=data)
    
def callProducer(query):
    print("Msg to be sent to producer : {0}" .format(query))
    headers = {"Content-type": "application/json"}
    response = requests.post("http://localhost:4004/kafkaProducer", json.dumps(query), headers=headers)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
