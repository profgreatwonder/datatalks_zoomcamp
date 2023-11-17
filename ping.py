# we want to turn this function into a web service
# def ping():
#     return "PONG"


# from crypt import methods
from flask import Flask

app = Flask('ping')

# we put a decorator to our function to increase it's functionality in order to turn it into a web service
@app.route('/ping', methods=['GET'])
def ping():
    return "PONG"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)