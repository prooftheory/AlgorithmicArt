import drawsvg as draw
import random

def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)

class Tree:
    def __init__(self,x,y,d):
        self.branches = []
        self.drawing = d
        self.x = x
        self.y = y

    def has(self,x,y):
        for branch in self.branches:
            if branch.has(x,y):
                return True
        return False

    def add_branch(self,branch):
        self.branches.append(branch)

    def get_drawing(self):
        return self.drawing
    
    def grow(self):
        branch = Branch(self,self.x,self.y,self.x,self.y-10,200,200,200)
        self.branches.append(branch)
        branch.grow()

    def __str__(self):
        out = ""
        for branch in self.branches:
            out += str(branch) + "\n"
        return out
    
class Branch:
    def __init__(self,tree,x1,y1,x2,y2,red,blue,green):
        self.tree = tree
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.drawing = tree.get_drawing()
        self.red = red
        self.blue = blue
        self.green = green 
        self.drawing.append(draw.Line(x1,y1,x2,y2,fill="#eeee00",stroke=rgb_to_hex(red,blue,green)))

    def has(self,x,y):
        return (self.x1 == x and self.y1 == y) or (self.x2 == x and self.y2 == y)

    def grow(self):
        branch1 = False
        branch2 = False
        branch3 = False
        new_red = self.red
        if self.red == 200:
            new_red = 150 
        if self.red == 150:
            new_red = 200

        x = random.randint(0,2)
        if x != 0 and self.x2 < 400 and self.y2 < 400 and not self.tree.has(self.x2+5,self.y2+5):
            branch1 = Branch(self.tree,self.x2,self.y2,self.x2+5,self.y2+5,new_red,self.blue,self.green)
            self.tree.add_branch(branch1)
            terminal = False
        y = random.randint(0,2)
        if y != 0 and self.x2 < 400 and not self.tree.has(self.x2+5,self.y2):
            branch2 = Branch(self.tree,self.x2,self.y2,self.x2+5,self.y2,new_red,self.blue,self.green)
            self.tree.add_branch(branch2)
            terminal = False
        z = random.randint(0,2)
        if z != 0 and self.y2 < 400 and not self.tree.has(self.x2,self.y2+5):
            branch3 = Branch(self.tree,self.x2,self.y2,self.x2,self.y2+5,new_red,self.blue,self.green)
            self.tree.add_branch(branch3)
            terminal = False
        x = random.randint(0,2)
        if x == 0:
            if branch3:
                branch3.grow()
            if branch2:
                branch2.grow()
            if branch1:
                branch1.grow()
        if x == 1:
            if branch2:
                branch2.grow()
            if branch1:
                branch1.grow()
            if branch3:
                branch3.grow()
        if x == 2:
            if branch1:
                branch1.grow()
            if branch3:
                branch3.grow()
            if branch2:
                branch2.grow()

    def __str__(self):
        return str(self.x1) + "," + str(self.y1) + "|" + str(self.x2) + "," + str(self.y2) + "|" + rgb_to_hex(self.red,self.blue,self.green) 


   


    


d = draw.Drawing(410,410,origin="center")

t = Tree(-170,-170,d)

t.grow()

print(t)

d.save_svg("art.svg")
