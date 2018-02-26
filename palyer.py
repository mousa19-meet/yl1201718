import turtle
from turtle import *
#from bullet import *
from zombie import *

tracer(0)
ht()
#screen = Screen()

class player(Turtle):
	def __init__(self,x,y):
		Turtle.__init__(self)
		self.shape("square")
		self.color("green")
		self.goto(x,y)
		self.bullets = []

	#def shoot(self):



	#	dem_bullets = []
	#	for bullet in self.bullets:
	#		bullet.move()
	#		hit = False
	#		if (not bullet.done() and not hit):
	#			dem_bullets.append(bullet)
	#	self.bullets = dem_bullets

	#def fire_bullet(self):
	#	self.bullets.append(Bullet(self.screen,self.xcor(),self.ycor(),self.heading()))

	##	if x < self.xcor():
	#		self.left(7)
	#	if x > self.xcor():
	#		self.right(7)
player1 = player(0,0)

def check_collide(zombie,bullet):
	if zombie == bullet:
		return False
						#squareroot ( x2-x1 squared ) + ( y2-y1 squared)
	distance = ((zombie.xcor()-bullet.xcor())**2 +(zombie.ycor()-bullet.ycor())**2)**0.5

	if distance+5 <= (zombie.r+bullet.r):
		return True 
	else:
		return False

def check_all_collions:
	for zombie in zombie_list:
		for bullet in zombie_list:
			if check_collide(zombie,bullet) == True:
				zombie_list.pop(zombie)


make_zombie()

while True:
	move_dem_zombies()
	getscreen().update()
	time.sleep(0.062)
mainloop()