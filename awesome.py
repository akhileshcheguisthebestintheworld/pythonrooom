import turtle

t = turtle.Turtle()
angle = 144
numbers = range(1,100)
for number in numbers:
	t.backward(100)
	t.left(angle)
	angle = angle + 1
