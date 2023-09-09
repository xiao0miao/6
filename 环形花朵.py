import turtle
p = turtle.Pen()
p.pensize(3)
p.speed(114514)
p.ht()
p.penup()
for i in range(6):
    for n in range(1):
        for l in range(6):
            p.left(60)
            p.forward(50)
            p.dot(100,"red")
            p.left(180)
            p.forward(50)
            p.left(180)
        p.dot(90,"yellow")
    p.left(60)
    p.forward(250)
turtle.done()