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
        ganam = popgame_2004(year)
        text = "The most sold game in " + str(year) +" was " + str(ganam) + "!!"
        return render_template("pop.html", ganam = text, year = year)
    return render_template('pop.html', popg = pop, year = year)
    
@app.route("/avg")
def render_avg():
    avg = average_times()
    alnam = all_game_names()
    fact = "The average time to finish games is " + str(avg) + " hours!"
    return render_template('avg.html', oneFact = fact, aln = alnam, avg = avg, points=format_dict_as_graph_points())

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
    
def average_times():
    with open('video_games.json') as corgis_data:
        nu = json.load(corgis_data)
    avg = 0
    for num in nu:
        avg = avg+num["Length"]["All PlayStyles"]["Average"] 
    avg = avg /len(nu)
    return avg
    
def popgame_2004(year):
    """Return the game with the higest sales in one year."""
    with open('video_games.json') as corgis_data:
        years = json.load(corgis_data)
    highest=0
    name = ""
    for x in years:
        if x["Release"]["Year"] == year:
            if x["Metrics"]["Sales"] > highest:
                highest = x["Metrics"]["Sales"]
                name = x["Title"]
    return name
    
def format_dict_as_graph_points():
    with open('video_games.json') as corgis_data:
        vv = json.load(corgis_data)
        graph_points = ""
        tak = 0
        for game in vv:
            graph_points = graph_points + Markup('{label: "' + game["Title"] + '" , y: ' + str(game["Length"]["All PlayStyles"]["Average"])+'}, ')
            #if tak > 1:
             #   break
           # tak = tak + 1
        graph_points = graph_points[:-2]
        print(graph_points)
    return graph_points
    
if __name__=="__main__":
        app.run(debug=False)