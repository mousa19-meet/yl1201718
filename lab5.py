import turtle
from turtle import *
colormode(255)
import random


class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self,color):
		self.colormode(color)
		
		
ayo = Square(10)
ayo.random_color(100)

turtle.mainloop()