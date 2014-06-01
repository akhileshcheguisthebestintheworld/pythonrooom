import turtle
t=turtle.Turtle()
colors=["red","blue","green","orange"]
distances=range(50,100)
distance = int(input("What surprise shape number do you want?"))
angle = 180 - (360/distance)
t.speed(1000000000000000)
for distance in distances:
	t.left(10)
	for c in colors:
		t.color(c)
		t.forward(distance)
		t.left(angle)