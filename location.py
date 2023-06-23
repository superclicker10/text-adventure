import time

class location():
    def __init__(self, xpos, ypos, edgeplusx, edgeminusx, edgeplusy, edgeminusy):
        self.xpos = xpos
        self.ypos = ypos
        """
        self.edgeplusx = edgeplusx
        self.edgeminusx = edgeminusx
        self.edgeplusy = edgeplusy
        self.edgeminusy = edgeminusy
        """

    def __str__(self):
        return f"{self.xpos}{self.ypos}"

    def testoutput(self):
        print("This square is at position " + self.xpos + self.ypos)
"""
class edge():
    def __init__(self, xpos, ypos):
        self.plusxedge = xpos
        self.minusxedge = xpos
        self.plusyedge = ypos
        self.minusyedge = ypos

    def __str__(self):
        return f"{self.plusxpos}{self.minusxpos}{self.plusypos}{self.minusypos}"
"""
