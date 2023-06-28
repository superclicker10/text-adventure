import time
import random
import webbrowser
from location import *
from locations import *
from wallmessages import *
from books import *

restricted_pos = ["01", "02", "03", "04", "15", "20", "21", "22", "24", "33"]
book_num = random.randint(1, 1000)
action = None
n = 1
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
lobby_wall = bookshelf_wall = one_one_wall_done = one_two_wall_done = one_three_wall_done = lectern_wall_done = False
lobby_wall_backup = bookshelf_wall_backup = one_one_wall_backup = one_two_wall_backup = one_three_wall_backup = lectern_room_wall_backup = 0



def time_check():
    global n
    n = float(input("How long do you want the text delay to be? (1 at default, range from 0.5 to 2): "))
    if n < 0.5:
        print("Delay set to min value (0.5)")
        time.sleep(n)
        n = 0.5
    elif n > 2:
        print("Delay set to max value (2)")
        time.sleep(n)
        n = 2
    else:
        print("Delay set to "+str(n)+"!")
        time.sleep(n)
    return n






def lobby_sequence():
    global room
    room = "lobby"
    print("You are in a dark room.")
    time.sleep(n)
    print("There is a passage to the right of you.")
    time.sleep(n)
    print("It looks to contain a bookshelf.")
    time.sleep(n)





def book_room():
    global room
    room = "book_room"
    print("There is a bookshelf to your east edge.")
    time.sleep(n)
    print("A door is in front of you at your north edge.")
    time.sleep(n)
    print("There is a large hole at your south-east.")   

def bookshelf_sequence():
    print("It's a bookshelf.")
    time.sleep(n)
    print("If you examined it, there may be more to it.")

def corner_hole():
    print("The infinite hole.")
    time.sleep(n)

def book_room_door():
    print("There is a door leading to your north (+y) direction leading to a long corridor.")
    time.sleep(n)

