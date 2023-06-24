from location import *
from locations import *
from functions import *

restricted_pos = ["01", "02", "20", "21", "22"]
game_on = False
x, newx = 0, 0
y, newy = 0, 0
room = "lobby"
inventory = []
ending_condition = False
door_interact_state = False
bookshelf_interact_state = False
wall_counter = 0
lobby_wall, bookshelf_wall, one_one_wall_done, one_two_wall_done = False, False, False, False

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

def book_room_wall():
    global wall_counter
    global bookshelf_wall
    print("You touch the wall again.")
    time.sleep(1)
    print("It's still cold.")
    time.sleep(1)
    if bookshelf_wall == False:
        wall_counter = wall_counter + 1
    bookshelf_wall = True
    return wall_counter, bookshelf_wall

def book_use(room):
    if room == "lobby" or room == "book_room" or room == "one_one_corridor":
        print("There is nothing here to use the book on.")

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

def one_one_wall():
    global wall_counter
    global one_one_wall_done
    print("You touch the wall again.")
    time.sleep(1)
    print("Why do you keep doing this?")
    time.sleep(1)
    if one_one_wall_done == False:
        wall_counter = wall_counter + 1
    one_one_wall_done = True
    return wall_counter, one_one_wall_done

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

def one_one_southedge():
    print("This is the door at your south edge.")
    time.sleep(1)
    print("It leads back to the bookshelf room you just came from.")
    time.sleep(1)

def one_two_corridor():
    global room
    room = "one_two_corridor"
    print("You are further along in the corridor.")
    time.sleep(1)
    print("The door is behind you by another space.")
    time.sleep(1)
    print("There is a door leading to a bigger area north of you.")
    time.sleep(1)

def one_two_wall():
    global wall_counter
    global one_two_wall_done
    print("You touch the wall again.")
    time.sleep(1)
    print("What are you getting out of this?")
    time.sleep(1)
    if one_two_wall_done == False:
        wall_counter = wall_counter + 1
    one_two_wall_done = True
    return wall_counter, one_two_wall_done
