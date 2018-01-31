import turtle
#for i in range(5):
#	turtle.forward(50)
#	turtle.right(145)
#turtle.mainloop()

turtle.register_shape("shape", ((25,0),(25,-25),(12.5,-35),(0,-25),(0,0)))
turtle.shape("shape")
turtle.mainloop()