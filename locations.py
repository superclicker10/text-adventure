from location import *

lobby = location(0, 0) # no edges
book_room = location(1, 0) # north, east, south-east edges
one_one_corridor = location(1, 1) # south edge
one_two_corridor = location(1, 2) # north edge
one_three_lobby = location(1, 3) # east, south edge
lectern_room = location(2, 3) # no edges

#book room has edges north, east, and south-east leading to door, bookshelf and hole respectively

locations = [lobby, book_room, one_one_corridor, one_two_corridor, one_three_lobby, lectern_room]

door_interact = False
bookshelf_interact = False

