from flask import Flask, request
import requests

# Justin Hagerty and Zach Podbielniak
# Base example for comparison with using the decorator for minimalistic "invasive code for the python sdk"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/anotherTest")
def anotherTest():
    return "Hello World!"


@app.route("/outgoingflask")
def outgoingflask():
    # Information already defined for outgoing requests
    headers = {"Test": "things"}
    url = "http://127.0.0.1"
    response = requests.get(url, headers=outgoingTracerHeaders)
    print(response)
    return "Hello World!"

@app.route('/exampleDecoratorPath')
def health(incoming_wreq):
    return "Hello world!"








if __name__ == "__main__":
    app.run()