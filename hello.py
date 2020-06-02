from flask import Flask,request
app = Flask(__name__)

@app.route('/uri/<name>', methods=['GET'])
def post(name):
    return 'Hello, {}!'.format(name)

@app.route('/post', methods=['POST'])
def uri():
    data = request.get_json(force=True)
    name = data['name']
    return 'Hello, {}!'.format(name)