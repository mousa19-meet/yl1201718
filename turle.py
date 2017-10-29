import turtle 
turtle.speed(100)
turtle.hideturtle()
a = 50
for i in range(10):
	turtle.left(a)
	for i in range(5):
		turtle.forward(50)
		turtle.left(50)
turtle.mainloop()
