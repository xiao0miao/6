import turtle
p = turtle.Pen()
p.pensize(3)
p.speed(114514)
n = 6
g = 6
p.begin_fill()
p.fillcolor("red")
for i in range(g):
    for j in range(n):
        p.forward(100)
        p.left(360/n)
    p.left(360/n)
p.end_fill()
turtle.done()