import turtle 
from turtle import *
import random
import time

#tracer(0)
ht()
getscreen().setup(1.0,1.0)
#tracer(0)
number_of_zombies = 4
zombie_list = []

class Zombie(Turtle):
	def __init__(self,x,y,dx,dy,hp,color,shape):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.hp = hp
		self.shape(shape)
		self.color(color)

	def move(self):
		slow_dy = random.randint(1,9)
		fast_dy = random.randint(15,25)
		slow_dx = random.randint(1,9)
		slow_dy = random.randint(15,25)

		current_x = self.xcor()
		new_x = current_x - self.dx 
		current_y = self.ycor()
		new_y = current_y - self.dy
		while current_x != 0 and current_y != 0:
			self.goto(0,0)


def make_zombie():
	for i in range(int(number_of_zombies/2)):
		radnom_X = random.randint(-550,550)
		random_y_list =[350,-350]
		random_y = random.choice(random_y_list)
		fat_zombe = Zombie(radnom_X , 350,5,5,100,"red","square")
		zombie_list.append(fat_zombe)
		radnom_X = random.randint(-550,550)
		random_y_list =[350,-350]
		random_y = random.choice(random_y_list)
		fast_zombe = Zombie(radnom_X , 350,50,50,10,"blue","circle")
		zombie_list.append(fast_zombe)

#def move_dem_zombies():
#	for variable in range(len(zombie_list)):
#		zombie_list[variable].move()


make_zombie()


#while True:
#	move_dem_zombies()
#	getscreen().update()
#	sleep(0.00777)

#getscreen().update()
mainloop()