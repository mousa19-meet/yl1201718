from ball import *

screen_width = getcanvas().winfo_width()/2
screen_height = getcanvas().winfo_height()/2

balls =[]






def create_ball(event):
	global balls 

	number_balls = 1

	for i in range(number_balls):
		x = 0 
		y = -screen_height + 50
		dx = event.x - screen_width -x
		dy = screen_height - event.y - y
		new_ball = Ball(event.x,event.y,dx/100,dy/100,50,"red")
		print("heyyyyyyyyy")
		balls.append(new_ball)

getcanvas().bind("<Button-1>", create_ball)

mainloop()
