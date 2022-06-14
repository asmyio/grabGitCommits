#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script reads any GitHub public commits and write to a database.

    1. It extracts commits and conversation.
    2. Returns progress and results (interesting comments/sorted comments).
    3. Save the returned results to a database (MongoDB)
"""
import json, os, requests, sys, datetime
from pymongo import MongoClient
from bson.json_util import dumps

def filter_commits(db_host, db_port, repo_owner, repo_name, data):
    for i in data:
        sha = i['sha']
        author = i['commit']['author']
        commit_message = i['commit']['message']
        comment_count = i['commit']['comment_count']
        html_url = i['html_url']
        filtered_data = {
            'sha' : f'{sha}',
            'html url' : f'{html_url}',
            'comment count' : comment_count,
            'commit message' : f'{commit_message}',
        }
        filtered_data.update(author)
        print(filtered_data)
        write_to_mongodb(db_host, db_port, repo_owner, repo_name, filtered_data)

def get_commits(repo_owner, repo_name):
    github_repo_path = 'https://api.github.com/repos/'
    github_commits = github_repo_path + f'{repo_owner}/{repo_name}/commits'
    response = requests.get(github_commits).json()
    print(response)
    return response

def read_from_mongodb(repo_owner, repo_name, db_host, db_port):
    client = MongoClient(db_host, db_port)
    db = client[repo_owner]
    collection = db[repo_name]
    data = collection.find()
    data = list(data)
    json_data = dumps(data, indent = 2)
    print(json_data)
    return json_data

def write_to_mongodb(db_host, db_port, repo_owner, repo_name, filtered_data):
    client = MongoClient(db_host, db_port)
    db = client[repo_owner]
    collection = db[repo_name]
    filtered_data.update({'last modified (UTC)' : datetime.datetime.utcnow()})
    collection.replace_one({'sha' : filtered_data['sha']}, filtered_data, upsert = True)

def get_input():
    
    if len(sys.argv) > 1:
        repo_owner  = sys.argv[1]
        repo_name   = sys.argv[2]
        db_host     = sys.argv[3]
        db_port     = sys.argv[4]

    else:
        repo_owner = input('repository owner:   ')
        repo_name  = input('repository name:    ')
        db_host    = input('DB Host:    ')
        db_port    = input('DB Port:    ')
    
    return repo_owner, repo_name, db_host, int(db_port)

def endpoint_trigger(repo_owner, repo_name, db_host, db_port):
    try:
        data = get_commits(repo_owner, repo_name)
        filter_commits(db_host, db_port, repo_owner, repo_name, data)
    
    except Exception as e:
        return e

def main():
    try:
        repo_owner, repo_name, db_host, db_port = get_input()
        print(f'Repository Owner: {repo_owner}\nRepository Name: {repo_name}\nDB host: {db_host}\nDB Port: {db_port}')
        data = get_commits(repo_owner, repo_name) 
        filter_commits(db_host, db_port, repo_owner, repo_name, data)
        read_from_mongodb(repo_owner, repo_name, db_host, db_port)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()