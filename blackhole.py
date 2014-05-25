import turtle
t=turtle.Turtle()
colors=["red","blue","green","orange"]
distances=range(10,100)
t.speed(1)
for distance in distances:
	t.left(10)
	for c in colors:
		t.color(c)
		t.forward(distance)
		t.left(90)
	