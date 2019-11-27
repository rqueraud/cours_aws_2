from flask import Flask, request
from flask_restful import Resource, Api

import json
import time

with open('./data.json') as json_file:
    data = json.load(json_file)

class Tweet(Resource):
    def get(self):
        actual_time = int(time.time())
        index = actual_time%len(data)
        datum = data[index]
        datum["id"] = actual_time
        return datum

app = Flask(__name__)
api = Api(app)
api.add_resource(Tweet, "/tweet")
app.run(port="5002", host= '0.0.0.0')