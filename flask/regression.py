from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

def linear_model(values):  
    x = np.array([x[0] for x in values]).reshape(-1, 1)
    y = np.array([x[1] for x in values]).reshape(-1, 1)
    reg = LinearRegression().fit(x, y)
    score = reg.score(x, y)
    [[coef]] = reg.coef_
    [intercept] = reg.intercept_
    return np.around(score,2), np.around(coef,2), np.around(intercept,2)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    values = data['values']
    score, coef, intercept = linear_model(values)
    response = {
        'score': score,
        'coef': coef,
        'intercept': intercept, 
    }
    response = jsonify(response)
    return response