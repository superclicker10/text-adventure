from location import *

lobby = location(0, 0, False, False, False, False)
book_room = location(1, 0, True, False, False, True)
corridor = location(1, 1, False, False, False, True)
#book room has edges north, east, and south-east leading to door, bookshelf and hole respectively

locations = [lobby, book_room, corridor]

door_interact = False
bookshelf_interact = False

