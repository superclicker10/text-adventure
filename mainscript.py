import time
import math
import webbrowser
from location import *
from locations import *
from wallmessages import *

restricted_pos = ["01", "02", "20", "21", "22"]
game_on = False
x, newx = 0, 0
y, newy = 0, 0
room = "lobby"
inventory = []
ending_condition = False
one_one_door_interact_state = False
bookshelf_interact_state = False
wall_counter = 0
general_backup = 0
lobby_wall = bookshelf_wall = one_one_wall_done = one_two_wall_done = False
lobby_wall_backup = bookshelf_wall_backup = one_one_wall_backup = one_two_wall_backup = 0





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
        
def book_room_door_interact(one_one_door_interact_state):
    if one_one_door_interact_state == False:
        print("You open the door wider, giving you a clear view of the corridor ahead.")
        time.sleep(1)
        print("Even though you already could've gone through it.")
        time.sleep(1)
    else:
        print("You close the door back to where it was originally.")
        time.sleep(1)

def book_room_bookshelf(bookshelf_interact_state):
    if bookshelf_interact_state == False:
        print("You take a book from one of the shelves, hoping it might be useful.")
        time.sleep(1)
        add_inventory("book")
        return bookshelf_interact
    elif inventory == []:
        print("You take another book from one of the shelves, hoping it might be useful.")
        time.sleep(1)
        add_inventory("book")
    else:
        print("You have no need for another book.")
        time.sleep(1)

def book_room_wall():
    global wall_counter
    global bookshelf_wall
    global bookshelf_wall_backup
    global general_backup
    if bookshelf_wall == False:
        bookshelf_wall_backup = general_backup = wall_counter
        wall_message_check(bookshelf_wall_backup)
        wall_counter = wall_counter + 1
    else:
        wall_message_check(bookshelf_wall_backup)
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
    global one_one_wall_backup
    global general_backup
    if one_one_wall_done == False:
        one_one_wall_backup = general_backup = wall_counter
        wall_message_check(one_one_wall_backup)
        wall_counter = wall_counter + 1
    else:
        wall_message_check(one_one_wall_backup)
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

def one_two_wall():      #ADD NEW WALL SYSTEM HERE
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

def one_two_door():
    if one_two_door_state == False:
        print("You open the door wider, giving you a clear view of the corridor ahead.")
        time.sleep(1)
        print("Even though you already could've gone through it.")
        time.sleep(1)
    else:
        print("You close the door back to where it was originally.")
        time.sleep(1)
        one_two_door_interact = False
        return door_interact






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
            time.sleep(1)
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
            time.sleep(1)
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
            time.sleep(1)
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
            time.sleep(1)
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
        elif room == "one_one_corridor":
            one_one_southedge()
        elif room == "one_two_corridor":
            one_two_northedge()
        else:
            print("There are no edges to move to in this room.")
            time.sleep(1)

def examine(room):
    if room == "lobby":
        print("There is nothing to examine in this room.")
        time.sleep(1)
    elif room == "book_room":
        obj_examine = input("What object would you like to examine?: ")
        book_room_examine(obj_examine)
    elif room == "one_one_corridor":
        obj_examine = input("What object would you like to examine?: ")
        one_one_corridor_examine(obj_examine)

def interact(room):
    global wall_counter
    global lobby_wall
    global general_backup
    global lobby_wall_backup
    obj_interact = input("What would you like to interact with?: ")
    if room == "lobby":
        if obj_interact == "wall":
            if lobby_wall == False:
                lobby_wall_backup = general_backup = wall_counter
                wall_message_check(lobby_wall_backup)
                wall_counter = wall_counter + 1
            else:
                wall_message_check(lobby_wall_backup)
            lobby_wall = True
            return lobby_wall, wall_counter
        else:
            print("You can't interact with that.")
            time.sleep(1)
    elif room == "book_room":
        global door_interact_state
        global bookshelf_interact_state
        if obj_interact == "door":
            book_room_door_interact(one_one_door_interact_state)
            if one_one_door_interact_state == True:
                one_one_door_interact_state == False
            else:
                one_one_door_interact_state = True
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
            time.sleep(1)
    elif room == "one_one_corridor":
        if obj_interact == "wall":
            one_one_wall()
        else:
            print("You can't interact with that.")
            time.sleep(1)
    elif room == "one_two_corridor":
        if obj_interact == "door":
            one_two_door()
        elif obj_interact == "wall":
            one_two_wall()
        else:
            print("You can't interact with that.")
            time.sleep(1)
            

def inventory_general():
    choice = input("View or drop item from inventory?: ")
    if choice == "view":
        print(inventory)
    elif choice == "drop":
        print(inventory)
        if inventory == []:
            print("You have nothing to drop.")
            time.sleep(1)
        else:
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

def use(room):
    if inventory == []:
        print("You have nothing to use.")
    else:
        print(inventory, "is your inventory.")
        time.sleep(1)
        item = input("What item would you like to use?: ")
        for x in inventory:
            if item == x:
                use_navigation(item, room)
                break
            else:
                continue
            
def use_navigation(item, room):
    if item == "book":
        book_use(room)
    else:
        print("You can't use that item.")
    

def room_check(x, y, newx, newy):
    for x in locations:
        posx = x.xpos
        posy = x.ypos
        if newx == 0 and newy == 0:
            lobby_sequence()
        elif newx == 1 and newy == 0:
            book_room()
        elif newx == 1 and newy == 1:
            one_one_corridor()
        elif newx == 1 and newy == 2:
            one_two_corridor()
        break

def wall_message_check(general_backup):
    for x in range(0, 100):
        if x == general_backup:
            eval("wall_"+str(general_backup)+"()")
        else:
            pass
def repeated_action(x, y, newx, newy, wall_counter):
    print()
    room_check(x, y, newx, newy)
    x = newx
    y = newy
    #print(wall_counter) for experiement purposes only
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
    elif action == "use":
        use(room)
    else:
        print("You can't do that.")
    

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
    
