from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Docker cos it helps our container and Dont forget to Please subscribe, like, and comment on this video, TY!!!'
