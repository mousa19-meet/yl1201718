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

screen_random1_x = int(-screen_width+maximum_ball_radius)
screen_random2_x = int(screen_width-maximum_ball_radius)

random_x = random.randint(screen_random1_x,screen_random2_x)
print(random_x)

screen_random1_y = int(-screen_height+maximum_ball_radius)
screen_random2_y = int(screen_height-maximum_ball_radius)

random_y = random.randint(screen_random1_y,screen_random2_y)
print(random_y)

random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
print (random_dx)
if random_dx == 0:
	random_dx += 1

random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
print(random_dy)
if random_dy == 0:
	random_dy += 1

radius = random.randint(minimum_ball_radius,maximum_ball_radius)
print(radius)
 
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
print(color)

ball1 = Ball(random_x,random_y,random_dx,random_dy,radius,color)


mainloop()