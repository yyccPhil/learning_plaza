# Introduction and Efficiency

## Python Practice
"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
        self.classydict = {"tophat" : 2,
                            "bowtie" : 4,
                            "monocle" : 5}
        
    def addItem(self, str):
        self.items.append(str)
        
    def getClassiness(self):
        point = 0
        for i in self.items:
            point += self.classydict.get(i, 0)
        
        return point

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()

## Python: The Basics

# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!

def show_excitement():
    # Your code goes here!
    a = ""
    for i in range(5):
        a += "I am super excited for this course! "
    return a.strip()
