import turtle
p = turtle.Pen()
#p.ht
p.speed(114514)
for i in range(8):
    p.begin_fill()
    p.fillcolor("blue")
    p.left(180)
    p.right(45)
    p.forward(70.5)
    p.left(90)
    p.forward(70.5)
    p.right(45)
    p.end_fill()
    p.right(180)
    p.forward(100)
    p.left(90)
    p.right(180)
    p.begin_fill()
    p.fillcolor("skyblue")
    p.forward(100)
    p.right(135)
    p.forward(141)
    p.end_fill()
    p.left(180)
turtle.done()