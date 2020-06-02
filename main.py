from flask import Flask,request
app = Flask(__name__)

@app.route('/by-name/<name>', methods=['GET'])
def by_name(name):
    return 'Hello, {}!'.format(name)

@app.route('/api/predict', methods=['POST'])
def predict():
    ccpFiltersToSQL = request.get_json(force=True)
    return ccpFiltersToSQL