import turtle
t=turtle.Turtle()
colors=["red","blue","green","orange"]
distances=range(10,100)
diagonal = (2 * (distance **2))**0.5
t.speed(1000000000000000)
for n in range(10,100):
	for c in colors:
		t.color(c)
		t.forward(distance)
		t.left(90)
		t.forward(distance)
		t.left(90)
		t.forward(distance)
		t.left(90)
		t.forward(distance)
		t.left(45)
		t.forward(diagonal)
		t.left(180)
		t.forward(diagonal)
		t.left(10)
		
	