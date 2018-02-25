import turtle 
from turtle import *
import random
import time

number_of_zombies = 10
zombie_list = []
screen_width =int(turtle.getcanvas().winfo_width()/2)
screen_height = int(turtle.getcanvas().winfo_height()/2)

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

	def move(self):
		global new_x , new_y
		current_x = self.xcor()
		current_y = self.ycor()

		if current_x > 0:
			new_x = current_x - self.dx
		if current_x < 0:
			new_x = current_x + self.dx
		if current_y > 0:
			new_y = current_y - self.dy
		if current_y < 0:
			new_y = current_y + self.dx

		self.goto(new_x,new_y)

def make_zombie():
	for i in range(int(number_of_zombies/2)):
		radnom_X = random.randint(-350,350)
		while radnom_X == 0:
			radnom_X = random.randint(-350,350)
		random_y_list =[250,-250]
		random_y = random.choice(random_y_list)
		fat_zombe = Zombie(radnom_X , random_y,2,2,10,"red")
		zombie_list.append(fat_zombe)
		radnom_X = random.randint(-350,350)
		while radnom_X == 0:
			radnom_X = random.randint(-350,350)
		random_y = random.choice(random_y_list)
		fast_zombe = Zombie(radnom_X,random_y,5,5,10,"blue")
		zombie_list.append(fast_zombe)

def move_dem_zombies():
	for variable in range(len(zombie_list)):
		zombie_list[variable].move()

#make_zombie()
#while True:
#	getscreen().update()
#	move_dem_zombies()
#	time.sleep(0.0714)
#mainloop()