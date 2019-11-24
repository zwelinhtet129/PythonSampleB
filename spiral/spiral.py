import turtle
from turtle import *



colors = ['red', 'purple', 'blue', 'green', 'brown', 'pink']

hellopen = turtle.Pen()
turtle.bgcolor("black")

begin_fill()
for x in range(360):
	hellopen.pencolor(colors[x % 6])
	hellopen.width(x/100 + 1)
	hellopen.forward(x)
	hellopen.left(59)

end_fill()
done()