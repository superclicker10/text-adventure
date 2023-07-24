from location import *

lobby = location(0, 0, "lobby") # no edges
zero_four = location(0, 4, "zero_four") # no edges
zero_five = location(0, 5, "zero_five") # no edges
zero_six = location(0, 6, "zero_six") # no edges
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
three_six = location(3, 6, "three_six") # no edges
four_four = location(4, 4, "four_four") # east edge
four_five = location(4, 5, "four_five") # east edge
four_six = location(4, 6, "four_six") # east edge
four_seven = location(4, 7, "four_seven") # no edges
four_eight = location(4, 8, "four_eight") # no edges
four_nine = location(4, 9, "four_nine") # no edges
five_zero = location(5, 0, "five_zero") # no edges
five_one = location(5, 1, "five_one") # no edges
five_two = location(5, 2, "five_two") # no edges
five_three = location(5, 3, "five_three") # no edges
five_four = location(5, 4, "five_four") # no edges
five_five = location(5, 5, "five_five") # no edges
five_six = location(5, 6, "five_six") # no edges
six_four = location(6, 4, "six_four") # no edges
six_five = location(6, 5, "six_five") # no edges
six_six = location(6, 6, "six_six") # no edges
seven_four = location(7, 4, "seven_four") # no edges
seven_five = location(7, 5, "seven_five") # no edges
seven_six = location(7, 6, "seven_six") # no edges
eight_four = location(8, 4, "eight_four") # no edges
eight_five = location(8, 5, "eight_five") # no edges
eight_six = location(8, 6, "eight_six") # no edges
eight_ten = location(8, 10, "eight_ten") # no edges
eight_eleven = location(8, 11, "eight_eleven") # no edges
nine_three = location(9, 3, "nine_three") # no edges
nine_four = location(9, 4, "nine_four") # no edges
nine_five = location(9, 5, "nine_five") # east edge
nine_six = location(9, 6, "nine_six") # no edges
nine_seven = location(9, 7, "nine_seven") # no edges
nine_eight = location(9, 8, "nine_eight") # no edges
nine_nine = location(9, 9, "nine_nine") # no edges
nine_ten = location(9, 10, "nine_ten") # no edges


#book room has edges north, east, and south-east leading to door, bookshelf and hole respectively

locations = [lobby, zero_four, zero_five, zero_six, book_room, one_one_corridor, one_two_corridor, one_three, one_four, one_five, one_six, one_seven, lectern_room, two_four, two_five, two_six, three_four, three_five, three_six]
locations.extend([four_four, four_five, four_six, four_seven, four_eight, four_nine, five_zero, five_one, five_two, five_three, five_four, five_five, five_six, six_four, six_five, six_six])
locations.extend([seven_four, seven_five, seven_six, eight_four, eight_five, eight_six, eight_ten, eight_eleven, nine_three, nine_four, nine_five, nine_six, nine_seven, nine_eight, nine_nine, nine_ten])
multiple_edges = [book_room, one_three, one_six]
no_edges = [lobby, zero_four, zero_five, zero_six, one_seven, lectern_room, two_five, two_six, three_four, three_five, three_six, four_seven, four_eight, four_nine, five_zero, five_one, five_two, five_three, five_four, five_five, five_six]
no_edges.extend([six_four, six_five, six_six, seven_four, seven_five, seven_six, eight_four, eight_five, eight_six, eight_eleven, nine_three, nine_four, nine_six, nine_seven, eight_ten, nine_eight, nine_nine, nine_ten])
no_examine = [lobby, two_four, two_five, two_six, three_four, three_five, three_six, four_seven, four_eight, five_one, five_two, five_three, five_four, five_five, five_six, six_four]
no_examine.extend([six_five, six_six, seven_four, seven_six, eight_four, eight_five, eight_six, eight_eleven, nine_four, nine_six, eight_ten, nine_eight, nine_nine, nine_ten])
no_interact = [one_four, one_six, one_five, two_four, two_five, three_five, four_five, five_four, four_six, five_five, six_five, eight_five, eight_eleven]

door_interact = False
bookshelf_interact = False

