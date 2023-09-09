import turtle
p = turtle.Pen()
c = 100
g = int(input("请输入要画的棒棒糖个数(横向排列)："))
p.ht()
p.pencolor("wheat")
for i in range(g):
    p.pensize(10)
    p.right(90)
    p.forward(150)
    p.left(180)
    p.forward(150)
    for l in range(5):
        p.dot(c,"yellow")
        c = c-10
        p.dot(c,"pink")
        c = c-10
    p.right(90)
    p.penup()
    p.forward(100)
    p.pendown()
    c=100
turtle.done()
