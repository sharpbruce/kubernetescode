from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Docker !!! Dont forget to Please subscribe, like, and comment on this video, TY!!!'
