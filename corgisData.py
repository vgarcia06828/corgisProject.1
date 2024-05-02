import json 

def main():
    with open(video_games.json) as corgis_data:
    
    
def list_games():
    """" "Title" """
    nam = ""
    y = 0
    for x in corgis_data 
        nam = corgis_data[y]["Title"]
    return nam
    
def game_pop():
    num = 0
    for x in corgis_data
        num = corgis_data["Metrics"]["Sales"]
    return num
    
def average_times():
    numb = 0
    avg = corgis_data["Length"]["All PlayStyles"]["Average"]
    for num in corgis_data
        avg = avg+num 
    avg = avg /len(numb)
    return avg
    
def popgame_2004(year):
    """Return the game with the higest sales in one year."""
    with open('video_games.json') as corgis_data:
        years = json.load(corgis_data)
    highest=0
    name = ""
    for x in year:
        if x["Release"]["Year"] == year:
            if x["Metrics"]["Sales"] > highest:
                highest = x["Metrics"]["Sales"]
                name = x["Title"]
    return name
    
def alphabetically_games():
    """Return all games and their average hours."""
    with open('video_games.json') as corgis_data:
    first = corgis_data[0]["Title"]
    for a in corgis_data[0]["Title"]:
        if a["Title"] < first:
            first = a["Title"]
    return first
    
def format_dict_as_graph_points(data)
    graph_points = ""
    for key in data:
    graph_points = graph_points + Markup('{y: ' + str(data[key])} + ', label: "' + key + '"}, ')
    graph_points = graph_points[:-2]
    return graph_points
    
"""note: remember to make a return that says wether or not the chosen game is the sequel to another game (hint: it should respond with true or false)"""
"""add what the producers are, and who produced them. """
if __name__ == '__main__':
    main()