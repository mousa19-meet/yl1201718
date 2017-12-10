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

b = Ball(3,"red",1)

c = Ball(3,"black",1)


ball_list =[a,b,c]

ball1_x = a.xcor()
ball1_y = a.ycor()
ball2_x = b.xcor()
ball2_y = b.ycor()
placex = random.randint(-100,100)
placey = random.randint(-100,100)

def collisions(ball1,ball2): 
	if (ball1.shapesize()[0]+ball2.shapesize()[0]) > math.sqrt(math.pow(ball1_x-ball2_x,2)+math.pow(ball1_y-ball2_y,2)):
		ball1.color("green")
		ball2.color("yellow")
		if b.shapesize()[0] < a.shapesize()[0]:
			b.pu()
			b.goto(placex,placey)
		else:
			a.pu()
			a.goto(placex,placey)

a.pu()
a.goto(100,100)
a.pd()
c.pu()
c.goto(100,100)
c.pd()
b.pu()
b.goto(100,100)
b.pd()
random_ballSelect = random.randint(0,len(ball_list))
random_ball = ball_list[random_ballSelect]

collisions(random_ball,random_ball)
print(random_ball)
turtle.mainloop()