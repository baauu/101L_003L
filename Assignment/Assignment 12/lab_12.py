##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 12
##
##########################################

import turtle

'''turtle.forward(100)
turtle.right(90)
turtle.forward(50)

turtle.circle(40)'''

'''turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()'''

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.c = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.c)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):

        turtle.dot()


'''p = Point(-100, 100, "blue")
p.draw()'''
#down 


class Box(Point):

    def __init__(self, x1, y1, width, height, color):

        super().__init__(x1, y1, color)
        self.w = width
        self.h = height

    def draw_action(self):
        #draw a box
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.setheading(0)
        turtle.color(self.c)
        turtle.pendown()
        turtle.forward(self.w)
        turtle.right(90)
        turtle.forward(self.h)
        turtle.right(90)
        turtle.forward(self.w)
        turtle.right(90)
        turtle.forward(self.h)

'''b = Box(-100, 100, 50, 20, "blue")
b.draw()'''
#created underneath

class BoxFilled(Box):

    def __init__ (self, x1, y1, width, height, color, fillcolor):

        super().__init__(x1, y1, width, height, color)
        self.fill = fillcolor

    def draw_action(self):

        turtle.begin_fill()
        Box.draw_action(self)
        turtle.fillcolor(self.fill)
        turtle.end_fill()

class Circle(Point):
    
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.rad = radius

    def draw_action(self):

        turtle.penup()
        turtle.goto(self.x, self.y-self.rad)
        turtle.setheading(0)
        turtle.color(self.c)
        turtle.pendown()
        turtle.circle(self.rad)

class CircleFilled(Circle):

    def __init__(self, x1, y1, radius, color, fill_color):

        super().__init__(x1, y1, radius, color)
        self.fc = fill_color
    
    def draw_action(self):

        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.fillcolor(self.fc)
        turtle.end_fill()



p = Point(-100, 100, "blue")
p.draw()

b = Box(100, 100, 50, 20, "blue")
b.draw_action()

b = BoxFilled(1, 2, 100, 200, "red", "blue")
b.draw_action()

c = Circle(-200, 60, 20, "red")
c.draw_action()

cf = CircleFilled(300, -60, 100, "blue", "red")
cf.draw_action()

        


