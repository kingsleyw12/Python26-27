#myfunctions
import turtle
bob = turtle.Turtle()

def polygon(distance, sides, c):
    bob.color(c)
    angle = 360/sides
    
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def cloud(x, y):
    jump(x, y)
    bob.begin_fill()
    bob.color("gray")
    bob.circle(50)
    jump(-25 + x , -30 + y)
    bob.circle(50)
    bob.end_fill()
    
def tree(x, y):
    jump(x, y)
    bob.width(5)
    bob.color("brown")
    polygon(50, 4)
    bob.color("green")
    polygon(100, 3)

def square(size):
    bob.width("4")
    bob.color("red")
    for times in range(4):
        bob.forward(size)
        bob.left(90)

def triangle(size):
    bob.width("5")
    bob.color("blue")
    for times in range(3):
        bob.forward(size)
        bob.left(120)

def grass(x, y):
    jump(-300, -300)
    for times in range(5):
        bob.color("green")
        bob.forward(100)
        bob.penup()
        jump(-250, -300)
        bob.pendown()
        bob.forward(100)
        bob.penup()
        jump(-200, -300)
        bob.pendown()
        bob.forward(100)
        bob.penup()
        jump(-150, -300)
        bob.pendown()
        bob.forward(100)
        bob.penup()
        jump(-100, -300)
        bob.pendown()
        bob.forward(100)
        bob.penup()
        jump(-50, -300)
        bob.pendown()#myfunctions
import turtle
bob = turtle.Turtle()

def polygon(distance, sides, c):
    bob.color(c)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def cloud(x, y):
    bob.begin_fill()
    bob.color("gray")
    bob.circle(50)
    bob.end_fill()
    bob.penup()
    bob.forward(25)
    bob.pendown()
    bob.begin_fill()
    bob.circle(50)
    bob.end_fill()

def cloud1(x, y):
    bob.begin_fill()
    bob.color("gray")
    bob.circle(50)
    bob.end_fill()
    bob.penup()
    bob.forward(25)
    bob.pendown()
    bob.begin_fill()
    bob.circle(50)
    bob.end_fill()
    
def tree(x, y):
    jump(x, y)
    bob.width(5)
    bob.color("brown")
    polygon(50, 4)
    bob.color("green")
    polygon(100, 3)

def square(size):
    bob.width("4")
    bob.color("red")
    bob.forward(100)
    bob.penup()
    jump(0, -300)
    bob.pendown()


def pentagon(size):
    bob.width("3")
    bob.color("pink")
    for times in range(5):
        bob.forward(size)
        bob.left(72)

def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()

def comet(distance, angle):
    for times in range(10):
        bob.width(times)
        bob.forward(distance)
        bob.left(angle)

def spiral():
    for times in range(5):
        bob.width(times)
        bob.forward(20)
        bob.left(10)

def stair(distance, amount):
    for times in range(amount):
        bob.forward(distance)
        bob.left(90)
        bob.forward(distance)
        bob.right(90)

def circle(radius):
    bob.color("yellow")
    bob.circle(radius)

def drop(radius):
    bob.color("cadetblue3")
    bob.circle(radius)
