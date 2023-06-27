import time
def book():
    print("This is the tutorial book!")
    time.sleep(3)
    while True:
        tutorial = input("What would you like to know about? (interact, examine, move, use, inventory, items, book generation, walls, leave): ")
        if tutorial == "interact":
            print("Interacting with an item either causes an item to be gained, or for something to occur or activate.")
            time.sleep(2)
            print("Sometimes this may be an ending, or a switch for another location.")
            time.sleep(2)
        elif tutorial == "examine":
            print("Examining an item reveals extra information about that item.")
            time.sleep(2)
            print("It may help you to solve a puzzle that you didn't know initially.")
            time.sleep(2)
        elif tutorial == "move":
            print("Moving means going to another location that is neither negative, nor restricted.")
            time.sleep(2)
            print("Often this will be revealed to you in location descriptions.")
            time.sleep(2)
            print("+x is for east, -x is for west, +y is for north, -y is for south.")
            time.sleep(2)
            print("Moving to an edge also allows you to access extra information in some locations.")
            time.sleep(2)
        elif tutorial == "use":
            print("When you get an item, often via interaction, it is put into your inventory and used.")
            time.sleep(2)
            print("Often there will be an indication to use an item.")
            time.sleep(2)
        elif tutorial == "inventory":
            print("Viewing your inventory lets you know what you have, should you forget.")
            time.sleep(2)
            print("Dropping an item means it goes out of your inventory, should you want to or not have enough space.")
            time.sleep(2)
        elif tutorial == "items":
            print("Items usually have specific functions to the storyline, or for easter eggs.")
            time.sleep(2)
            print("You get these items via interactions or random events.")
            time.sleep(2)
        elif tutorial == "book generation":
            print("There are three books in the game, and this is one of them.")
            time.sleep(2)
            print("You have a 1/40 chance to get another, and 1/1000 chance to get another.")
            time.sleep(2)
            print("This chance is refreshed every time you launch the game.")
            time.sleep(2)
        elif tutorial == "walls":
            print("Read the wall lore book for more information.")
            time.sleep(2)
        elif tutorial == "leave":
            break
        
def fish_book():
    print("Test")

def wall_lore_book():
    print("Test")
#IMPLEMENT THESE (NUTS)