def book_room_examine(obj_examine):
    if obj_examine == "bookshelf":
        print("There are only a few books on this moldy-looking bookshelf.")
        time.sleep(n)
        print("You turn a few pages inside some, but there appears to be random words scattered across the pages.")
        time.sleep(n)
        print("You could take a book, but you aren't sure what use it would serve.")
        time.sleep(n)
    elif obj_examine == "hole":
        print("You look down the hole.")
        time.sleep(n)
        print("It goes on for miles and miles, with a calling inside your head telling you something will be at the bottom.")
        time.sleep(n)
    elif obj_examine == "door":
        print("The door is slightly ajar.")
        time.sleep(n)
        print("You see a corridor ahead of you that is longer than the confined spaces you are in.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)
        
def book_room_door_interact(one_one_door_interact_state):
    if one_one_door_interact_state == False:
        print("You open the door wider, giving you a clear view of the corridor ahead.")
        time.sleep(n)
        print("Even though you already could've gone through it.")
        time.sleep(n)
    else:
        print("You close the door back to where it was originally.")
        time.sleep(n)

def book_room_bookshelf(bookshelf_interact_state):
    if bookshelf_interact_state == False:
        print("You take a book from one of the shelves, hoping it might be useful.")
        time.sleep(n)
        if book_num <= 25:
            add_inventory("fish book")
        elif book_num == 1000:
            add_inventory("wall lore book")
        else:
            add_inventory("book")
            time.sleep(n)
        bookshelf_interact_state = True
        return bookshelf_interact
    elif inventory == []:
        print("You take another book from one of the shelves, hoping it might be useful.")
        time.sleep(1)
        add_inventory("book")
    else:
        print("You have no need for another book.")
        time.sleep(n)

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
    if room == "lobby" or room == "book_room" or room == "one_one_corridor" or room == "one_two_corridor" or room == "one_three_lobby":
        print("There is nothing here to use the book on.")
    elif room == "lectern_room":
        print("Reading book at the lectern...")
        time.sleep(2)
        book()

def fish_book_use(room):
    if room == "lobby" or room == "book_room" or room == "one_one_corridor" or room == "one_two_corridor" or room == "one_three_lobby":
        print("There is nothing here to use the book on.")
    elif room == "lectern_room":
        print("Reading fish book at the lectern...")
        time.sleep(2)
        fish_book()

def wall_book_use(room):
    if room == "lobby" or room == "book_room" or room == "one_one_corridor" or room == "one_two_corridor" or room == "one_three_lobby":
        print("There is nothing here to use the book on.")
    elif room == "lectern_room":
        print("Reading wall lore book at the lectern...")
        time.sleep(2)
        wall_lore_book()   
        

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
    time.sleep(n)
    print("There is a door ahead of you by 2 spaces.")
    time.sleep(n)
    print("The door you came through is behind you.")
    time.sleep(n)
    print("There is no sign of anything useful in this space.")
    time.sleep(n)

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
        time.sleep(n)
    elif obj_examine == "wall":
        print("These are unusually thick stone walls.")
        time.sleep(n)
        print("You see no way to exit as it is.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)

def one_one_southedge():
    print("This is the door at your south edge.")
    time.sleep(n)
    print("It leads back to the bookshelf room you just came from.")
    time.sleep(n)




def one_two_corridor():
    global room
    room = "one_two_corridor"
    print("You are further along in the corridor.")
    time.sleep(n)
    print("The door is behind you by another space.")
    time.sleep(n)
    print("There is a door leading to a bigger area north of you.")
    time.sleep(n)

def one_two_wall():      
    global wall_counter
    global one_two_wall_done
    global one_two_wall_backup
    global general_backup
    if one_two_wall_done == False:
        one_two_wall_backup = general_backup = wall_counter
        wall_message_check(one_two_wall_backup)
        wall_counter = wall_counter + 1
    else:
        wall_message_check(one_two_wall_backup)
    one_two_wall_done = True
    return wall_counter, one_two_wall_done

def one_two_door():
    if one_two_door_state == False:
        print("You open the door wider.")
        time.sleep(n)
        print("You can see a big room full of side rooms and posts in the middle.")
        time.sleep(n)
        print("It looks intriguing.")
        time.sleep(n)
    else:
        print("You close the door back to where it was originally.")
        time.sleep(n)
        one_two_door_interact = False
        return door_interact

def one_two_north_edge():
    print("A door that leads to another room.")
    time.sleep(n)

def one_two_corridor_examine(obj_examine):
    if obj_examine == "door":
        print("This is a door much like the last one.")
        time.sleep(n)
        print("But this one is a little grander than that.")
        time.sleep(n)
        print("And it seems to lead somewhere more grandiose than the last.")
        time.sleep(n)
    else:
        print("You can't examine that.")




def one_three_lobby():
    global room
    room = "one_three_lobby"
    print("You are through the door into the big room.")
    time.sleep(n)
    print("It is expansive, with many extra corridors going to different places.")
    time.sleep(n)
    print("There are many things to do here.")
    time.sleep(n)

def one_three_wall():
    global wall_counter
    global one_three_wall_done
    global lectern_room_wall_backup
    global general_backup
    if one_three_wall_done == False:
        one_three_wall_backup = general_backup = wall_counter
        wall_message_check(one_three_wall_backup)
        wall_counter = wall_counter + 1
    else:
        wall_message_check(one_three_wall_backup)
    one_three_wall_done = True
    return wall_counter, one_three_wall_done

def one_three_lobby_examine(obj_examine):
    if obj_examine == "wall":
        print("It's a wall.")
        time.sleep(n)
    elif obj_examine == "door":
        print("Perhaps you could get a better view of the door from the previous room.")
        time.sleep(n)
    else:
        print("You can't examine that.")

def one_three_eastedge():
    print("There is a foggy, mysterious room to your east.")
    time.sleep(n)

def one_three_southedge():
    print("It's a door, much like the last one you found.")
    time.sleep(n)





def lectern_room():
    global room
    room = "lectern_room"
    print("You move to a solitary room.")
    time.sleep(n)
    print("There is a lectern in the corner.")
    time.sleep(n)
    print("Maybe you could read those books from the bookshelf on it.")
    time.sleep(n)
    print("(This is the end of v0.1.4 room content, but there may still be more to do in previous rooms!)")
    time.sleep(n)
    

def lectern_wall():
    global wall_counter
    global lectern_wall_done
    global lectern_room_wall_backup
    global general_backup
    if lectern_wall_done == False:
        lectern_room_wall_backup = general_backup = wall_counter
        wall_message_check(lectern_room_wall_backup)
        wall_counter = wall_counter + 1
    else:
        wall_message_check(lectern_room_wall_backup)
    lectern_wall_done = True
    return wall_counter, lectern_wall_done

def lectern_room_examine(obj_examine):
    if obj_examine == "lectern":
        print("This is a very old, yet somehow very clean lectern.")
        time.sleep(n)
        print("Maybe this lectern lets you read some of the books from that bookshelf properly.")
        time.sleep(n)
    elif obj_examine == "wall":
        print("It's. A. Wall.")
        time.sleep(n)

def lectern_interact():
    print("You can't pick up the lectern. It's too heavy.")
    time.sleep(n)
    print("Perhaps using the book on it will yield a different result.")
    time.sleep(n)




def one_four():
    global room
    room = "one_four"
    print("You have a better view of this huge room now.")
    time.sleep(n)
    print("There is a wide and long corridor ending at a singular room at the end.")
    time.sleep(n)
    print("To your left there is a door that looks unbreachable, but does look like it can be opened somehow.")
    time.sleep(n)
    print("(This is the end of v0.1.4 room content, but there may still be more to do in previous rooms!)")
    time.sleep(n)

def one_four_westedge():
    print("A huge sliding door.")
    time.sleep(n)

def one_four_examine(obj_examine):
    if obj_examine == "door":
        print("This is a huge door, made of an undiscernable metal.")
        time.sleep(n)
        print("It looks like it can be opened using a remote system somehow.")
        time.sleep(n)
        print("Maybe there is some sort of switch to open the door somewhere.")
        time.sleep(n)




def oob(x, y, newx, newy):
    if newx <= -1 or newy <= -1:
        print("All negative co-ordinates are out of bounds.")
        time.sleep(n)

def move(x, y, room):
    global newx
    global newy
    move = input("Where are you moving to? (+x, -x, +y, -y, edge): ")
    if move == "+x":
        x_backup = x
        newx = x + 1
        if str(newx)+str(newy) in restricted_pos:
            print("This position is restricted.")
            time.sleep(n)
            newx = x_backup
        else:
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
            time.sleep(n)
            newx = x_backup
        else:
            newy = y
            return x, y, newx, newy
    elif move == "+y":
        y_backup = y
        newy = y + 1
        if str(newx)+str(newy) in restricted_pos:
            print("This position is restricted.")
            time.sleep(n)
            newy = y_backup
        else:
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
            time.sleep(n)
            newy = y_backup
        else:
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
        elif room == "one_three_lobby":
            edge = input("East edge, or south edge?: ")
            if edge == "east":
                one_three_eastedge()
            elif edge == "south":
                one_three_southedge()
        elif room == "one_four":
            one_four_westedge()
        else:
            print("There are no edges to move to in this room.")
            time.sleep(n)

def examine(room):
    if room == "lobby":
        print("There is nothing to examine in this room.")
        time.sleep(n)
    elif room == "book_room":
        obj_examine = input("What object would you like to examine?: ")
        book_room_examine(obj_examine)
    elif room == "one_one_corridor":
        obj_examine = input("What object would you like to examine?: ")
        one_one_corridor_examine(obj_examine)
    elif room == "one_two_corridor":
        obj_examine = input("What object would you like to examine?: ")
        one_two_corridor_examine(obj_examine)
    elif room == "one_three_lobby":
        obj_examine = input("What object would you like to examine?: ")
        one_three_lobby_examine(obj_examine)
    elif room == "one_four":
        obj_examine = input("What object would you like to examine?: ")
        one_four_examine(obj_examine)
    elif room == "lectern_room":
        obj_examine = input("What object would you like to examine?: ")
        lectern_room_examine(obj_examine)

def interact(room):
    global wall_counter
    global lobby_wall
    global general_backup
    global lobby_wall_backup
    if room == "one_four":
        print("There is nothing to interact with in this room.")
        time.sleep(n)
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
        global one_one_door_interact_state
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
            time.sleep(n)
    elif room == "one_one_corridor":
        if obj_interact == "wall":
            one_one_wall()
        else:
            print("You can't interact with that.")
            time.sleep(n)
    elif room == "one_two_corridor":
        if obj_interact == "door":
            one_two_door()
        elif obj_interact == "wall":
            one_two_wall()
        else:
            print("You can't interact with that.")
            time.sleep(n)
    elif room == "one_three_lobby":
        if obj_interact == "wall":
            one_three_wall()
        else:
            print("You can't interact with that.")
            time.sleep(n)
    elif room == "lectern_room":
        if obj_interact == "wall":
            lectern_wall()
        elif obj_interact == "lectern":
            lectern_interact()
        else:
            print("You can't interact with that.")
            time.sleep(n)

def inventory_general():
    choice = input("View or drop item from inventory?: ")
    if choice == "view":
        print(inventory)
    elif choice == "drop":
        print(inventory)
        if inventory == []:
            print("You have nothing to drop.")
            time.sleep(n)
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
            time.sleep(n)
            break
        else:
            pass

def use(room):
    if inventory == []:
        print("You have nothing to use.")
        time.sleep(1)
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
    elif item == "fish book":
        fish_book_use(room)
    elif item == "wall lore book":
        wall_book_use(room)
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
        elif newx == 1 and newy == 3:
            one_three_lobby()
        elif newx == 1 and newy == 4:
            one_four()
        elif newx == 2 and newy == 3:
            lectern_room()
        break

def wall_message_check(general_backup):
    for x in range(0, 100):
        if x == general_backup:
            eval("wall_"+str(general_backup)+"()")
        else:
            pass
def repeated_action(x, y, newx, newy, wall_counter):
    global action
    print()
    room_check(x, y, newx, newy)
    x = newx
    y = newy
    print("Your co-ordinates are", str(x)+", "+str(y))
    action = input("What to do? (interact, move, use, examine, inventory): ")
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
    elif action == "stop":
        ending_condition = True
        game_on = "ended"
        return action
    else:
        print("You can't do that.")
    

while game_on == False:
    start = input("Turn game on?: ")
    if start == "yes":
        time_check()
        print("Enter 'stop' to stop the game.")
        time.sleep(2)
        game_on = True
    else:
        print("Next time, play gaming.")
        game_on = "ended"
        break

while game_on == True:
    if ending_condition == True:
        game_on = "ended"
        break
    elif action == "stop":
        game_on = "ended"
        break
    repeated_action(x, y, newx, newy, wall_counter)
    
