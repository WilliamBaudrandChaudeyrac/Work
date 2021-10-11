#by William Baudrand Chaudeyrac

import flask as fs
import requests, json
from flask import request, jsonify



def n_num_getter(scores, n):
    return list(scores)[n]

app = fs.Flask(__name__)
app.config["DEBUG"] = True

url = "https://4v9r83qfo4.execute-api.eu-central-1.amazonaws.com/dev"
response = requests.get(url)
data = json.loads(response.text);#put all the data collected from the json file into a  variable

print(requests.put(url))#status code check about the request made


#print(data) # to see how the data looks like

@app.route('/', methods=['GET'])
def all_data():
    return jsonify(data)


@app.route('/scores', methods=['GET'])
def score_data():
    return jsonify(data["scores"])


@app.route('/scores/<int:n>', methods=['GET'])
def n_score_data(n):
    n_num = n_num_getter(data["scores"], n)
    return jsonify({list(data["scores"])[n]: (data["scores"])[n_num]})


@app.route('/scores', methods=['POST'])
def add_new_score():#to add a new score
    score_value = request.json['score_value']
    score_key = request.json['score_key']
    new_score = { score_key: score_value }
    (data["scores"])[score_key] = score_value
    return jsonify(new_score)


@app.route('/scores/<int:n>', methods=['PUT'])
def put_score(n):
    new_key = request.json["new_key"]
    new_value = request.json['new_value']
    n_num = n_num_getter(data["scores"], n)
    return_info = {new_key: new_value}
    (data["scores"])[new_key] = (data["scores"]).pop(n_num)
    (data["scores"])[new_key] = new_value
    return jsonify(return_info)


@app.route('/scores/<int:n>', methods=['PATCH'])
def patch_score(n): 
    new_value = request.json['new_value']
    n_num = n_num_getter(data["scores"], n)
    (data["scores"])[n_num] = new_value
    return jsonify({list(data["scores"])[n]: new_value})



@app.route('/scores/<int:n>', methods=['DELETE'])
def del_score(n):#to delete the score
    n_num = n_num_getter(data["scores"], n)
    return_info = {n_num: (data["scores"])[n_num]}
    (data["scores"]).pop(n_num)
    return jsonify(return_info)

app.run()