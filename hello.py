from flask import Flask
from flask import make_response
app = Flask(__name__)


@app.route("/api/v.1/ping" , methods=['GET'])
def return_message():
    respo = make_response ("pong")
    return respo

if __name__ == '__main__':
    app.run(debug=True)