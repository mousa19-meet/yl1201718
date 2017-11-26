import turtle

turtle.begin_poly()
turtle.penup()
for i in range (6):
	turtle.fd(50)
	turtle.right(60)
turtle.end_poly()
p = turtle.get_poly()

turtle.register_shape("hexagon",p)
turtle.shape("hexagon")
turtle.mainloop()


turtle.register_shape("hexagon", turtle.begin_poly()
								