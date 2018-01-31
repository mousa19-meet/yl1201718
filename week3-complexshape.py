import turtle
turtle.register_shape("pic.gif")
turtle.shape("pic.gif")
turtle.hideturtle()
b = 0
shape = 1
angle = 400 / shape
turtle.tracer(100)
for i in range(int(angle)):
	turtle.right(b)
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(85)
	turtle.forward(55)
	turtle.home()
	b += shape
turtle.mainloop()