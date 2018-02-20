from turtle import *
import random
import math


class Bullet(Turtle):
  def __init__(self,screen,x,y,heading):
    Turtle.__init__(self)
    self.speed(0)
    self.penup()
    self.goto(x,y)
    self.seth(heading)
    self.screen = screen 
    self.color('red')
    self.max_distance = 500
    self.distance = 0
    self.delta = 20
    self.shape("circle")
  
  def move(self):
    self.distance = self.distance + self.delta
    self.forward(self.delta)
    if self.done():
      self.reset()
      
  def getRadius(self):
    return 4
    
  def blowUp(self):
    self.goto(-300,0)
  
  def done(self):
    return self.distance >= self.max_distance\

