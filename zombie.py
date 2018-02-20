import turtle 
from turtle import *
import random
import time

number_of_zombies = 6
zombie_list = []

class Zombie(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.dx = dx
		self.dy = dy
		self.r = r
		self.x = x
		self.y = y
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
			self.dy = -self.dy

		elif bottom_side_ball < -height:
			self.dy = -self.dy

		elif left_side_ball < -width:
			self.dx = -self.dx

		elif right_side_ball > width:
			self.dx = -self.dx 


def make_zombie():
	for i in range(int(number_of_zombies/2)):
		radnom_X = random.randint(-50,50)
		random_y_list =[100,-100]
		random_y = random.choice(random_y_list)
		fat_zombe = Zombie(radnom_X , random_y,5,5,10,"red")
		zombie_list.append(fat_zombe)
		radnom_X = random.randint(-50,50)
		random_y = random.choice(random_y_list)
		fast_zombe = Zombie(radnom_X , random_y,15,15,10,"blue")
		zombie_list.append(fast_zombe)

def move_dem_zombies():
	for variable in range(len(zombie_list)):
		zombie_list[variable].move(screen_width,screen_height)


#make_zombie()
#while True:
#	getscreen().update()
#	move_dem_zombies()
#	time.sleep(0.0714)
#mainloop()