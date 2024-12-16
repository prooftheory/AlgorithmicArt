import drawsvg 
import random
import datetime

now = str(datetime.datetime.now()).replace(" ","_").replace(":","_")

def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)

class Tree:
    def __init__(self,x,y,d):
        self.branches = []
        self.drawing = d
        self.x2 = x
        self.y2 = y
        self.red = 200
        self.green = 200
        self.blue = 200
        self.length_to_root = 0
        self.tree = self

    def has(self,x,y):
        for branch in self.branches:
            if branch.has(x,y):
                return True
        return False

    def add_branch(self,branch):
        self.branches.append(branch)

    def grow(self):
        branch = Branch(self,self.x2+5,self.y2)
        branch.grow()

    def __str__(self):
        out = "tree:\n"
        for branch in self.branches:
            out += str(branch) + "\n"
        return out
    
class Branch:

    def __init__(self,origin,x2,y2):
        self.valid = False
        self.x2 = x2
        self.y2 = y2
        self.children = []
        self.origin = origin
        self.tree = origin.tree
        self.length_to_root = origin.length_to_root + 1
        self.x1 = origin.x2
        self.y1 = origin.y2
        self.drawing = origin.drawing 
        self.red = 200
        if origin.red == 200:
            self.red = 150
        self.blue = origin.blue
        self.green = origin.green
        if not self.tree.has(self.x2,self.y2):
            self.valid = True
            self.draw()
            self.tree.add_branch(self)

    def draw(self):
        self.drawing.append(drawsvg.Line(self.x1,self.y1,self.x2,self.y2,fill="#eeee00",stroke=rgb_to_hex(self.red,self.green,self.blue)))

    def isValid(self):
        return self.valid

    def add_child(self,child):
        self.children.append(child)

    def has(self,x,y):
        return (self.x1 == x and self.y1 == y) or (self.x2 == x and self.y2 == y)

    def grow(self):
        if self.x2 >= 400 or self.y2 >= 400:
            return
        #if self.length_to_root >= 40:
        #    return
        x = random.randint(0,2)
        branch1 = False
        if x != 0:
            branch1 = Branch(self,self.x2+5,self.y2+5)
        x = random.randint(0,2)
        branch2 = False
        if x != 0:
            branch2 = Branch(self,self.x2+5,self.y2)
        x = random.randint(0,2)
        branch3 = False
        if x != 0:
            branch2 = Branch(self,self.x2,self.y2+5)
        x = random.randint(0,5)
        if x == 0:
            if branch3 and branch3.isValid():
                branch3.grow()
            if branch2 and branch2.isValid():
                branch2.grow()
            if branch1 and branch1.isValid():
                branch1.grow()
        if x == 5:
            if branch3 and branch3.isValid():
                branch3.grow()
            if branch1 and branch1.isValid():
                branch1.grow()
            if branch2 and branch2.isValid():
                branch2.grow()
        if x == 1:
            if branch1 and branch1.isValid():
                branch1.grow()
            if branch3 and branch3.isValid():
                branch3.grow()
            if branch2 and branch2.isValid():
                branch2.grow()
        if x == 2:
            if branch1 and branch1.isValid():
                branch1.grow()
            if branch2 and branch2.isValid():
                branch2.grow()
            if branch3 and branch3.isValid():
                branch3.grow()
        if x == 3:
            if branch2 and branch2.isValid():
                branch2.grow()
            if branch1 and branch1.isValid():
                branch1.grow()
            if branch3 and branch3.isValid():
                branch3.grow()
        if x == 4:
            if branch2 and branch2.isValid():
                branch2.grow()
            if branch3 and branch3.isValid():
                branch3.grow()
            if branch1 and branch1.isValid():
                branch1.grow()


    def __str__(self):
        return "branch:" + str(self.x1) + "," + str(self.y1) + "|" + str(self.x2) + "," + str(self.y2) + "|" + rgb_to_hex(self.red,self.blue,self.green) + "|" + str(self.length_to_root)



d = drawsvg.Drawing(410,410,origin="center")

t = Tree(-170,-170,d)

t.grow()

now = ""

d.save_svg("leaf1" + now + ".svg")
