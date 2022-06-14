#!/usr/bin/env python3
# encoding: utf-8
import json, requests
from flask import Flask, jsonify
from grab_commits import endpoint_trigger, get_commits, read_from_mongodb
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello everybody :D'

@app.route("/get_commit/<repo_owner>/<repo_name>/<db_host>/<db_port>" ,methods=['GET'])
def write_it(repo_owner, repo_name, db_host, db_port):
    db_port = int(db_port)
    endpoint_trigger(repo_owner, repo_name, db_host, db_port)
    data = read_from_mongodb(repo_owner, repo_name, db_host, db_port)
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    return data, headers

app.run()
