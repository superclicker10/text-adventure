import time
import random
import webbrowser
import os
from location import *
from locations import *
from wallmessages import *
from books import *

restricted_pos = ["01", "02", "03", "04", "05", "06", "07", "18", "20", "21", "22", "27", "33", "37", "44", "45", "46"]
book_num = random.randint(1, 100)
action = None
n = 1
count = 0
game_on = False
x = 0
newx = 0
y = 0
newy = 0
room = "lobby"
inventory = []
ending_condition = False
one_one_door_interact_state = False
bookshelf_interact_state = False
wall_counter = 0
general_backup = 0
one_two_door_interact = False
one_seven_switch_done = False
lobby_wall = bookshelf_wall = one_one_wall_done = one_two_wall_done = one_three_wall_done = one_seven_wall_done = lectern_wall_done = two_six_wall_done= False
lobby_wall_backup = bookshelf_wall_backup = one_one_wall_backup = one_two_wall_backup = one_three_wall_backup = one_seven_wall_backup = lectern_room_wall_backup = two_six_wall_backup = 0
zero_four_wall_done = three_four_wall_done = three_six_wall_done = False
zero_four_wall_backup = three_four_wall_backup = three_six_wall_backup = 0
game_values = [restricted_pos, book_num, n, game_on, x, newx, y, newy, room, inventory, ending_condition, one_one_door_interact_state, bookshelf_interact_state, wall_counter, general_backup, one_two_door_interact, one_seven_switch_done]
game_values_string = ["restricted_pos", "book_num", "n", "game_on", "x", "newx", "y", "newy", "room", "inventory", "ending_condition", "one_one_door_interact_state", "bookshelf_interact_state", "wall_counter", "general_backup", "one_two_door_interact", "one_seven_switch_done"]

def time_check():
    global n
    try:
        n = float(input("How long do you want the text delay to be? (1 at default, range from 0.5 to 2): "))
    except ValueError:
        print("n set to 1.")
        time.sleep(n)
    else:
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






def lobby():
    global room
    room = "lobby"
    print("You are in a dark room.")
    time.sleep(n)
    print("There is a passage to the right of you.")
    time.sleep(n)
    print("It looks to contain a bookshelf.")
    time.sleep(n)
    return room

def lobby_interact(obj_interact):
    global lobby_wall
    global lobby_wall_backup
    global wall_counter
    global general_backup
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





def zero_four():
    global room
    room = "zero_four"
    print("You are inside the first room you unlocked with the switch.")
    time.sleep(n)
    print("There is a note on the ground, scruffy and torn with age.")
    time.sleep(n)
    print("It might give you a clue toward the locations of the other switches.")
    time.sleep(n)
    return room

