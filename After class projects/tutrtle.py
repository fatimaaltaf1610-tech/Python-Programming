import turtle

window = turtle.Screen

my_turtle = turtle.Turtle()

for i in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

window.exitonclick()
