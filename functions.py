from location import *
from locations import *
from story import *

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
        elif room == "one_one_corridor":
            one_one_southedge()
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
    global wall_counter
    global lobby_wall
    obj_interact = input("What would you like to interact with?: ")
    if room == "lobby":
        if obj_interact == "wall":
            print("You touch the wall. It's cold.")
            time.sleep(1)
            if lobby_wall == False:
                wall_counter = wall_counter + 1
            lobby_wall = True
            return lobby_wall, wall_counter
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
        else:
            print("You can't interact with that.")
    elif room == "one_two_corridor":
        if obj_interact == "door":
            one_two_door()
        elif obj_interact == "wall":
            one_two_wall()
        else:
            print("You can't interact with that.")
            

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
