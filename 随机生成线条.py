import turtle
import random
p = turtle.Pen()
p.speed(114514)
p.pensize(5)
p.pencolor('gold')
for i in range(114):
    for i in range(114514):
        for i in range(1145140):
            x = random.randint(0,360)
            d = random.randint(0,500)
            s = random.randint(-360,360)
            z = random.randint(0,500)
            p.circle(d,x)
            p.left(s)
            p.forward(z)
turtle.done()