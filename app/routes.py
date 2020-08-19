from app import app
from flask import render_template, request, jsonify
import requests
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():

    
    res= requests.post('https://tntymxzluw4.sandbox.verygoodproxy.com/post',
                            json={'cc_number': request.form.get('cc_number'),'cc_exp': request.form.get('cc_exp'),'cc_cvv': request.form.get('cc_cvv')})
    
    print(str(res))
    
    res = res.json()
   
    return render_template('decrypt.html', message=res)

@app.route("/forward", methods=['POST'])
def forward():

    os.environ['HTTPS_PROXY'] = 'https://USd5v28vqwq2YRxSADbfiYM1:15c59952-e907-491a-b409-931f1edbe127@tntymxzluw4.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'cc_number': request.form.get('cc_number'),'cc_exp': request.form.get('cc_exp'),'cc_cvv': request.form.get('cc_cvv')},
                        verify='cert.pem')
    res = res.json()

    return render_template('forward.html', response=res)

