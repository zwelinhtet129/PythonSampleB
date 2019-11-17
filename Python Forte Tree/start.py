import turtle
from turtle import *

window = turtle.Screen()
#window.bgcolor("#8f21a8")
window.bgpic("tae.gif")

color('red', 'green')
begin_fill()
while True:
	#backward(90)
	#left(90)
	
	forward(180)
	left(120)

	if abs(pos()) < 1:
		break

end_fill()
done()