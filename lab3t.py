import turtle
turtle.register_shape("pic.gif")
turtle.shape("pic.gif")
a = 0
for i in range(100):
	#turtle.right(a)
	turtle.forward(100)
	turtle.right(60)
	turtle.forward(50)
	turtle.right(60)
	turtle.goto(0,0)
	a += 1
turtle.mainloop()