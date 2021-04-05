from flask import Flask
from flask import (Blueprint, current_app, flash, jsonify, redirect, request,url_for)
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():

    # puedes convertir esa variable en un string json así
    json_text =jsonify(todos)

    return json_text






# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)