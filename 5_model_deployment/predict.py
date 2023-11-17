import pickle

# parameters
model_file = '5_model_deployment/model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

print(dv, model)

customer = {
  'customerid': '8879-zkjof',
  'gender': 'female',
  'seniorcitizen': 0,
  'partner': 'no',
  'dependents': 'no',
  'tenure': 41,
  'phoneservice': 'yes',
  'multiplelines': 'no',
  'internetservice': 'dsl',
  'onlinesecurity': 'yes',
  'onlinebackup': 'no',
  'deviceprotection': 'yes',
  'techsupport': 'yes',
  'streamingtv': 'yes',
  'streamingmovies': 'yes',
  'contract': 'one_year',
  'paperlessbilling': 'yes',
  'paymentmethod': 'bank_transfer_(automatic)',
  'monthlycharges': 79.85,
  'totalcharges': 3320.75
}


X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print(f'input: {customer}')
print(f'churn probability: {y_pred}')

