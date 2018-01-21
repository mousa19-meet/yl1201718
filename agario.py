from turtle import *
import turtle
import time
import random
from ball import *
colormode(255)


number_of_BALLS = 5 
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
balls =[]

for i in range(number_of_BALLS):

	screen_random1_x = int(-screen_width+maximum_ball_radius)
	screen_random2_x = int(screen_width-maximum_ball_radius)
	random_x = random.randint(screen_random1_x,screen_random2_x)
	
	screen_random1_y = int(-screen_height+maximum_ball_radius)
	screen_random2_y = int(screen_height-maximum_ball_radius)
	random_y = random.randint(screen_random1_y,screen_random2_y)
	
	random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	while random_dx == 0:
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

	random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	while random_dy == 0:
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	radius = random.randint(minimum_ball_radius,maximum_ball_radius)

	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	


	ball = Ball(random_x,random_y,random_dx,random_dy,radius,color)
	balls.append(ball)


def move_all_balls():
	for variable in range(number_of_BALLS):
		balls[variable].move(screen_width,screen_height)

for i in range(1000):
	move_all_balls()

def check_collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False

						#sqrt ( x2-x1 square ) + ( y2-y1 square)
	balls_distance = ((ball_a.xcor()-ball_b.xcor())^2+(ball_a.ycor()-ball_b.ycor())^2)^0.5

	if balls_distance+10 <= ball_a.r+ball_b.r:
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in range (balls):
		for ball_b in range (balls):
			if check_collide == True:
				radius1 = ball_a.r
				radius2 = ball_b.r
				if radius1 > radius2:
				 	ball.b = ball(random_x,random_y,random_dx,random_dy,radius,color)
				 	radius1 += 1 
				elif radius1 < radius2:
				 	ball.a = ball(random_x,random_y,random_dx,random_dy,radius,color)
				 	radius2 += 1
def check_myball_collision():			
	for i in range(balls):
		if 
mainloop()