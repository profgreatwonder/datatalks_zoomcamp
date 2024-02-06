import pickle
# from unittest import result
from flask import Flask, jsonify, request
# from flask import Flask
# from flask import jsonify
# from flask import request

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

# parameters
model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')

# print(dv, model)

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    # X = dv.transform([customer])
    # y_pred = model.predict_proba(X)[0, 1]
    # churn = y_pred >= 0.5

    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5

    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)


# had trouble with the command using unicorn to run flask app
# gunicorn --bind 127.0.0.1:5000 predict:app
# solution is to install waitress
# pip install waitress or conda install conda-forge::waitress
# then run the command below'
# waitress-serve --listen=0.0.0.0:9696 predict:app

