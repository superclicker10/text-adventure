import time
import random
import webbrowser
import os
import sys
import warnings
from location import *
from locations import *
from wallmessages import *
from books import *
# ADD THE BACKROOMS
# v1.0bf: fixed loading save bug, fixed combat autosave, fixed repeat blade pickup text
restricted_pos = ["01", "02", "03", "04", "05", "06", "07", "18", "20", "21", "22", "27", "33", "37", "38", "39", "40", "41", "42", "43", "410", "55", "54", "56", "57", "58", "59", "60", "61", "62", "63", "67", "73", "77", "710", "83", "87", "88", "89", "92", "911", "103", "104", "106", "107", "108", "109", "1010"]
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
combat_state = False
inventory = []
inv_size = 3
health = 10
statue_health = 10
statue_state = "alive"
attack_pattern = False
weapon = "your fists"
atk_power = 1
ending_condition = False
one_one_door_interact_state = False
bookshelf_interact_state = False
wall_counter = 0
general_backup = 0
one_two_door_interact = False
one_seven_switch_done = False
four_nine_switch_done = False
five_zero_switch_done = False
lobby_wall = bookshelf_wall = one_one_wall_done = one_two_wall_done = one_three_wall_done = one_seven_wall_done = lectern_wall_done = two_six_wall_done = False
lobby_wall_backup = bookshelf_wall_backup = one_one_wall_backup = one_two_wall_backup = one_three_wall_backup = one_seven_wall_backup = lectern_room_wall_backup = two_six_wall_backup = 0
zero_four_wall_done = zero_five_wall_done = three_four_wall_done = three_six_wall_done = four_four_wall_done = four_seven_wall_done = four_eight_wall_done = four_nine_wall_done = five_one_wall_done = five_two_wall_done = five_three_wall_done = five_six_wall_done = False
zero_four_wall_backup = zero_five_wall_backup = three_four_wall_backup = three_six_wall_backup = four_four_wall_backup = four_seven_wall_backup = four_eight_backup_state = four_nine_wall_backup = five_one_wall_backup = five_two_wall_backup =  five_three_wall_backup = five_six_wall_backup = 0
five_zero_wall_done = zero_six_wall_done = six_four_wall_done = six_six_wall_done = seven_four_wall_done = seven_six_wall_done = eight_four_wall_done = eight_six_wall_done = nine_three_wall_done = nine_four_wall_done = nine_six_wall_done = nine_seven_wall_done = False
five_zero_wall_backup = zero_six_wall_backup = six_four_wall_backup = six_six_wall_backup = seven_five_wall_done = seven_six_wall_backup = eight_four_wall_backup = eight_six_wall_backup = nine_three_wall_backup = nine_four_wall_backup = nine_six_wall_backup = nine_seven_wall_backup = 0
eight_ten_wall_done = nine_seven_wall_done = nine_eight_wall_done = nine_nine_wall_done = nine_ten_wall_done = ten_five_wall_done = False
eight_ten_wall_backup = nine_seven_wall_backup = nine_eight_wall_backup = nine_nine_wall_backup = nine_ten_wall_backup = ten_five_wall_backup = 0
game_values = [restricted_pos, book_num, n, game_on, x, newx, y, newy, room, combat_state, statue_state, inventory, inv_size, health, weapon, atk_power, ending_condition, one_one_door_interact_state, bookshelf_interact_state, wall_counter, general_backup, one_two_door_interact, one_seven_switch_done]
game_values.extend([four_nine_switch_done, five_zero_switch_done])
game_values_string = ["restricted_pos", "book_num", "n", "game_on", "x", "newx", "y", "newy", "room", "combat_state", "statue_state", "inventory", "inv_size", "health", "weapon", "attack_power", "ending_condition", "one_one_door_interact_state", "bookshelf_interact_state", "wall_counter", "general_backup", "one_two_door_interact", "one_seven_switch_done"]
game_values_string.extend(["four_nine_switch_done", "five_zero_switch_done"])

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    
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
            n = 0.5
            time.sleep(n)
        elif n > 2:
            print("Delay set to max value (2)")
            n = 2
            time.sleep(n)
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
        time.sleep(n)





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
            zero_four_wall_backup = general_backup = wall_counter
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



def zero_five():
    global room
    room = "zero_five"
    print("This is the second once locked room.")
    time.sleep(n)
    print("It contains a small, solitary key on the ground.")
    time.sleep(n)
    print("It might have something to do with the wall.")
    time.sleep(n)

