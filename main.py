#main.py

from myfunctions import *

from random import randint

#bg
turtle.bgcolor("cadetblue1")
bob.speed(0)
bob.shape("turtle")
bob.color("white")
turtle.colormode(255)

bob.right(90)
polygon(500, 4, "green")
bob.right(90)
polygon(500, 4, "green")

bob.right(180)

#flower1
bob.color("green2")
bob.width(10)
jump(0, -50)
bob.right(90)
bob.forward(400)
jump(0, 0)
for times in range(5):
    polygon(50, 6, "red")
    polygon(50, 5, "blue")
    polygon(50, 4, "green")
    
    bob.left(72)

polygon(50, 4, "green")

jump(-35, 0)
bob.begin_fill()
circle(30)
bob.end_fill()

#flower2

jump(-200, -35)
bob.color("green2")
bob.width(10)
bob.forward(400)
jump(-200, 0)



for times in range(5):
    bob.width(1)
    polygon(50, 6, "blue4")
    polygon(50, 5, "magenta")
    polygon(50, 4, "pink")
    bob.left(72)

polygon(50, 4, "pink")

jump(-225, 0)
bob.begin_fill()
circle(30)
bob.end_fill()

#clouds
jump(250, 250)
bob.left(90)
for times in range(4):
    cloud(200, 200)
jump(260, 275)
for times in range(3):
    cloud1(260, 260)

jump(0, 250)
for times in range(4):
    cloud(0, 200)
jump(10, 275)
for times in range(3):
    cloud1(10, 260)

jump(-200, 250)
for times in range(4):
    cloud(-200, 200)
jump(-190, 275)
for times in range(3):
    cloud1(-200, 260)

#raindrops
jump(100, 100)
for times in range(4):
    bob.begin_fill()
    drop(15)
    bob.end_fill()
    bob.penup()
    bob.forward(75)
    bob.left(20)
    bob.pendown()

bob.right(50)
jump(80, 120)
for times in range(3):
    bob.begin_fill()
    drop(15)
    bob.end_fill()
    bob.penup()
    bob.forward(75)
    bob.left(20)
    bob.pendown()

bob.right(40)
jump(-50, 100)
for times in range(3):
    bob.begin_fill()
    drop(15)
    bob.end_fill()
    bob.penup()
    bob.forward(75)
    bob.left(20)
    bob.pendown()

bob.right(80)
jump(-200, 100)
for times in range(3):
    bob.begin_fill()
    drop(15)
    bob.end_fill()
    bob.penup()
    bob.forward(75)
    bob.left(10)
    bob.pendown()

#sun
jump(-400, 350)
bob.begin_fill()
bob.color("yellow")
bob.circle(80)
bob.end_fill()

#ant hole
bob.right(60)
jump(100, 0)
bob.begin_fill()
bob.color("brown")
for times in range(50):
    bob.forward(1)
    bob.left(1)

bob.right(50)
for times in range(10):
    bob.forward(1)
    bob.right(2)

for times in range(10):
    bob.forward(1)
    bob.left(3)

bob.right(60)
for times in range(40):
    bob.forward(1)
    bob.left(1)
bob.end_fill()


#ants
bob.left(9)
jump(150, 20)
bob.begin_fill()
bob.color("black")
bob.circle(5)
bob.end_fill()
bob.forward(5)
bob.begin_fill()
bob.circle(5)
bob.end_fill()

jump(200, 0)
bob.begin_fill()
bob.color("black")
bob.circle(5)
bob.end_fill()
bob.forward(5)
bob.begin_fill()
bob.circle(5)
bob.end_fill()

jump(230, 0)
bob.begin_fill()
bob.color("black")
bob.circle(5)
bob.end_fill()
bob.forward(5)
bob.begin_fill()
bob.circle(5)
bob.end_fill()

jump(260, 0)
bob.begin_fill()
bob.color("black")
bob.circle(5)
bob.end_fill()
bob.forward(5)
bob.begin_fill()
bob.circle(5)
bob.end_fill()

jump(300, 0)
bob.begin_fill()
bob.color("black")
bob.circle(5)
bob.end_fill()
bob.forward(5)
bob.begin_fill()
bob.circle(5)
bob.end_fill()

#tree
jump(-320, 0)
bob.right(180)
bob.begin_fill()
bob.color("brown")
for times in range(90):
    bob.forward(1)
    bob.right(1)
bob.forward(150)
bob.left(92)
bob.forward(50)
bob.left(90)
bob.forward(150)
for times in range(90):
    bob.forward(1)
    bob.right(1)
bob.end_fill()


jump(-435, 205)
bob.color("green")
bob.left(180)
for times in range(4):
    bob.begin_fill()
    bob.circle(35)
    bob.end_fill()
    bob.forward(25)

jump(-420, 240)
bob.color("green")
for times in range(3):
    bob.begin_fill()
    bob.circle(35)
    bob.end_fill()
    bob.forward(25)
