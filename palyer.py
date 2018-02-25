import turtle
from turtle import *
#from bullet import *
from zombie import *

tracer(0)
ht()
screen = Screen()

class player(Turtle):
	def __init__(self,x,y):
		Turtle.__init__(self)
		self.shape("square")
		self.color("green")
		self.goto(x,y)
		self.bullets = []

	def shoot(self):
		dem_bullets = []
		for bullet in self.bullets:
			bullet.move()
			hit = False
			if (not bullet.done() and not hit):
				dem_bullets.append(bullet)
		self.bullets = dem_bullets

	def fire_bullet(self):
		self.bullets.append(Bullet(self.screen,self.xcor(),self.ycor(),self.heading()))

	def turnTowards(self,x,y):
		if x < self.xcor():
			self.left(7)
		if x > self.xcor():
			self.right(7)
player1 = player(0,0)

def turnLeft():
	player1.left(7)

def turnRight():
	player1.right(7)

#def collision():
	###

#def zombie_collison:
	###

#def pow():
#	player1.shoot()
#	player1.fire_bullet()
#onkey(pow,"a")

screen.onkey(turnLeft,"Left")
screen.onkey(turnRight,"Right")
listen()


make_zombie()

while True:
	move_dem_zombies()
	getscreen().update()
	time.sleep(0.062)
mainloop()