def zero_five_interact(obj_interact):
    global inventory
    if obj_interact == "key":
        if "key" not in inventory:
            print("You pick up the key.")
            time.sleep(n)
            add_inventory("key")
            restricted_pos.remove("54")
            restricted_pos.remove("55")
            restricted_pos.remove("56")
        else:
            print("You have already picked up the key.")
    elif obj_interact == "wall":
        global wall_counter
        global zero_five_wall_done
        global zero_five_wall_backup
        global general_backup
        if zero_five_wall_done == False:
            zero_five_wall_backup = general_backup = wall_counter
            wall_message_check(zero_five_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(zero_five_wall_backup)
        zero_five_wall_done = True
        return wall_counter, zero_five_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def zero_six():
    global room
    room = "zero_six"
    print("This is the most northern of the three rooms.")
    time.sleep(n)
    print("There is a button on the ground, that looks like it can be picked up.")
    time.sleep(n)
    print("It may help you later on.")
    time.sleep(n)
    return room

def zero_six_interact(obj_interact):
    global inventory
    if obj_interact == "button":
        if "button" not in inventory:
            print("You pick up the button.")
            time.sleep(n)
            add_inventory("button")
            try:
                restricted_pos.remove("106")
            except Exception:
                pass
        else:
            print("You have already picked up the button.")
    elif obj_interact == "wall":
        global wall_counter
        global zero_six_wall_done
        global zero_six_wall_backup
        global general_backup
        if zero_six_wall_done == False:
            zero_six_wall_backup = general_backup = wall_counter
            wall_message_check(zero_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(zero_six_wall_backup)
        zero_six_wall_done = True
        return wall_counter, zero_six_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def zero_six_examine(obj_examine):
    if obj_examine == "button" and "button" not in inventory:
        print("A small button that looks like it can be used to end something, or to start something new.")
        time.sleep(n)
        print("You get a weird feeling.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)


        
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
            one_one_door_interact_state = True                      
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
                time.sleep(n)
            elif book_num >= 99:
                add_inventory("wall lore book")
                time.sleep(n)
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
    elif obj_interact == "hole":
        hole_ending_sequence()
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
    global health
    health = health - 2
    if health <= 0:
        print("You jump in the hole, falling forever and ever.")
        time.sleep(3)
        for x in range(0, 250000):
            print("DEATH", end="")
        for x in range(0, 150):
            print("\n")
        print("ENDING 1 - FALLING INTO THE DEPTHS")
        time.sleep(4)
        ending_condition = True
    else:
        print("You jump into the hole, falling forever and ever...")
        time.sleep(n)
        print("...until a sudden jump brings you back.")
        time.sleep(n)


    
    

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
        time.sleep(n)




def three_five():
    global room
    room = "three_five"
    print("You are further centered in the huge room.")
    time.sleep(n)
    print("There is little to do in the centre.")
    time.sleep(n)
    return room



def three_six():
    global room
    room = "three_six"
    print("On your immediate east is the entrance to a corridor going north.")
    time.sleep(n)
    print("It may have some clues towards opening another door.")
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
        time.sleep(n)



def four_four():
    global room
    room = "four_four"
    if "key" not in inventory:
        print("You suddenly see a huge barrier appear in front of you, blocking the path.")
        time.sleep(n)
        print("There is a long corridor to your north.")
        time.sleep(n)
        print("Perhaps it might be worth an investigation.")
        time.sleep(n)
    else:
        print("You are at the border of where the barrier used to be.")
        time.sleep(n)
        print("There is a corridor to the south-east of you.")
        time.sleep(n)
    return room

def four_four_edge():
    if "key" not in inventory:
        print("A huge barrier with details examining may reveal.")
        time.sleep(n)
    else:
        print("There are no edges to examine in this room.")
        time.sleep(n)

def four_four_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global four_four_wall_done
        global four_four_wall_backup
        global general_backup
        if four_four_wall_done == False:
            four_four_wall_backup = general_backup = wall_counter
            wall_message_check(four_four_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(four_four_wall_backup)
        four_four_wall_done = True
        return wall_counter, four_four_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def four_four_examine(obj_examine):
    if obj_examine == "barrier" and "key" not in inventory:
        print("A huge barrier blocking the path to the rest of the space.")
        time.sleep(n)
        print("However, it does look like it can be opened using a remote system, or a key.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)



def four_five():
    global room
    room = "four_five"
    if "key" not in inventory:
        print("You suddenly see a huge barrier appear in front of you, blocking the path.")
        time.sleep(n)
        print("You are a bit closer to the entrance of the northern corridor.")
        time.sleep(n)
        print("Perhaps it might be worth an investigation.")
        time.sleep(n)
    else:
        print("You are at the border of where the barrier used to be.")
        time.sleep(n)
        print("You are in the middle of the big space.")
        time.sleep(n)
    return room

def four_five_edge():
    if "key" not in inventory:
        print("A huge barrier with details examining may reveal.")
        time.sleep(n)
    else:
        print("There are no edges to examine in this room.")
        time.sleep(n)

def four_five_examine(obj_examine):
    if obj_examine == "barrier" and "key" not in inventory:
        print("A huge barrier blocking the path to the rest of the space.")
        time.sleep(n)
        print("It looks like it can be opened using a remote system.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)
        



def four_six():
    global room
    room = "four_six"
    if "key" not in inventory:
        print("You are at the entrance to the northern corridor.")
        time.sleep(n)
        print("The huge barrier still looms over you to your east.")
        time.sleep(n)
    else:
        print("You are at the entrance to the northern corridor.")
        time.sleep(n)
        print("You are also at the border of where the barrier used to be.")
        time.sleep(n)
    return room

def four_six_edge():
    if "key" not in inventory:
        print("A huge barrier with details examining may reveal.")
        time.sleep(n)
    else:
        print("There are no edges to examine in this room.")
        time.sleep(n)

def four_six_examine(obj_examine):
    if obj_examine == "barrier" and "key" not in inventory:
        print("A huge barrier blocking the path to the rest of the space.")
        time.sleep(n)
        print("It looks like it can be opened using a remote system.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)



def four_seven():
    global room
    room = "four_seven"
    print("You enter the northern corridor.")
    time.sleep(n)
    print("There appears to be an object at the other end.")
    time.sleep(n)
    print("You feel claustrophobic.")
    time.sleep(n)
    return room

def four_seven_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global four_seven_wall_done
        global four_seven_wall_backup
        global general_backup
        if four_seven_wall_done == False:
            four_seven_wall_backup = general_backup = wall_counter
            wall_message_check(four_seven_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(four_seven_wall_backup)
        four_seven_wall_done = True
        return wall_counter, four_seven_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def four_eight():
    global room
    room = "four_eight"
    print("You are further down the corridor.")
    time.sleep(n)
    print("The object is almost within view.")
    time.sleep(n)
    print("You still feel claustrophobic.")
    time.sleep(n)
    return room

def four_eight_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global four_eight_wall_done
        global four_eight_wall_backup
        global general_backup
        if four_eight_wall_done == False:
            four_eight_wall_backup = general_backup = wall_counter
            wall_message_check(four_eight_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(four_eight_wall_backup)
        four_eight_wall_done = True
        return wall_counter, four_eight_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def four_nine():
    global room
    room = "four_nine"
    print("You arrive at a room with a strange object that looks like a lever.")
    time.sleep(n)
    print("Perhaps it can be used to open the locked doors.")
    time.sleep(n)
    print("You are at the end of the long corridor.")
    time.sleep(n)
    return room

def four_nine_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global four_nine_wall_done
        global four_nine_wall_backup
        global general_backup
        if four_nine_wall_done == False:
            four_nine_wall_backup = general_backup = wall_counter
            wall_message_check(four_nine_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(four_nine_wall_backup)
        four_nine_wall_done = True
        return wall_counter, four_nine_wall_done
    elif obj_interact == "lever":
        global four_nine_switch_done
        if four_nine_switch_done == False:
            print("You turn the lever.")
            time.sleep(n)
            print("With a crank, and a loud noise, something opens in the distance.")
            time.sleep(n)
            print("Perhaps you should go investigate.")
            time.sleep(n)
            four_nine_switch_done = True
            restricted_pos.remove("05")
        else:
            print("You have already turned the lever.")
            time.sleep(n)
    else:
        print("You can't interact with that.")
        time.sleep(n)

def four_nine_examine(obj_examine):
    if obj_examine == "lever":
        print("A fairly big mechanical lever.")
        time.sleep(n)
        print("It might help you open those locked doors at your west.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)



def five_zero():
    global room
    room = "five_zero"
    print("You reach the end of the southern corridor.")
    time.sleep(n)
    print("Another lever awaits you.")
    time.sleep(n)
    return room

def five_zero_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global five_zero_wall_done
        global five_zero_wall_backup
        global general_backup
        if five_zero_wall_done == False:
            five_zero_wall_backup = general_backup = wall_counter
            wall_message_check(five_zero_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(five_zero_wall_backup)
    elif obj_interact == "lever":
        global five_zero_switch_done
        if five_zero_switch_done == False:
            print("You turn the lever.")
            time.sleep(n)
            print("With a crank, and a loud noise, something opens in the distance.")
            time.sleep(n)
            print("Perhaps you should go investigate.")
            time.sleep(n)
            five_zero_switch_done = True
            restricted_pos.remove("06")
        else:
            print("You have already turned the lever.")
            time.sleep(n)
    else:
        print("You can't interact with that.")
        time.sleep(n)

def five_zero_examine(obj_examine):
    if obj_examine == "lever":
        print("Another lever that may open one of the doors.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)


        

def five_one():
    global room
    room = "five_one"
    print("You go even further into the southern corridor.")
    time.sleep(n)
    print("The end of it is further in sight.")
    time.sleep(n)
    return room

def five_one_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global five_one_wall_done
        global five_one_wall_backup
        global general_backup
        if five_one_wall_done == False:
            five_one_wall_backup = general_backup = wall_counter
            wall_message_check(five_one_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(five_one_wall_backup)
        five_one_wall_done = True
        return wall_counter, five_one_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def five_two():
    global room
    room = "five_two"
    print("You go further into the southern corridor.")
    time.sleep(n)
    print("The end of it is ahead of you by a few spaces.")
    time.sleep(n)
    return room

def five_two_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global five_two_wall_done
        global five_two_wall_backup
        global general_backup
        if five_two_wall_done == False:
            five_two_wall_backup = general_backup = wall_counter
            wall_message_check(five_two_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(five_two_wall_backup)
        five_two_wall_done = True
        return wall_counter, five_two_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



    
def five_three():
    global room
    room = "five_three"
    print("You enter the southern corridor.")
    time.sleep(n)
    print("Another switch like object appears to be at the end.")
    time.sleep(n)
    print("It may help you to open one of the three doors.")
    time.sleep(n)
    return room

def five_three_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global five_three_wall_done
        global five_three_wall_backup
        global general_backup
        if five_three_wall_done == False:
            five_three_wall_backup = general_backup = wall_counter
            wall_message_check(five_three_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(five_three_wall_backup)
        five_three_wall_done = True
        return wall_counter, five_three_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)




def five_four():
    global room
    room = "five_four"
    print("You have passed the barrier.")
    time.sleep(n)
    print("Now you see the second part of the space to your east clearly.")
    time.sleep(n)
    print("Just south of you is another corridor.")
    time.sleep(n)
    return room


    

def five_five():
    global room
    room = "five_five"
    print("You have passed the barrier.")
    time.sleep(n)
    print("Now you see the second part of the space to your east clearly.")
    time.sleep(n)
    print("Far south of you there is another corridor.")
    time.sleep(n)
    return room

    

def five_six():
    global room
    room = "five_six"
    print("You have passed the barrier.")
    time.sleep(n)
    print("Now you see the second part of the space to your east clearly.")
    time.sleep(n)
    print("Very far south of you there is another corridor.")
    time.sleep(n)
    return room

def five_six_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global five_six_wall_done
        global five_six_wall_backup
        global general_backup
        if five_six_wall_done == False:
            five_six_wall_backup = general_backup = wall_counter
            wall_message_check(five_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(five_six_wall_backup)
        five_six_wall_done = True
        return wall_counter, five_six_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def six_four():
    global room
    room = "six_four"
    print("You advance into the second part of the space.")
    time.sleep(n)
    print("To your north east there is something on the ground.")
    time.sleep(n)
    return room

def six_four_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global six_four_wall_done
        global six_four_wall_backup
        global general_backup
        if six_four_wall_done == False:
            six_four_wall_backup = general_backup = wall_counter
            wall_message_check(six_four_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(six_four_wall_backup)
        six_four_wall_done = True
        return wall_counter, six_four_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def six_five():
    global room
    room = "six_five"
    print("You advance into the second part of the space.")
    time.sleep(n)
    print("To your east there is something on the ground.")
    time.sleep(n)
    return room



def six_six():
    global room
    room = "six_six"
    print("You advance into the second part of the space.")
    time.sleep(n)
    print("To your south east there is something on the ground.")
    time.sleep(n)

def six_six_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global six_six_wall_done
        global six_six_wall_backup
        global general_backup
        if six_six_wall_done == False:
            six_six_wall_backup = general_backup = wall_counter
            wall_message_check(six_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(six_six_wall_backup)
        six_six_wall_done = True
        return wall_counter, six_six_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)




def seven_four():
    global room
    room = "seven_four"
    print("You go further into the space.")
    time.sleep(n)
    print("To your north is something on the ground.")
    time.sleep(n)
    return room

def seven_four_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global seven_four_wall_done
        global seven_four_wall_backup
        global general_backup
        if seven_four_wall_done == False:
            seven_four_wall_backup = general_backup = wall_counter
            wall_message_check(seven_four_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(seven_four_wall_backup)
        seven_four_wall_done = True
        return wall_counter, seven_four_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def seven_five():
    global room
    room = "seven_five"
    print("You go further into the space.")
    time.sleep(n)
    print("There is a piece of food on the ground.")
    time.sleep(n)
    print("You don't feel hungry right now, but you may need it later.")
    time.sleep(n)
    return room

def seven_five_interact(obj_interact):
    if obj_interact == "food" and ("apple" not in inventory):
        print("You pick the food off of the ground.")
        time.sleep(n)
        add_inventory("apple")
        time.sleep(n)
    else:
        print("You have already picked up the apple.")
        time.sleep(n)

def seven_five_examine(obj_examine):
    if obj_examine == "food":
        print("A small apple on the ground.")
        time.sleep(n)
        print("At least it looks fresh.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)
        
def apple_use():
    global health
    if health >= 10:
        print("You already have maximum health.")
        time.sleep(n)
    elif health < 10:
        print("Eating apple...")
        time.sleep(n)
        health = health + 4
        inventory.remove("apple")
        if health > 10:
            health = 10
        print("You have", health, "health.")
        time.sleep(n)

def seven_six():
    global room
    room = "seven_six"
    print("You go further into the space.")
    time.sleep(n)
    print("To your south there is something on the ground.")
    time.sleep(n)
    return room

def seven_six_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global seven_six_wall_done
        global seven_six_wall_backup
        global general_backup
        if seven_six_wall_done == False:
            seven_six_wall_backup = general_backup = wall_counter
            wall_message_check(seven_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(seven_six_wall_backup)
        seven_six_wall_done = True
        return wall_counter, seven_six_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def eight_four():
    global room
    room = "eight_four"
    print("You get closer to the eastern wall of the complex.")
    time.sleep(n)
    print("The last huge corridor to your east seems to hold many things.")
    time.sleep(n)
    return room

def eight_four_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global eight_four_wall_done
        global eight_four_wall_backup
        global general_backup
        if eight_four_wall_done == False:
            eight_four_wall_backup = general_backup = wall_counter
            wall_message_check(eight_four_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(eight_four_wall_backup)
        eight_four_wall_done = True
        return wall_counter, eight_four_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)




def eight_five():
    global room
    room = "eight_five"
    print("You get closer to the eastern wall of the complex.")
    time.sleep(n)
    print("The last huge corridor to your east seems to hold many things.")
    time.sleep(n)
    return room



def eight_six():
    global room
    room = "eight_six"
    print("You get closer to the eastern wall of the complex.")
    time.sleep(n)
    print("The last huge corridor to your east seems to hold many things.")
    time.sleep(n)
    return room

def eight_six_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global eight_six_wall_done
        global eight_six_wall_backup
        global general_backup
        if eight_six_wall_done == False:
            eight_six_wall_backup = general_backup = wall_counter
            wall_message_check(eight_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(eight_six_wall_backup)
        eight_six_wall_done = True
        return wall_counter, eight_six_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)


def eight_ten():
    global room
    room = "eight_ten"
    print("A blue light leading to another distant place lies north.")
    time.sleep(n)
    print("You still have time to go back.")
    time.sleep(n)
    return room

def eight_ten_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global eight_ten_wall_done
        global eight_ten_wall_backup
        global general_backup
        if eight_ten_wall_done == False:
            eight_ten_wall_backup = general_backup = wall_counter
            wall_message_check(eight_ten_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(eight_ten_wall_backup)
        eight_ten_wall_done = True
        return wall_counter, eight_ten_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)


    

def eight_eleven():
    global room
    global ending_condition
    room = "eight_eleven"
    backrooms_entry_ending()
    ending_condition = True
    return ending_condition
    
def backrooms_entry_ending():
    global ending_condition
    global game_on
    print("You enter through the portal into a strange place filled with yellow walls and a sense of evil.")
    time.sleep(2)
    print("(This is the Backrooms DLC to be developed after the game's completion. Come here when the DLC is released.)")
    time.sleep(2)
    print("ENDING 2 - INTO THE BACKROOMS")
    time.sleep(3)
    ending_condition = True

def nine_three():
    global room
    room = "nine_three"
    print("You are at the southern edge of the eastern corridor.")
    time.sleep(n)
    print("There is a backpack on the ground.")
    time.sleep(n)
    print("It may be of use to you.")
    time.sleep(n)
    return room

def nine_three_interact(obj_interact):
    if obj_interact == "backpack":
        global inv_size
        if inv_size >= 5:
            print("You already have the backpack.")
            time.sleep(n)
        else:
            print("You pick up the backpack.")
            time.sleep(n)
            inv_size = 5
            print("Inventory size increased to 5!")
            time.sleep(n)
    elif obj_interact == "wall":
        global wall_counter
        global nine_three_wall_done
        global nine_three_wall_backup
        global general_backup
        if nine_three_wall_done == False:
            nine_three_wall_backup = general_backup = wall_counter
            wall_message_check(nine_three_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(nine_three_wall_backup)
        nine_three_wall_done = True
        return wall_counter, nine_three_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def nine_three_examine(obj_examine):
    if obj_examine == "backpack":
        print("A backpack on the ground.")
        time.sleep(n)
        print("It may increase your inventory size.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)


        
def nine_four():
    global room
    room = "nine_four"
    print("You are at the eastern edge of the space.")
    time.sleep(n)
    print("There seems to be objects below and above you.")
    time.sleep(n)
    return room

def nine_four_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global nine_four_wall_done
        global nine_four_wall_backup
        global general_backup
        if nine_four_wall_done == False:
            nine_four_wall_backup = general_backup = wall_counter
            wall_message_check(nine_four_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(nine_four_wall_backup)
        nine_four_wall_done = True
        return wall_counter, nine_four_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def nine_five():
    global room
    room = "nine_five"
    print("There is a room to your east.")
    time.sleep(n)
    print("And there is a blade on the ground.")
    time.sleep(n)

def nine_five_interact(obj_interact):
    if obj_interact == "blade":
        global weapon
        global atk_power
        if weapon != "a blade":
            print("You pick up the blade.")
            time.sleep(n)
            weapon = "a blade"
            atk_power = 2
            print("Your attack power is now 2.")
            time.sleep(n)
        else:
            print("You already have the blade.")
            time.sleep(n)
        return weapon
    else:
        print("You can't interact with that.")
        time.sleep(n)

def nine_five_examine(obj_examine):
    if obj_examine == "blade":
        print("A small blade with a wood handle.")
        time.sleep(n)
        print("It could make you appear more dangerous to anything that you come across.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)

def nine_five_edge():
    print("A room to your east contains something alive inside of it.")
    time.sleep(n)
    print("It may pose a threat to you if you approach it.")
    time.sleep(n)




def nine_six():
    global room
    room = "nine_six"
    print("You are at the eastern end of the space.")
    time.sleep(n)
    print("There is a strange object north of you.")
    time.sleep(n)
    return room

def nine_six_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global nine_six_wall_done
        global nine_six_wall_backup
        global general_backup
        if nine_six_wall_done == False:
            nine_six_wall_backup = general_backup = wall_counter
            wall_message_check(nine_six_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(nine_six_wall_backup)
        nine_six_wall_done = True
        return wall_counter, nine_six_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def nine_seven():
    global room
    room = "nine_seven"
    print("You approach the northern end of the corridor.")
    time.sleep(n)
    print("There is a strange screen on the floor.")
    time.sleep(n)
    print("Also, the northern wall does not look to be as solid as the others...")
    time.sleep(n)
    return room

def nine_seven_interact(obj_interact):
    if obj_interact == "screen":
        if "screen" not in inventory:
            print("You pick up the screen.")
            time.sleep(n)
            print("It lights up and displays some numbers on the screen.")
            time.sleep(n)
            print("Perhaps using it will give you more information.")
            time.sleep(n)
            add_inventory("screen")
        else:
            print("You already have the screen.")
            time.sleep(n)
    elif obj_interact == "wall":
        global wall_counter
        global nine_seven_wall_done
        global nine_seven_wall_backup
        global general_backup
        if nine_seven_wall_done == False:
            nine_seven_wall_backup = general_backup = wall_counter
            wall_message_check(nine_seven_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(nine_seven_wall_backup)
        nine_seven_wall_done = True
        return wall_counter, nine_seven_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def nine_seven_examine(obj_examine):
    if obj_examine == "screen":
        print("The screen displays a number as a fraction of another.")
        time.sleep(n)
        print("It's title is 'WALLS TOUCHED'.")
        time.sleep(n)
        print("You realise this might have importance across the whole space.")
        time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)

def screen_use():
    print()
    print("You have touched", wall_counter, "out of 37 walls in the game.")
    time.sleep(n)



def nine_eight():
    global room
    room = "nine_eight"
    print("You enter through the veil into a mystical place.")
    time.sleep(n)
    print("The corridor continues further north.")
    time.sleep(n)
    return room

def nine_eight_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global nine_eight_wall_done
        global nine_eight_wall_backup
        global general_backup
        if nine_eight_wall_done == False:
            nine_eight_wall_backup = general_backup = wall_counter
            wall_message_check(nine_eight_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(nine_eight_wall_backup)
        nine_eight_wall_done = True
        return wall_counter, nine_eight_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def nine_nine():
    global room
    room = "nine_nine"
    print("You continue as the shade of your vision gets darker.")
    time.sleep(n)
    print("Stars appear around you.")
    time.sleep(n)
    print("Something isn't right here. There is another space further north.")
    time.sleep(n)
    return room

def nine_nine_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global nine_nine_wall_done
        global nine_nine_wall_backup
        global general_backup
        if nine_nine_wall_done == False:
            nine_nine_wall_backup = general_backup = wall_counter
            wall_message_check(nine_nine_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(nine_nine_wall_backup)
        nine_nine_wall_done = True
        return wall_counter, nine_nine_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def nine_ten():
    global room
    room = "nine_ten"
    print("You go further down.")
    time.sleep(n)
    print("Your sense of reality feels weak here.")
    time.sleep(n)
    print("There is another space to your west, and an odd blue light in the distance.")
    time.sleep(n)
    return room

def nine_ten_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global nine_ten_wall_done
        global nine_ten_wall_backup
        global general_backup
        if nine_ten_wall_done == False:
            nine_ten_wall_backup = general_backup = wall_counter
            wall_message_check(nine_ten_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(nine_ten_wall_backup)
        nine_ten_wall_done = True
        return wall_counter, nine_ten_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)



def ten_five():
    global room
    global combat_state
    global game_values_string
    global health
    room = "ten_five"
    if statue_state == "alive" and health > 0:
        for x in game_values_string:
            exec("global "+x)
        print("You enter a room with a statue. But it moves in reaction to your presence.")
        time.sleep(n)
        print("It doesn't want you here.")
        time.sleep(n)
        print("Entering combat...(GAME AUTOSAVE)")
        time.sleep(2)
        global game_values
        global newx
        global newy
        global y
        game_values = [restricted_pos, book_num, n, game_on, x, newx, y, newy, room, combat_state, statue_state, inventory, inv_size, health, weapon, atk_power, ending_condition, one_one_door_interact_state, bookshelf_interact_state, wall_counter, general_backup, one_two_door_interact, one_seven_switch_done]
        game_values.extend([four_nine_switch_done, five_zero_switch_done])
        game_values_string = ["restricted_pos", "book_num", "n", "game_on", "x", "newx", "y", "newy", "room", "combat_state", "statue_state", "inventory", "inv_size", "health", "weapon", "atk_power", "ending_condition", "one_one_door_interact_state", "bookshelf_interact_state", "wall_counter", "general_backup", "one_two_door_interact", "one_seven_switch_done"]
        game_values_string.extend(["four_nine_switch_done", "five_zero_switch_done"])
        file = open("save.txt", "w")
        for x, y in zip(game_values, game_values_string):
            if y == "weapon":
                txt = "weapon="+f'"{weapon}"'+"\n"
                file.write(txt)
            elif y == "statue_state":
                txt = "statue_state="+f'"{statue_state}"'+"\n"
                file.write(txt)
            elif y == "room":
                file.write("room='ten_five'"+"\n")
            elif y == "x":
                x = 10
                newx = x
                newy = y
                y = newy = 5
                file.write("x="+str(x)+"\n")
                x = 10
                newx = 10
                y = newy = 5
            elif y == "statue_state":
                file.write("statue_state="+f'"{statue_state}"'+"\n")
            else:
                txt = str(y+"="+str(x))
                file.write(txt)
                file.write("\n")
        file.close()
        combat_state = True
        return combat_state, room, health
    elif health <= 0:
        death_sequence()
        combat_state = False
        return combat_state
    else:
        print("You are where the statue's corpse lies.")
        time.sleep(n)
        print("To the east of you is an open space.")
        time.sleep(n)
        print("Freedom looks to be mere moments away.")
        time.sleep(n)
        return room

def ten_five_interact(obj_interact):
    if obj_interact == "wall":
        global wall_counter
        global ten_five_wall_done
        global ten_five_wall_backup
        global general_backup
        if ten_five_wall_done == False:
            ten_five_wall_backup = general_backup = wall_counter
            wall_message_check(ten_five_wall_backup)
            wall_counter = wall_counter + 1
        else:
            wall_message_check(ten_five_wall_backup)
        ten_five_wall_done = True
        return wall_counter, ten_five_wall_done
    else:
        print("You can't interact with that.")
        time.sleep(n)

def ten_five_examine(obj_examine):
    if obj_examine == "statue":
        if statue_state == "alive":
            print("A big statue made of rock.")
            time.sleep(n)
            print("It is threatening but not exactly overpowering.")
            time.sleep(n)
        else:
            print("A big statue made of rock.")
            time.sleep(n)
            print("It is now dead on the floor.")
            time.sleep(n)
    else:
        print("You can't examine that.")
        time.sleep(n)

def ten_five_edge():
    print("Freedom.")
    time.sleep(n)

def ten_five_combat():
    global health
    global weapon
    global statue_health
    global attack_pattern
    global combat_state
    global statue_state
    global game_values_string
    global action
    if action == "stop":
        exit(1)
    for x in game_values_string:
        exec("global "+x)
    if health <= 0:
        death_sequence()
        combat_state = False
        return combat_state
    elif statue_health <= 0:
        print("The statue falls as it dies.")
        time.sleep(n)
        print("You are victorious!")
        time.sleep(n)
        combat_state = False
        statue_state = "dead"
        return combat_state, statue_state
    elif attack_pattern == True:
        statue_pattern()
        attack_pattern = False
    else:
        print("You have", health, "health.")
        time.sleep(n)
        print("You have", weapon, "as your weapon.")
        time.sleep(n)
        print("The statue has", statue_health, "health left.")
        action = input("What to do? (attack, idle, interact, examine, move (edge), use, inventory, stop): ")
        if action == "attack":
            eval(room+"_attack()")
            attack_pattern = True
        elif action == "idle":
            print("You wait. It doesn't seem helpful. The statue is confused.")
            time.sleep(n)
            attack_pattern = True
        elif action == "interact":
            interact(room)
            attack_pattern = True
        elif action == "examine":
            examine(room)
            attack_pattern = True
        elif action == "move":
            y = newy
            move(x, y, room)
            attack_pattern = True
        elif action == "use":
            use(room)
        elif action == "inventory":
            inventory_general()
        elif action == "stop":
            try:
                os.remove("save.txt")
            finally:
                game_on = True
                global game_values
                y = newy
                ending_condition = False
                game_values = [restricted_pos, book_num, n, game_on, x, newx, y, newy, room, combat_state, statue_state, inventory, inv_size, health, weapon, atk_power, ending_condition, one_one_door_interact_state, bookshelf_interact_state, wall_counter, general_backup, one_two_door_interact, one_seven_switch_done]
                game_values.extend([four_nine_switch_done, five_zero_switch_done])
                game_values_string = ["restricted_pos", "book_num", "n", "game_on", "x", "newx", "y", "newy", "room", "combat_state", "statue_state", "inventory", "inv_size", "health", "weapon", "atk_power", "ending_condition", "one_one_door_interact_state", "bookshelf_interact_state", "wall_counter", "general_backup", "one_two_door_interact", "one_seven_switch_done"]
                game_values_string.extend(["four_nine_switch_done", "five_zero_switch_done"])
                file = open("save.txt", "w")
                for x, y in zip(game_values, game_values_string):
                    if y == "x":
                        x = newx
                        file.write("x="+f'{x}'+"\n")
                    elif y == "weapon":
                        txt = "weapon="+f'"{weapon}"'+"\n"
                        file.write(txt)
                    else:
                        txt = str(y+"="+str(x))
                        file.write(txt)
                        file.write("\n")
                file.close()
                game_on = "ended"
                ending_condition = True
                return action, game_on, ending_condition
                sys.exit()
        else:
            print("You can't do that.")
            time.sleep(n)

def death_sequence():
    global game_values_string
    for y in game_values_string:
        exec("global "+y)
    print("You died!")
    time.sleep(n)
    print("Exiting... (if you want to return load previous save.)")
    time.sleep(n)
    file = open("save.txt", "r")
    for x in file:
        exec(x)
    combat_state = False
    room = "nine_five"
    sys.exit()
    return combat_state, game_values


def statue_pattern():
    global health
    crit_chance = random.randint(1, 20)
    if crit_chance == 5:
        health = health - (3*1)
        print("You were damaged for 3 health! (CRIT)")
    else:
        health = health - 1
        print("You were damaged for 1 health!")
    time.sleep(n)
    attack_pattern = False
    return attack_pattern, health
        
def ten_five_attack():
    global statue_health
    crit_chance = random.randint(1, 10)
    if crit_chance == 5:
        statue_health = statue_health - (3*atk_power)
        print("Damaged statue for", (3*atk_power), "damage! (CRIT)")
    else:
        statue_health = statue_health - atk_power
        print("Damaged statue for", atk_power, "damage!")
    time.sleep(n)
    return statue_health

def eleven_five():
    global room
    global ending_condition
    room = "eleven_five"
    freedom_ending()
    ending_condition = True
    return ending_condition

def freedom_ending():
    print("You walk out into the open air, and feel the breeze among your face.")
    time.sleep(3)
    print("You feel comfort and happiness, as you start to walk toward your life again.")
    time.sleep(3)
    print("You are free.")
    time.sleep(3)
    print("ENDING 3 - FREEDOM")
    time.sleep(3)
    print("(This is the True Ending to the game. Now you can restart to find all the secrets this game has to offer.)")
    time.sleep(3)
    sys.exit()



def wall_god_ending():
    print("As you touch the very last wall there is...")
    time.sleep(2)
    print("A godly energy begins to seep from the walls. It manifests into a ghostly being.")
    time.sleep(2)
    print("'Thank you for freeing me...' it says.")
    time.sleep(2)
    print("'You read the book, didn't you? And found how to free me...'")
    time.sleep(2)
    print("'Even if you haven't, I applaud your effort.'")
    time.sleep(2)
    print("'I have been trapped in these walls for many hundreds of years.'")
    time.sleep(2)
    print("'Watching time pass in these narrow halls.'")
    time.sleep(2)
    print("'I could only watch as you went through this complex. Begging for you to touch the walls.'")
    time.sleep(2)
    print("'The walls contain my energy, to be only released upon touch.'")
    time.sleep(2)
    print("'But this place was abandoned. So alas, nothing.")
    time.sleep(2)
    print("'You should continue your adventure. I will roam these lands until I am called upon once again.'")
    time.sleep(2)
    print("'Goodbye, mortal...'")
    time.sleep(2)
    print("The deity floats away. You are confused, but know you have saved a trapped being.")
    time.sleep(2)
    print("ENDING 4 - FREEING THE WALL GOD")
    time.sleep(4)
    sys.exit()

def oob(x, y, newx, newy):
    if newx <= -1 or newy <= -1:
        print("All negative co-ordinates are out of bounds.")
        time.sleep(n)

def move(x, y, room):
    global newx
    global newy
    if combat_state == True:
        move = "edge"
    else:
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
    if len(inventory) == inv_size:
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
    elif item == "apple":
        apple_use()
    elif item == "screen":
        screen_use()
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
    global game_values_string
    global ending_condition
    global game_on
    global combat_state
    global statue_state
    if wall_counter == 37:
        wall_god_ending()
    for x in game_values_string:
        exec("global "+x)
    print()
    if room == "ten_five" and statue_state == "alive" and health > 0:
        for x in range(0, len(locations)):
            y = locations[x]
            if newx == y.xpos and newy == y.ypos:
                eval(y.name+"_combat()")
    elif health == 0:
        death_sequence()
    else:
        room_check(x, y, newx, newy)
        x = newx
        y = newy
        if combat_state == True:
            return x, newx, y, newy
        if room == "eight_eleven":
            ending_condition = True
            game_on = "ended"
            return ending_condition, game_on
        print("Your co-ordinates are", str(x)+", "+str(y)+".")
        time.sleep(n)
        print("You have", health, "health.")
        time.sleep(n)
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
        elif action == "https://youtube.com/watch?v=dQw4w9WgXcQ":
            webbrowser.open("https://youtube.com/watch?v=dQw4w9WgXcQ")
            time.sleep(1)
        elif action == "stop":
            try:
                os.remove("save.txt")
            except Exception:
                game_on = True
                global game_values
                game_values = [restricted_pos, book_num, n, game_on, x, newx, y, newy, room, combat_state, statue_state, inventory, inv_size, health, weapon, atk_power, ending_condition, one_one_door_interact_state, bookshelf_interact_state, wall_counter, general_backup, one_two_door_interact, one_seven_switch_done]
                game_values.extend([four_nine_switch_done, five_zero_switch_done])
                game_values_string = ["restricted_pos", "book_num", "n", "game_on", "x", "newx", "y", "newy", "room", "combat_state", "statue_state", "inventory", "inv_size", "health", "weapon", "atk_power", "ending_condition", "one_one_door_interact_state", "bookshelf_interact_state", "wall_counter", "general_backup", "one_two_door_interact", "one_seven_switch_done"]
                game_values_string.extend(["four_nine_switch_done", "five_zero_switch_done"])
                file = open("save.txt", "w")
                for x, y in zip(game_values, game_values_string):
                    if y == "weapon":
                        txt = "weapon="+f'"{weapon}"'+"\n"
                        file.write(txt)
                    elif y == "statue_state":
                        txt = "statue_state="+f'"{statue_state}"'+"\n"
                        file.write(txt)
                    else:
                        txt = str(y+"="+str(x))
                        file.write(txt)
                        file.write("\n")
                file.close()
                game_on = "ended"
                return action
                sys.exit()
def move(x, y, room):
    global newx
    global newy
    if combat_state == True:
        move = "edge"
    else:
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
        else:
            print("You can't do that.")
            time.sleep(n)
"""
def title_load():
    try:
        print ("  _______        _                  _                 _                       __   ___   ")
        print (" |__   __|      | |        /\      | |               | |                     /_ | / _ \  ")
        print ("    | | _____  _| |_      /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___      | || | | | ")
        print ("    | |/ _ \ \/ / __|    / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \     | || | | | ")
        print ("    | |  __/>  <| |_    / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/     | || |_| | ")
        print ("    |_|\___/_/\_\\___|  /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|     |_(_)___/  ")
        print ("                                                                                         ")
    except SyntaxWarning:
        pass
"""   
def game_load():
    global game_on
    time_check()
    print("Enter 'stop' to exit and save your game. NOTE: CLOSING DIRECTLY DOES NOT SAVE")
    time.sleep(1)
    game_on = True
    return game_on
    
while game_on == False:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
    start = input("Turn game on? (yes/no): ")
    if start == "yes":
        title_load()
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
                for x in file:
                    exec(x)
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
    if ending_condition == True or action == "stop":
        sys.exit()
        game_on = False
        break
    elif action == "stop":
        sys.exit()
        ending_condition = True
        game_on = False
        break
    repeated_action(x, y, newx, newy, wall_counter)
    
