from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/all")
def render_all():
    return render_template('allgames.html')
    
@app.route("/pop")
def render_pop():
    return render_template('pop.html')
    
@app.route("/avg")
def render_avg():
    return render_template('avg.html')
    
if __name__=="__main__":
    app.run(debug=False)
