def example():
    global example_door_state
    if obj_interact == "door":
        example_door(example_door_state)
        if example_door_state == True:
            door_interact_state == False

def example_door(example_door_state):
    if example_door_state == False:
        print("Description would go here")
    else:
        print("Alternate description goes here")
        
    
