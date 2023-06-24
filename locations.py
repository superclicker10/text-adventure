from location import *

lobby = location(0, 0, False, False, False, False)
book_room = location(1, 0, True, False, False, True)
one_one_corridor = location(1, 1, False, False, False, True)
one_two_corridor = location(1, 2, True, False, False, False)
#book room has edges north, east, and south-east leading to door, bookshelf and hole respectively

locations = [lobby, book_room, one_one_corridor, one_two_corridor]

door_interact = False
bookshelf_interact = False

