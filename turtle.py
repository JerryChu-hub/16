
from turtle import Turtle, Screen
#turtle = module, Turtle =  class = blueprint, screen = object

jerry = Turtle()
print(jerry)
jerry.shape("turtle")
jerry.color("DeepPink2")
jerry.forward(100)

my_screen = Screen()
print(my_screen.canvheight) #attributes in the object

my_screen.exitonclick() #function in the object = method, what this object need to do