def zero_four_interact(obj_interact):
    global inventory
    if obj_interact == "note":
        if "note" not in inventory:
            print("You pick up the note.")
            time.sleep(n)
            add_inventory("note")
        else:
            print("You have already picked up the note.")
    elif obj_interact == "wall":
        global wall_counter
        global zero_four_wall_done
        global zero_four_wall_backup
        global general_backup
        if zero_four_wall_done == False:
            one_one_wall_backup = general_backup = wall_counter
            wall_message_check(zero_four_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(zero_four_wall_backup)
        zero_four_wall_done = True
        return wall_counter, zero_four_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def note_use():
    print("'Three switches - '")
    time.sleep(n)
    print("'(1, 7)'")
    time.sleep(n)
    print("'(4, '")
    time.sleep(n)
    print("'(5, '")
    time.sleep(n)
    print("Some of the note is torn, missing some of the coordinates to the other switches.")
    time.sleep(n)

def zero_four_examine(obj_examine):
    if obj_examine == "note":
        print("A torn note with some writing on it.")
        time.sleep(n)
        print("It might help you to find the locations of some other switches for the other doors.")
        time.sleep(n)
    else:
        print("You can't examine that.")



        
def book_room():
    global room
    room = "book_room"
    print("There is a bookshelf to your east edge.")
    time.sleep(n)
    print("A door is in front of you at your north edge.")
    time.sleep(n)
    print("There is a large hole at your south-east.")
    return room

def book_room_edges():
    edge = input("Which edge to move to? (north, south-east, east): ")
    if edge == "north":
        print("There is a door leading to your north (+y) direction leading to a long corridor.")
        time.sleep(n)
    elif edge == "south-east":
        print("The infinite hole.")
        time.sleep(n)
    elif edge == "east":
        print("It's a bookshelf.")
        time.sleep(n)
        print("If you examined it, there may be more to it.")
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
        
def book_room_interact(obj_interact):
    global one_one_door_interact_state
    global bookshelf_interact_state
    global repeat_book
    if obj_interact == "door":
        if one_one_door_interact_state == False:
            print("You open the door wider, giving you a clear view of the corridor ahead.")
            time.sleep(n)
            print("Even though you already could've gone through it.")
            time.sleep(n)
            one_one_door_interact_state = True                      #TEST THIS FUNCTIONALITY
        else:
            print("You close the door back to where it was originally.")
            time.sleep(n)
            one_one_door_interact_state = False
    elif obj_interact == "bookshelf":
        if bookshelf_interact_state == False and (("book" not in inventory) or ("fish book" not in inventory) or ("wall lore book" not in inventory)):
            print("You take a book from one of the shelves, hoping it might be useful.")
            time.sleep(n)
            if book_num <= 10:
                add_inventory("fish book")
            elif book_num >= 99:
                add_inventory("wall lore book")
            else:
                add_inventory("book")
                time.sleep(n)
            bookshelf_interact_state = True
            return bookshelf_interact
        elif bookshelf_interact_state == True:
            for x in inventory:
                if x == "book" or x == "fish book" or x == "wall lore book":
                    print("You have no need for another book.")
                    time.sleep(n)
                    bookshelf_interact_state = False
        else:
            print("You have no need for another book.")
            time.sleep(n)
    elif obj_interact == "wall":
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
    else:
        print("You can't interact with that.")
        time.sleep(n)

def book_use(room):
    if room == "lectern_room":
        print("Reading book at the lectern...")
        time.sleep(2)
        book()
    else:
        print("There is nothing here to use the book on.")
        time.sleep(n)

def fish_book_use(room):
    if room == "lectern_room":
        print("Reading fish book at the lectern...")
        time.sleep(2)
        fish_book()
    else:
        print("There is nothing here to use the book on.")
        time.sleep(n)

def wall_book_use(room):
    if room == "lectern_room":
        print("Reading wall lore book at the lectern...")
        time.sleep(2)
        wall_lore_book()
    else:
        print("There is nothing here to use the book on.")
        time.sleep(n)  
        

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
    return room

def one_one_corridor_interact(obj_interact):
    if obj_interact == "wall":
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
    else:
        print("You can't interact with that.")
        time.sleep(n)
        
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

def one_one_corridor_edge():
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
    return room

def one_two_corridor_interact(obj_interact):
    global one_two_door_interact
    if obj_interact == "door":
        if one_two_door_interact == False:
            print("You open the door wider.")
            time.sleep(n)
            print("You can see a big room full of side rooms and posts in the middle.")
            time.sleep(n)
            print("It looks intriguing.")
            time.sleep(n)
            one_two_door_interact = True
        else:
            print("You close the door back to where it was originally.")
            time.sleep(n)
            one_two_door_interact = False
            return one_two_door_interact
    elif obj_interact == "wall":
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
    else:
        print("You can't interact with that.")
        time.sleep(n)

def one_two_corridor_edge():
    print("A door that leads to another room to your north.")
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




def one_three():
    global room
    room = "one_three"
    print("You are through the door into the big room.")
    time.sleep(n)
    print("It is expansive, with many extra corridors going to different places.")
    time.sleep(n)
    print("There are many things to do here.")
    time.sleep(n)
    return room

def one_three_interact(obj_interact):
    if obj_interact == "wall":
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
    else:
        print("You can't interact with that.")
        time.sleep(n)

def one_three_examine(obj_examine):
    if obj_examine == "wall":
        print("It's a wall.")
        time.sleep(n)
    elif obj_examine == "door":
        print("Perhaps you could get a better view of the door from the previous room.")
        time.sleep(n)
    else:
        print("You can't examine that.")

def one_three_edges():
    edge = input("Which edge to move to? (east, south): ")
    if edge == "east":
        print("There is a foggy, mysterious room to your east.")
        time.sleep(n)
    elif edge == "south":
        print("It's a door to your south, much like the last one you found.")
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
    return room

def one_four_edge():
    print("A huge sliding door to your west.")
    time.sleep(n)

def one_four_examine(obj_examine):
    if obj_examine == "door":
        print("This is a huge door, made of an undiscernable metal.")
        time.sleep(n)
        print("It looks like it can be opened using a remote system somehow.")
        time.sleep(n)
        print("Maybe there is some sort of switch to open the door somewhere.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)




def one_five():
    global room
    room = "one_five"
    print("You're now further along this now very long corridor.")
    time.sleep(n)
    print("To your left is another door like the one south of you.")
    time.sleep(n)
    print("To your north you are starting to see more corridors in the distance.")
    time.sleep(n)
    return room

def one_five_edge():
    print("A huge sliding door to your west.")
    time.sleep(n)

def one_five_examine(obj_examine):
    if obj_examine == "door":
        print("This is another huge door like the one south of you.")
        time.sleep(n)
        print("There seems to be another one to your north as well.")
        time.sleep(n)
        print("Perhaps there'll be a switch for them somewhere.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)



def one_six():
    global room
    room = "one_six"
    print("To your west is the most northern door of the three.")
    time.sleep(n)
    print("To your north is a strange space with an object in it.")
    time.sleep(n)
    print("Perhaps you should investigate.")
    time.sleep(n)
    return room

def one_six_examine(obj_examine):
    if obj_examine == "door":
        print("It's a door, just like the two south of you.")
        time.sleep(n)
        print("Another switch may be required.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)

def one_six_edges():
    edge = input("Which edge to move to? (west, north): ")
    if edge == "west":
        print("Another door to your west.")
        time.sleep(n)
    elif edge == "north":
        print("A solitary room to your north which contains a strange object.")
        time.sleep(n)
        print("Perhaps it can help you open those doors.")
        time.sleep(n)



def one_seven():
    global room
    room = "one_seven"
    print("You are in a room bulging from the end of the left space, in the big room.")
    time.sleep(n)
    print("There is a strange lever in the room.")
    time.sleep(n)
    print("(This is on the border of v0.2.1 content, but there may still be more to do in previous rooms!)")
    time.sleep(n)
    return room

def one_seven_examine(obj_examine):
    if obj_examine == "lever":
        print("A fairly big mechanical lever.")
        time.sleep(n)
        print("It may help you to open one of the doors to your south-west.")
        time.sleep(n)

def one_seven_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global one_seven_wall_done
        global one_seven_wall_backup
        global general_backup
        if one_seven_wall_done == False:
            one_seven_wall_backup = general_backup = wall_counter
            wall_message_check(one_seven_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(one_seven_wall_backup)
        one_seven_wall_done = True
        return wall_counter, one_seven_wall_done
    elif obj_interact == "lever":
        global one_seven_switch_done
        if one_seven_switch_done == False:
            print("You turn the lever.")
            time.sleep(n)
            print("With a crank, and a loud noise, something opens behind you.")
            time.sleep(n)
            print("Perhaps you should go investigate.")
            time.sleep(n)
            one_seven_switch_done = True
            restricted_pos.remove("04")
        else:
            print("You have already turned the lever.")
            time.sleep(n)
    else:
        print("You can't interact with that.")
        


        
def lectern_room():
    global room
    room = "lectern_room"
    print("You move to a solitary room.")
    time.sleep(n)
    print("There is a lectern in the corner.")
    time.sleep(n)
    print("Maybe you could read those books from the bookshelf on it.")
    time.sleep(n)
    return room

def lectern_room_interact(obj_interact):
    if obj_interact == "wall":
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
    elif obj_interact == "lectern":
        print("You can't pick up the lectern. It's too heavy.")
        time.sleep(n)
        print("Perhaps using the book on it will yield a different result.")
        time.sleep(n)
    else:
        print("You can't interact with that.")
        time.sleep(n)

def lectern_room_examine(obj_examine):
    if obj_examine == "lectern":
        print("This is a very old, yet somehow very clean lectern.")
        time.sleep(n)
        print("Maybe this lectern lets you read some of the books from that bookshelf properly.")
        time.sleep(n)
    elif obj_examine == "wall":
        print("It's. A. Wall.")
        time.sleep(n)




def two_four():
    global room
    room = "two_four"
    print("You are further along in the big central room.")
    time.sleep(n)
    print("You now have view of three locked rooms a few units to your left.")
    time.sleep(n)
    print("They all have identical doors.")
    time.sleep(n)
    return room

def two_four_edge():
    print("There is a foggy, mysterious room to your south.")
    time.sleep(n)



def two_five():
    global room
    room = "two_five"
    print("From here you have a full view of both the doors to your west and the huge corridor to your east.")
    time.sleep(n)
    print("You now realise you have a lot to explore.")
    time.sleep(n)
    return room



def two_six():
    global room
    room = "two_six"
    print("To your north-west there is a room with an odd object.")
    time.sleep(n)
    print("To your east by a few spaces there appears to be an entrance to another corridor.")
    time.sleep(n)
    print("You have also seemed to reach one of the northern walls of this big room, save for the corridors you see.")
    time.sleep(n)
    return room

def two_six_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global two_six_wall_done
        global two_six_wall_backup
        global general_backup
        if two_six_wall_done == False:
            two_six_wall_backup = general_backup = wall_counter
            wall_message_check(two_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(two_six_wall_backup)
        two_six_wall_done = True
        return wall_counter, two_six_wall_done
    else:
        print("You can't interact with that.")
        


def three_four():
    global room
    room = "three_four"
    print("To your south-east is the lectern room.")
    time.sleep(n)
    print("Overall you are further along the corridor.")
    time.sleep(n)
    print("A few spaces further east of you is what looks to be a corridor entrance.")
    time.sleep(n)
    print("(This is on the border of v0.2.1 content (3, y), but there may still be more to do in previous rooms!)")
    time.sleep(n)
    return room

def three_four_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global three_four_wall_done
        global three_four_wall_backup
        global general_backup
        if three_four_wall_done == False:
            three_four_wall_backup = general_backup = wall_counter
            wall_message_check(three_four_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(three_four_wall_backup)
        three_four_wall_done = True
        return wall_counter, three_four_wall_done
    else:
        print("You can't interact with that.")




def three_five():
    global room
    room = "three_five"
    print("You are further centered in the huge room.")
    time.sleep(n)
    print("There is little to do in the centre.")
    time.sleep(n)
    print("(This is on the border of v0.2.1 content (3, y), but there may still be more to do in previous rooms!)")
    time.sleep(n)
    return room



def three_six():
    global room
    room = "three_six"
    print("On your immediate east is the entrance to a corridor going north.")
    time.sleep(n)
    print("It may have some clues towards opening another door.")
    time.sleep(n)
    print("(This is on the border of v0.2.1 content (3, y), but there may still be more to do in previous rooms!)")
    time.sleep(n)
    return room

def three_six_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global three_six_wall_done
        global three_six_wall_backup
        global general_backup
        if three_six_wall_done == False:
            three_six_wall_backup = general_backup = wall_counter
            wall_message_check(three_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(three_six_wall_backup)
        three_six_wall_done = True
        return wall_counter, three_six_wall_done
    else:
        print("You can't interact with that.")




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
        global edge_done
        for x in no_edges:
            edge_done = False
            if room == x.name:
                print("There are no edges to move to in this room.")
                time.sleep(n)
                edge_done = True
                break
        if edge_done == False:
            for x in range(0, len(locations)):
                y = locations[x]
                if newx == y.xpos and newy == y.ypos:
                    for x in multiple_edges:
                        if room == x.name:                            
                            eval(y.name+"_edges()")
                            break
                    else:
                        try:
                            eval(y.name+"_edge()")
                        except NameError:
                            print("There are no edges to move to in this room.")
                            time.sleep(n)
                        
def examine(room):
    global examine_done
    for x in no_examine:
        examine_done = False
        if room == x.name:                  
            print("There is nothing to examine in this room.")
            time.sleep(n)
            examine_done = True
            break
    if examine_done == False:        
        obj_examine = input("What object would you like to examine?: ")
        for x in range(0, len(locations)):
            y = locations[x]
            if newx == y.xpos and newy == y.ypos:
                eval(y.name+"_examine(obj_examine)")
"""    
(level_name)interact():
   (obj_interact choice):
        (text for choice)
"""
"""
eval(level_name_interact())
"""
def interact(room):
    global interact_done
    for x in no_interact:
        interact_done = False
        if room == x.name:
            print("There is nothing to interact with in this room.")
            time.sleep(n)
            interact_done = True
            break
    if interact_done == False:
        obj_interact = input("What would you like to interact with?: ")
        for x in range(0, len(locations)):
            y = locations[x]
            if newx == y.xpos and newy == y.ypos:
                eval(y.name+"_interact(obj_interact)")
    """                                        #REFORM INTERACT MECHANICS TO REDUCE THE LINES USED
    if interact_done == False:
        elif room == "three_six":
            if obj_interact == "wall":
                three_six_wall()
            else:
                print("You can't interact with that.")
    """
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
    global bookshelf_interact_state
    for x in inventory:
        if item == x:
            inventory.remove(item)
            print("Dropped", item, "from inventory!")
            if item == "book" or item == "fish book" or item == "wall lore book":
                bookshelf_interact_state = False
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
    elif item == "note":
        note_use()
    else:
        print("You can't use that item.")
    

def room_check(x, y, newx, newy):
    for x in range(0, len(locations)):
        y = locations[x]
        if newx == y.xpos and newy == y.ypos:
            eval(y.name+"()")

def wall_message_check(general_backup):
    for x in range(0, 100):
        if x == general_backup:
            eval("wall_"+str(general_backup)+"()")
        else:
            pass
        
def repeated_action(x, y, newx, newy, wall_counter):
    global action
    for x in game_values_string:
        exec("global "+x)
    print()
    room_check(x, y, newx, newy)
    x = newx
    y = newy
    print("Your co-ordinates are", str(x)+", "+str(y))
    action = input("What to do? (interact, move, use, examine, inventory, stop): ")
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
        try:
            os.remove("save.txt")
        except Exception:
            game_on = True
            game_values = [restricted_pos, book_num, n, game_on, x, newx, y, newy, room, inventory, ending_condition, one_one_door_interact_state, bookshelf_interact_state, wall_counter, general_backup, one_seven_switch_done]
            file = open("save.txt", "w")
            for x, y in zip(game_values, game_values_string):
                txt = str(y+"="+str(x))
                file.write(txt)
                file.write("\n")
            file.close()
            game_on = "ended"
            return action
    else:
        print("You can't do that.")
    
def game_load():
    global game_on
    time_check()
    print("Enter 'stop' to exit and save your game.")
    time.sleep(1)
    print("(Current boundaries for this version are (3, y) and (0, y) apart from (0, 4) and (0, 0). Nothing is more east or more north than those points.)")
    time.sleep(1)
    game_on = True
    return game_on
    
while game_on == False:
    start = input("Turn game on?: ")
    if start == "yes":
        load = input("Start new or load file? (new, load): ")
        if load == "new":
            try:
                os.remove("save.txt")
            except Exception:
                pass
            game_load()
        elif load == "load":
            try:
                file = open("save.txt", "r")
            except FileNotFoundError:
                print("You have no save file.")
                time.sleep(1)
                print("Starting new game...")
                time.sleep(1)
                game_load()
            else:
                #try:
                for x in file:
                    exec(x)
                    #eval(a+"="+x)
                    count = count + 1
                general_backup = wall_counter = 0
                game_load()
            exec("game_on = True")
        else:
            print("Exiting...")
            game_on = "ended"
            break
    else:
        print("Next time, play gaming.")
        game_on = "ended"
        break

while game_on == True:
    if ending_condition == True:
        game_on = "ended"
        break
    elif action == "stop":
        ending_condition = True
        game_on = "ended"
        break
    repeated_action(x, y, newx, newy, wall_counter)
    
