import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/interests')
def interests():
    return render_template('interests.html', title="My Interests", url=os.getenv("URL"))