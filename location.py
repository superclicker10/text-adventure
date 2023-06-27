import time

class location():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def __str__(self):
        return f"{self.xpos}{self.ypos}"

    def testoutput(self):
        print("This square is at position " + self.xpos + self.ypos)
