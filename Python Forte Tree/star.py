import turtle
from turtle import *

star = turtle.Turtle()

for i in range(5):
	star.color('#ffff56', '#00ffff')
	begin_fill()
	while True:
		star.forward(150)
		star.right(144)

		if abs(pos()) < 1:
			break

end_fill()

turtle.done()