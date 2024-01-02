host = '0.0.0.0'
port = 7200

from flask import Flask, render_template, request, redirect, session, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return 'Hello World'

if __name__ == '__main__':
    print('running the app')
    app.run(host=host, port=port)