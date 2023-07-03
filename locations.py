from location import *

lobby = location(0, 0, "lobby") # no edges
zero_four = location(0, 4, "zero_four") # east edge
book_room = location(1, 0, "book_room") # north, east, south-east edges
one_one_corridor = location(1, 1, "one_one_corridor") # south edge
one_two_corridor = location(1, 2, "one_two_corridor") # north edge
one_three = location(1, 3, "one_three") # east, south edge
one_four = location(1, 4, "one_four") # west edge
one_five = location(1, 5, "one_five") # west edge
one_six = location(1, 6, "one_six") # west, north edge
one_seven = location(1, 7, "one_seven") # no edges
lectern_room = location(2, 3, "lectern_room") # no edges
two_four = location(2, 4, "two_four") # south edge
two_five = location(2, 5, "two_five") # no edges
two_six = location(2, 6, "two_six") # no edges
three_four = location(3, 4, "three_four") # no edges
three_five = location(3, 5, "three_five") # no edges
three_six = location(3, 6, "three_six")

#book room has edges north, east, and south-east leading to door, bookshelf and hole respectively

locations = [lobby, zero_four, book_room, one_one_corridor, one_two_corridor, one_three, one_four, one_five, one_six, one_seven, lectern_room, two_four, two_five, two_six, three_four, three_five, three_six]
multiple_edges = [book_room, one_three, one_six]
no_edges = [lobby, one_seven, lectern_room, two_five, two_six, three_four, three_five, three_six]
no_examine = [lobby, two_four, two_five, two_six, three_four, three_five, three_six]
no_interact = [one_four, one_six, one_five, two_four, two_five, three_five]

door_interact = False
bookshelf_interact = False

