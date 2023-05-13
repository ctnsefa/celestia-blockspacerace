# -*- coding: utf-8 -*-
import requests
import json
import random
from flask import Flask, render_template, request
from requests.exceptions import RequestException

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_none'

def generate_random_hex(length=16):
    """Generates a random hex string."""
    return ''.join(random.choices('0123456789abcdef', k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        result = pay_for_blob()
    return render_template('index.html', result=result)

@app.route('/pay-for-blob', methods=['GET', 'POST'])
def pay_for_blob():
    """Sends a POST request to a specific node with given IP and port."""

    if request.method == 'POST':
        node_ip = request.form.get('node_ip')
        node_port = request.form.get('node_port')
        namespace_id = generate_random_hex(16)  # 16-character random hex string for namespace_id
        data = generate_random_hex(50)  # 50-character random hex string for data

        payload = {
            'namespace_id': namespace_id,
            'data': data,
            'gas_limit': 80000,
            'fee': 2000
        }

        try:
            response = requests.post(f"http://{node_ip}:{node_port}/submit_pfb", json=payload)
            response.raise_for_status()
        except RequestException as e:
            return {"error": f"Request error warning: {str(e)}"}

        try:
            result = response.json()
        except ValueError as e:
            result = {"error": f"JSON Error: {str(e)}"}

        return result
    elif request.method == 'GET':
        # Burada GET istegi için islemler yapilacak
        pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
