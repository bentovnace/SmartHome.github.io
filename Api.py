from flask import Flask, request
import requests
import json
import subprocess as sp
app = Flask(__name__)


@app.route('/Light1', methods=['GET','POST'])
def Light_1():
    global data_1
    data_1 = request.args.get('input') 
    return str(data_1)
@app.route('/Light1state', methods=['GET','POST'])
def Light_1_state():

    return data_1

@app.route('/Light2', methods=['GET','POST'])
def Light_2():
    global data_2
    data_2 = request.args.get('input') 
    return str(data_2)

@app.route('/Light2state', methods=['GET','POST'])
def Light_2_state():

    return data_2

@app.route('/Light3', methods=['GET','POST'])
def Light_3():
    global data_3
    data_3 = request.args.get('input') 
    return str(data_3)

@app.route('/Light3state', methods=['GET','POST'])
def Light_3_state():

    return data_3

@app.route('/Light4', methods=['GET','POST'])
def Light_4():
    global data_4
    data_4 = request.args.get('input') 
    return str(data_4)
@app.route('/Light4state', methods=['GET','POST'])
def Light_4_state():

    return data_4



if __name__  == "__main__":
    app.run(host ='0.0.0.0',port = '5000')
    