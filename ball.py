from turtle import *
import turtle
import random
import math
colormode(255)

running = True
sleep = 0.0077
screen_width =int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)
print(screen_width)
print(screen_height)

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shapesize(r/10)
		self.goto(x,y)
		self.color(color)
		self.shape("circle")



	def move(self,width,height):
		current_x = self.xcor()
		new_x = current_x + self.dx 
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r
		self.goto(new_x,new_y)


		if top_side_ball > height:
			self.dy = - self.dy

		elif bottom_side_ball < -height:
			self.dy = -self.dy

		elif left_side_ball < -width:
			self.dx = -self.dx

		elif right_side_ball > width:
			self.dx = -self.dx 
MY_BALL = Ball(0,0,5,5,10,"red")

#ball = Ball(5,5,10,10,5,"red")
#print(ball.r)
#		def top(self):
#			return self.ycor() + (0.5 *self.height)
#		def bottom(self):
#			return self.ycor() - (0.5 * self.height)
#		def right(self):
#			return self.xcor() + (0.5 *self.width)
#		def left(self):
#			return self.xcor() - (0.5 *self.width)

#if a.top > b.bottom &
#a.right > b. right &
#a. bottom < b .bottom &
#a.left < b.left :
#return true 
#my_ball = Ball(100,0,5,5,10 ,"red")
# my_ball.goto(10,10)

#sqrt ( x2-x1 square ) + ( y2-y1 square)


