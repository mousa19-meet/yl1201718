import turtle
from turtle import *
colormode(255)
import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
		self.color(red,green,blue)
	def random_color(self):
			print(red,green,blue)
		
ayo = Square(10)
ayo.random_color()
turtle.mainloop()