import drawsvg 
import random
import datetime

now = str(datetime.datetime.now()).replace(" ","_").replace(":","_")

def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)

class Tree:
    def __init__(self,x,y,r,g,b,d,draw_function,growth_function,growth_limit_function,validation_function,color_function):
        self.branches = []
        self.drawing = d
        self.x2 = x
        self.y2 = y
        self.red = r 
        self.green = g 
        self.blue = b
        self.length_to_root = 0
        self.tree = self
        self.color_function = color_function
        self.validate_function = validation_function
        self.grow_function = growth_function
        self.limit_growth_function = growth_limit_function
        self.draw_function = draw_function

    def has(self,x,y):
        for branch in self.branches:
            if branch.has(x,y):
                return True
        return False

    def add_branch(self,branch):
        self.branches.append(branch)

    def start(self):
        branch = Branch(self,self.x2,self.y2)
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
        self.color_function = origin.color_function
        self.set_color()
        self.validate_function = origin.validate_function
        self.draw_function = origin.draw_function
        self.grow_function = origin.grow_function
        self.limit_growth_function = origin.limit_growth_function
        self.validate()

    def grow(self):
        return self.grow_function(self)
    def validate(self):
        return self.validate_function(self)
    def limit_growth(self):
        return self.limit_growth_function(self)
    def draw(self):
        return self.draw_function(self)
        
    def set_color(self):
        self.color_function(self)
    
    def __str__(self):
        return "branch:" + str(self.x1) + "," + str(self.y1) + "|" + str(self.x2) + "," + str(self.y2) + "|" + rgb_to_hex(self.red,self.blue,self.green) + "|" + str(self.length_to_root)


    def isValid(self):
        return self.valid

    def add_child(self,child):
        self.children.append(child)

    def has(self,x,y):
        return (self.x1 == x and self.y1 == y) or (self.x2 == x and self.y2 == y)

def straight_southeast_grow(branch):
    if branch.limit_growth():
        return
    new_branch = Branch(branch,branch.x2+5,branch.y2+5)
    if new_branch.isValid():
        new_branch.grow()

def westward_tree_grow(branch):
    if branch.limit_growth():
        return
    x = random.randint(0,2)
    branch1 = False
    if x != 0:
        branch1 = Branch(branch,branch.x2-5,branch.y2-5)
    x = random.randint(0,2)
    branch2 = False
    if x != 0:
        branch2 = Branch(branch,branch.x2-5,branch.y2)
    x = random.randint(0,2)
    branch3 = False
    if x != 0:
        branch2 = Branch(branch,branch.x2,branch.y2-5)
    x = random.randint(0,5)
    branch4 = False
    if x != 0:
        branch4 = Branch(branch,branch.x2,branch.y2+5)
    if x == 0:
        if branch3 and branch3.isValid():
            branch3.grow()
        if branch2 and branch2.isValid():
            branch2.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
    if x == 5:
        if branch3 and branch3.isValid():
            branch3.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
        if branch2 and branch2.isValid():
            branch2.grow()
    if x == 1:
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
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
        if branch4 and branch4.isValid():
            branch4.grow()
    if x == 3:
        if branch2 and branch2.isValid():
            branch2.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
        if branch3 and branch3.isValid():
            branch3.grow()
    if x == 4:
        if branch2 and branch2.isValid():
            branch2.grow()
        if branch3 and branch3.isValid():
            branch3.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()



def eastward_tree_grow(branch):
    if branch.limit_growth():
       return
    x = random.randint(0,2)
    branch1 = False
    if x != 0:
        branch1 = Branch(branch,branch.x2+5,branch.y2+5)
    x = random.randint(0,2)
    branch2 = False
    if x != 0:
        branch2 = Branch(branch,branch.x2+5,branch.y2)
    x = random.randint(0,2)
    branch3 = False
    if x != 0:
        branch2 = Branch(branch,branch.x2,branch.y2+5)
    x = random.randint(0,5)
    branch4 = False
    if x != 0:
        branch4 = Branch(branch,branch.x2,branch.y2-5)
    if x == 0:
        if branch3 and branch3.isValid():
            branch3.grow()
        if branch2 and branch2.isValid():
            branch2.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
    if x == 5:
        if branch3 and branch3.isValid():
            branch3.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
        if branch2 and branch2.isValid():
            branch2.grow()
    if x == 1:
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
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
        if branch4 and branch4.isValid():
            branch4.grow()
    if x == 3:
        if branch2 and branch2.isValid():
            branch2.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()
        if branch3 and branch3.isValid():
            branch3.grow()
    if x == 4:
        if branch2 and branch2.isValid():
            branch2.grow()
        if branch3 and branch3.isValid():
            branch3.grow()
        if branch1 and branch1.isValid():
            branch1.grow()
        if branch4 and branch4.isValid():
            branch4.grow()


def line_draw(branch):
    branch.drawing.append(drawsvg.Line(branch.x1,branch.y1,branch.x2,branch.y2,fill="#eeee00",stroke=rgb_to_hex(branch.red,branch.green,branch.blue)))

def bezier_draw(branch):
    b = drawsvg.Path(stroke=rgb_to_hex(branch.red,branch.green,branch.blue),fill="transparent",stroke_width=1)
    branch.drawing.append(b.M(branch.x1,branch.y1).Q(branch.x1, branch.x2, branch.x2, branch.y2))

def line_with_circle_draw(branch):
    branch.drawing.append(drawsvg.Line(branch.x1,branch.y1,branch.x2,branch.y2,fill="#eeee00",stroke=rgb_to_hex(branch.red,branch.green,branch.blue)))
    branch.drawing.append(drawsvg.Circle(branch.x2,branch.y2,1,fill="white", stroke=rgb_to_hex(branch.red,branch.green,branch.blue)))

def line_with_circle_growing_draw(branch):
    branch.drawing.append(drawsvg.Line(branch.x1,branch.y1,branch.x2,branch.y2,fill="#eeee00",stroke=rgb_to_hex(branch.red,branch.green,branch.blue)))
    g = branch.length_to_root/4
    branch.drawing.append(drawsvg.Circle(branch.x2,branch.y2,g,fill="transparent", stroke=rgb_to_hex(branch.red,branch.green,branch.blue)))

def default_limit_growth(xmax, ymax,xmin,ymin,lengthmax):
    def output(branch):
        if branch.x2 >= xmax or branch.y2 >= ymax or branch.x2 <= xmin or branch.y2 <= ymin:
            return True
        if branch.length_to_root >= lengthmax:
            return True
        return False
    return output

def base_validation(branch):
    if not branch.tree.has(branch.x2,branch.y2):
        branch.valid = True
        branch.draw()
        branch.tree.add_branch(branch)

def default_color_function(branch):
    branch.red = branch.origin.red
    branch.green = branch.origin.green
    branch.blue = branch.origin.blue

def increase_green_color_function(branch):
    branch.red = branch.origin.red
    branch.blue = branch.origin.blue
    if branch.origin.green < 255:
        branch.green = branch.origin.green + 4

d = drawsvg.Drawing(410,410,origin="center")

#        x,y,d,draw_function,   growth_function,               growth_limit_function,      validation_function):
t = Tree(0,0,0,0,0,d,line_draw,westward_tree_grow,default_limit_growth(200,200,-200,-200,40),base_validation,increase_green_color_function)

t.start()

now = ""
p = drawsvg.Path(stroke='black', fill='none', stroke_width=1)
d.append(p.M(0, 0).Q(0, 5, 5, 5))

d.save_svg("leaf1" + now + ".svg")
