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
    allnam = all_game_names()
    #print allnam
    return render_template('allgames.html', alln = allnam)
    
@app.route("/pop")
def render_pop():
    return render_template('pop.html')
    
@app.route("/avg")
def render_avg():
    return render_template('avg.html')
    
    
def all_game_names():
    """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
    with open('video_games.json') as corgis_data:
        names = json.load(corgis_data)
    allnam=[]
    for x in names:
        if x["Title"] not in allnam:
            allnam.append(x["Title"])
            
    return allnam
    
if __name__=="__main__":
    app.run(debug=False)
