import turtle

def bunga(n, panjang, sudut):
    for i in range(n):
        turtle.forward(panjang)
        turtle.right(sudut)
        turtle.forward(panjang)
        turtle.right(180 - sudut)

turtle.speed(0)
turtle.color("red")

for j in range(6):
    bunga(4, 100, 90)
    turtle.right(60)

turtle.hideturtle()
turtle.done()
