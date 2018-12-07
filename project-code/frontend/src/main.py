from flask import Flask, render_template
from kafka import KafkaConsumer,KafkaProducer
from flask import stream_with_context, request, Response
import requests
import sys
import os
import json

app = Flask(__name__)

result={}

@app.route('/')
def index():
   
    return render_template('input_page.html')
   
@app.route('/inputs',methods = ['POST'])
def inputs():
#    query={
#            'topic':'SampleInput',
#            'data': {
#                'business' : request.form['business'],
#                'location' : request.form['location']
#                }
#          }
    #callProducer(query)
    producer = KafkaProducer (value_serializer=lambda m: json.dumps(m).encode('ascii'),bootstrap_servers='localhost:9092')
    future = producer.send('SampleInput', {'business' : request.form['business'],'location' : request.form['location']})
        
    def output():
        for images_labels in results():
            print (images_labels)
            result.update(images_labels)
            #return render_template('display_results.html',images_labels=images_labels)
        
    return render_template('input_page.html') 

def results():
    consumer = KafkaConsumer('labels', bootstrap_servers='localhost:9092') 
    for message in consumer:
        images_labels=json.loads(message.value)
        yield images_labels
      
    return 

#def stream_template(template_name, **context):
 #   app.update_template_context(context)
  #  t = app.jinja_env.get_template(template_name)
   # rv = t.stream(context)
    #rv.enable_buffering(5)
    #return rv
@app.route('/display_results')
def display():
    #print(images_labels)

    return render_template("display_results.html",images_labels=result)
    
def callProducer(query):
    print("Msg to be sent to producer : {0}" .format(query))
    headers = {"Content-type": "application/json"}
    response = requests.post("http://localhost:4004/kafkaProducer", json.dumps(query), headers=headers)

@app.route('/shutdown')
def shutdown():
    t1.terminate()
    shutdown_server();
    return "Server shutting down....Khuda Hafiz!!"


if __name__ == '__main__':
    app.run(port=8080, debug=True)
