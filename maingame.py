import time
import math
import webbrowser
from location import *
from locations import *
from functions import *
from story import *

while game_on == False:
    start = input("Turn game on?: ")
    if start == "yes":
        print("Gaming.")
        game_on = True
    else:
        print("Next time, play gaming.")
        game_on = "ended"
        break

while game_on == True:
    if ending_condition == True:
        game_on = "ended"
        break
    repeated_action(x, y, newx, newy, wall_counter)
    
