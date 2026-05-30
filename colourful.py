import turtle
screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(17)
colors = ["red", "yellow", "green", "pink", "orange", "white"]
for i in range(200):
    pen.color(colors[i % 6])
    pen.forward(i)
    pen.right(126)
