import time
import math
import webbrowser
from location import *
from locations import *

restricted_pos = ["01", "20", "21"]
game_on = False
x, newx = 0, 0
y, newy = 0, 0
room = "lobby"

def lobby_sequence():
    global room
    room = "lobby"
    print("You are in a dark room.")
    time.sleep(1)
    print("There is a passage to the right of you.")
    time.sleep(1)
    print("It looks to contain a bookshelf.")
    time.sleep(1)

def book_room():
    global room
    room = "book_room"
    print("There is a bookshelf to your east edge.")
    time.sleep(1)
    print("A door is in front of you at your north edge.")
    time.sleep(1)
    print("There is a large hole at your south-east.")

def bookshelf_sequence():
    print("Test bookshelf")
    time.sleep(1)

def corner_hole():
    print("The infinite hole.")
    time.sleep(1)

def book_room_door():
    print("There is a door leading to your north (+y) direction leading to a long corridor.")
    time.sleep(1)

def book_room_examine(obj_examine):
    if obj_examine == "bookshelf":
        print("There are only a few books on this moldy-looking bookshelf.")
        time.sleep(1)
        print("You turn a few pages inside some, but there appears to be random words scattered across the pages.")
        time.sleep(1)
        print("You could take a book, but you aren't sure what use it would serve.")
        time.sleep(1)
    elif obj_examine == "hole":
        print("You look down the hole.")
        time.sleep(1)
        print("It goes on for miles and miles, with a calling inside your head telling you something will be at the bottom.")
        time.sleep(1)
    elif obj_examine == "door":
        print("The door is slightly ajar.")
        time.sleep(1)
        print("You see a corridor ahead of you that is longer than the confined spaces you are in.")
        time.sleep(1)
    else:
        print("You can't examine that.")
        time.sleep(1)

def one_one_corridor():
    global room
    room = "one_one_corridor"
    print("You are in a corridor.")
    time.sleep(1)
    print("There is a door ahead of you by 2 spaces.")
    time.sleep(1)
    print("The door you came through is behind you.")
    time.sleep(1)
    print("There is no sign of anything useful in this space.")
    time.sleep(1)

def one_one_corridor_examine(obj_examine):
    if obj_examine == "door":
        print("Going back to the last room would allow you to get a better look at the door.")
        time.sleep(1)
    elif obj_examine == "wall":
        print("These are unusually thick stone walls.")
        time.sleep(1)
        print("You see no way to exit at it is.")
        time.sleep(1)
    else:
        print("You can't examine that.")
        time.sleep(1)

def oob(x, y, newx, newy):
    if newx <= -1 or newy <= -1:
        print("All negative co-ordinates are out of bounds.")
        time.sleep(1)

def move(x, y, room):
    global newx
    global newy
    move = input("Where moving to? (+x, -x, +y, -y, edge): ")
    if move == "+x":
        x_backup = x
        newx = x + 1
        if str(newx)+str(newy) in restricted_pos:
            print("This position is restricted.")
            newx = x_backup
        else:
            #print("This position is restricted.")
            newy = y
            return x, y, newx, newy
    elif move == "-x":
        x_backup = x
        newx = x - 1
        if newx <= -1:
            oob(x, y, newx, newy)
            newx = x_backup
        elif str(newx)+str(newy) in restricted_pos:
            print("This position is restricted.")
            newx = x_backup
        else:
            #print("This position is restricted.")
            newy = y
            return x, y, newx, newy
    elif move == "+y":
        y_backup = y
        newy = y + 1
        if str(newx)+str(newy) in restricted_pos:
            print("This position is restricted.")
            newy = y_backup
        else:
            #print("This position is restricted.")
            newx = x
            return x, y, newx, newy
    elif move == "-y":
        y_backup = y
        newy = y - 1
        if newy <= -1:
            oob(x, y, newx, newy)
            newy = y_backup
        elif str(newx)+str(newy) in restricted_pos:
            print("This position is restricted.")
            newy = y_backup
        else:
            #print("This position is restricted.")
            newx = x
            return x, y, newx, newy
    elif move == "edge":
        if room == "book_room":
            edge = input("North edge, east edge, or south-east edge?: ")
            if edge == "north":
                book_room_door()
            elif edge == "east":
                bookshelf_sequence()
            elif edge == "south-east":
                corner_hole()
        else:
            print("There are no edges to move to in this room.")

def examine(room):
    if room == "lobby":
        print("There is nothing to examine in this room.")
    elif room == "book_room":
        obj_examine = input("What object would you like to examine?: ")
        book_room_examine(obj_examine)
    elif room == "one_one_corridor":
        obj_examine = input("What object would you like to examine?: ")
        one_one_corridor_examine(obj_examine)
    

def room_check(x, y, newx, newy):
    for x in locations:
        posx = x.xpos
        posy = x.ypos
        if newx == 0 and newy == 0:
            lobby_sequence()
            break
        elif newx == 1 and newy == 0:
            book_room()
            break
        elif newx == 1 and newy == 1:
            one_one_corridor()
            break

"""
def first_action(x, y, counter):
    room_check(x, y, 0, 0)
    action = input("What do? (interact, move, use, examine): ")
    if action == "move":
        move(x, y, room)
"""
def repeated_action(x, y, newx, newy):
    room_check(x, y, newx, newy)
    x = newx
    y = newy
    print("Your co-ordinates are", str(x)+", "+str(y))
    action = input("What do? (interact, move, use, examine): ")
    if action == "move":
        move(x, y, room)
    elif action == "examine":
        examine(room)
    

while game_on == False:
    start = input("Turn game on?: ")
    if start == "yes":
        print("Gaming.")
        game_on = True
    else:
        print("Next time, play gaming.")

while game_on == True:
    repeated_action(x, y, newx, newy)
    """
    try:
        repeated_action(x, y, newx, newy)
    except NameError:
        print("The game works, don't worry bout it.")
        x = newx
        y = newy
    """
    
