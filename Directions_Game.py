""" COURSE 2: Built-in data structures - Part3 (dictionaries) """
""" Homework """


###################
### 1. Game Map ###

# Create a set of instructions helping the player find their way through a game,
# by replicating the map provided in the course. Depending on where the player
# is currently located, the program first describes the current location and then
# reveals the directions in which the player can move further. The possible directions
# should be expressed in geographical coordinates (N, S, E, W) + Q (the option to quit the
# game is always available). The starting position is the Road.

# Tip: - store the locations along with their position numbers in a dictionary 
#      - store the possible exists for each location in a list of dictionaries ;-)


locations = {"1":"Road","5":"Forest","3":"Building","2":"Hill","4":"Valley"}
directions = {"Road": ["N", "S", "E", "W", "Q"],"Forest":["S","Q"],"Building":["W","Q"],"Valley":["N","W","Q"],"Hill":["N","Q"]}
start = input("Please insert your location(1 for Road,2 for Hill,3 for Building,4 for Valley,5 for Forest): ")
loc = start
def startgame(): 
    global loc
    name = locations[loc]
    print(name)
    newloc = input("You can move here: " + str(directions[name]) + " .Please select your choice ")
    if newloc == "Q":
        print("Game is over.")
    elif newloc == "W" and name == "Road":
        loc = "2";
        startgame();
    elif newloc == "W" and name == "Building":
        loc = "1";
        startgame();
    elif newloc == "W" and name == "Valley":
        loc = "2";
        startgame();
    elif newloc == "S" and name == "Road":
        loc = "4";
        startgame();
    elif newloc=="S" and name =="Forest":
        loc = "1";
        startgame();
    elif newloc == "E" and name == "Road":
        loc = "3";
        startgame();
    elif newloc == "N" and name == "Road":
        loc ="5";
        startgame();
    elif newloc == "N" and name == "Valley":
        loc="1";
        startgame();
    elif newloc == "N" and name == "Hill":
        loc="5";
        startgame();
    else:
        print("This is not a valid direction. Please choose again")
        startgame();
 
startgame();
# Instructions: First choose your location by using an assigned number: 1,2,3,4,5. The game will then show you alternative directions that you can take 
