from turtle import *
import turtle
import random 
import math

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)

a = Ball(5,"blue",1)
a.pu()
a.goto(100,100)
a.pd()
b = Ball(3,"red",1)
b.pu()
b.goto(100,100)
b.pd()

ball1_x = a.xcor()
ball1_y = a.cor()
ball2_x = b.xcor()
ball2_y = b.ycor()

def collisions(ball1,ball2):
	if (ball1.shapesize()[0]+ball2.shapesize()[0]) > math.sqrt((math.pow))

	ball1.color("green")
	ball2.color("yellow")

collisions(a,b)