import turtle
from turtle import *
colormode(255)
import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)


class rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		self.width = width
		self.height = height
		turtle.register_shape("rectangle",((height,0),(height,width),(0,width),(0,0)))
		turtle.shape("rectangle")
		self.setheading(90) 
class Square(Turtle):
	def __init__(self,size):
		rectangle.__init__(self,size,size)
	def random_color(self):
		#self.shapesize(size)
		self.shape("square")
		self.color(red,green,blue)
		print(red,green,blue)
class hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.begin_poly()
		for i in range (6):
			self.pu()
			self.fd(size)
			self.right(60)
		self.end_poly()
		register_shape("hexagon",self.get_poly())
		self.setheading(90)
		self.shape("hexagon")



myhexa = hexagon(50)		
#ayo = Square(50)
#ayo.random_color()
#rectangle123 = rectangle(10,20)

turtle.mainloop()