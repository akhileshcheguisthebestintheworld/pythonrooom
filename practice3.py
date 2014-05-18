# author: akhileshcheguisthebestintheworld
import turtle

def makeShape(sides):
	t = turtle.Turtle()
	for i in range(sides):
		t.forward(50)
		t.left(360.0/sides)
shape = input("What should I draw?")


if shape == "square":
	square()
if shape == "triangle":
	triangle()
if shape == "pentagon":
	pentagon()
if shape == "hexagon":
	hexagon()
if shape == "decagon":
	decagon()
if shape == "dodecagon":
	dodecagon()	