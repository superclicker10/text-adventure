import time

class location():
    def __init__(self, xpos, ypos, name):
        self.xpos = xpos
        self.ypos = ypos
        self.name = name

    def __str__(self):
        return f"{self.xpos}{self.ypos}"

    def testoutput(self):
        print("This square is at position " + self.xpos + self.ypos)
