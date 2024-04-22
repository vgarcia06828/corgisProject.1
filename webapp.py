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
    pop = pop_gam()
    #print pop
    year = 2004
    if "year" in request.args:
        year = int(request.args["year"])
    return render_template('pop.html', popg = pop, year = year)
    
@app.route("/avg")
def render_avg():
    return render_template('avg.html')
    
@app.route("/fft")
def render_fft():
    return render_template('funfact.html')
    
def all_game_names():
    with open('video_games.json') as corgis_data:
        names = json.load(corgis_data)
    allnam=[]
    for x in names:
        allnam.append({x["Title"]:x["Metadata"]["Publishers"]})
    return allnam
    
def pop_gam():
    with open('video_games.json') as corgis_data:
        num = json.load(corgis_data)
    allnum=[]
    for x in num:
        allnum.append ({x["Metrics"]["Sales"]:x["Release"]["Year"]})
    return allnum
    
#def pop_year():
   # """with open('video_games.json') as corgis_data:"""
        
#def highest_mil():
# with open('video_games.json') as corgis_data:"""
    
if __name__=="__main__":
        app.run(debug=False)