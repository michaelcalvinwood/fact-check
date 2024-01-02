host = '0.0.0.0'
port = 7200

from flask import Flask, render_template, request, redirect, session, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/compare', methods=["POST"])
def compare():
    data = request.get_json()
    sources = data.get('sources', [])
    content = data.get('content', '')

    num_sources = len(sources)
    content_length = len(content)

    if (num_sources == 0):
        return "Bad Command: missing sources", 400

    if (content_length == 0):
        return "Bad Command: missing content", 400
    
    return f"Num Sources: {len(sources)}"

    return 'ok'

if __name__ == '__main__':
    print('running the app')
    app.run(host=host, port=port)