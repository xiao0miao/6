import turtle
p = turtle.Pen()
p.pensize(10)
p.pencolor("gold")
# 5
p.goto(-100,0)
p.goto(-100,-100)
p.goto(0,-100)
p.goto(0,-200)
p.goto(-100,-200)
p.penup()
p.goto(100,0)
p.pendown()
p.pencolor("seagreen")
# 2
p.goto(200,0)
p.goto(200,-100)
p.goto(100,-100)
p.goto(100,-200)
p.goto(200,-200)
p.penup()
p.goto(300,0)
p.pendown()
p.pencolor("cornflowerblue")
# 0
p.goto(400,0)
p.goto(400,-200)
p.goto(300,-200)
p.goto(300,0)
p.ht()
turtle.done()