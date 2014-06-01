import turtle
t=turtle.Turtle()
colors=["red","blue","green","orange"]
distances=range(100,200)
#diagonal = (2 * (distance **2))**0.5
t.speed(1000000000000000)
for distance in distances:
	diagonal = (2 * (distance **2))**0.5
	for c in colors:
		t.color(c)
		t.forward(distance)
		t.left(90)
		t.forward(distance)
		t.left(90)
		t.forward(distance)
		t.left(90)
		t.forward(distance)
		t.left(135)
		t.forward(diagonal)
		t.left(180)
		t.forward(diagonal)
	t.left(150)
		
	