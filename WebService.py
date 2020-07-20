# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:54:04 2020

@author: @irvincabezas
"""

from flask import Flask, request
from flask_restful import Resource, Api
import subprocess, os

app = Flask(__name__)
api = Api(app)

users = []

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        # returns None while subprocess is running
        retcode = p.poll() 
        line = p.stdout.readline()
        yield line
        if retcode is not None:
            break
    

class Person(Resource):
    def get(self, email):
        users.clear()
        for line in runProcess(f'bash ./query.sh {email}'.split()):
            if line and line not in users:
                line = str(line.decode("utf-8").rstrip(os.linesep)) #remove newline from each line prior manipulation
                user = {'email': line.split(':')[0], 'password': line.split(':')[1]}
                users.append(user)
        return {'users': users}
    

api.add_resource(Person, '/target/<string:email>') #http://127.0.0.1:5000/target/example@example.com

app.run(port=5000)
    