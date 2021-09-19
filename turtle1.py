import turtle

col = ('red','yellow','green','cyan','pink','white')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
for i in range(150):
    t.color(col[i%6])
    t.forward(i*1.5)
    t.left(56)
    t.width(3)