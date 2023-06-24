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
inventory = []
ending_condition = False
door_interact_state = False
bookshelf_interact_state = False

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
    print("It's a bookshelf.")
    time.sleep(1)
    print("If you examined it, there may be more to it.")

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
        
def book_room_door_interact(door_interact_state):
    if door_interact_state == False:
        print("You open the door wider, giving you a clear view of the corridor ahead.")
        time.sleep(1)
        print("Even though you already could've gone through it.")
        time.sleep(1)
    else:
        print("You close the door back to where it was originally.")
        time.sleep(1)
        door_interact = False
        return door_interact

def book_room_bookshelf(bookshelf_interact_state):
    if bookshelf_interact_state == False:
        print("You take a book from one of the shelves, hoping it might be useful.")
        time.sleep(1)
        add_inventory("book")
        return bookshelf_interact
    else:
        print("You have no need for another book.")
        time.sleep(1)

def book_room_wall(wall_counter):
    print("You touch the wall again.")
    time.sleep(1)
    print("It's still cold.")
    time.sleep(1)

def hole_ending_sequence():
    global ending_condition
    print("You jump in the hole, falling forever and ever.")
    time.sleep(3)
    print("ENDING 1 - FALLING INTO THE DEPTHS")
    time.sleep(2)
    ending_condition = True

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

def one_one_wall(wall_counter):
    print("You touch the wall again.")
    time.sleep(1)
    print("Why do you keep doing this?")
    time.sleep(1)
    wall_counter = wall_counter + 1
    return wall_counter

def one_one_corridor_examine(obj_examine):
    if obj_examine == "door":
        print("Going back to the last room would allow you to get a better look at the door.")
        time.sleep(1)
    elif obj_examine == "wall":
        print("These are unusually thick stone walls.")
        time.sleep(1)
        print("You see no way to exit as it is.")
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

def interact(room):
    obj_interact = input("What would you like to interact with?: ")
    if room == "lobby":
        if obj_interact == "wall":
            print("You touch the wall. It's cold.")
            time.sleep(1)
        else:
            print("You can't interact with that.")
    elif room == "book_room":
        global door_interact_state
        global bookshelf_interact_state
        if obj_interact == "door":
            book_room_door_interact(door_interact_state)
            if door_interact_state == True:
                door_interact_state == False
            else:
                door_interact_state = True
        elif obj_interact == "bookshelf":
            book_room_bookshelf(bookshelf_interact_state)
            bookshelf_interact_state = True
            return bookshelf_interact_state
        elif obj_interact == "hole":
            hole_ending_sequence()
        elif obj_interact == "wall":
            book_room_wall()
        else:
            print("You can't interact with that.")
    elif room == "one_one_corridor":
        if obj_interact == "wall":
            one_one_wall()
            

def inventory_general():
    choice = input("View or drop item from inventory?: ")
    if choice == "view":
        print(inventory)
    elif choice == "drop":
        item = input("What item would you like to drop?: ")
        drop_item(item)

def add_inventory(item):
    if len(inventory) == 3:
        print("You cannot add this item, as you haven't enough inventory space.")
        time.sleep(1)
        print("Drop an item, or use one first.")
        time.sleep(1)
    else:
        print("Added", item, "to inventory!")
        inventory.append(item)

def drop_item(item):
    for x in inventory:
        if item == x:
            inventory.remove(item)
            print("Dropped", item, "from inventory!")
            time.sleep(1)
            break
        else:
            pass
    print("You do not have this item.")

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
    action = input("What do? (interact, move, use, examine, inventory): ")
    if action == "move":
        move(x, y, room)
    elif action == "examine":
        examine(room)
    elif action == "interact":
        interact(room)
    elif action == "inventory":
        inventory_general()
    

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
    repeated_action(x, y, newx, newy)
    """
    try:
        repeated_action(x, y, newx, newy)
    except NameError:
        print("The game works, don't worry bout it.")
        x = newx
        y = newy
    """
    
