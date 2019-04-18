import turtle

window = turtle.Screen()
window.colormode(255)

myTurtle = turtle.Turtle(shape='turtle')
myTurtle.left(90)

lv = 13
l = 120
s = 45

myTurtle.width(lv)

r = 0
g = 0
b = 0

myTurtle.pencolor('black')

myTurtle.penup()
myTurtle.backward(l)
myTurtle.pendown()
myTurtle.forward(l)


def draw_tree(l, level):
    global r, g, b

    # save the current pen width
    w = myTurtle.width()

    # narrow the pen width
    myTurtle.width(w * 3.0 / 4.0)
    # set color:
    r += 1
    g += 2
    b += 3
    myTurtle.pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    myTurtle.left(s)
    myTurtle.forward(l)

    if level < lv:
        draw_tree(l, level + 1)
    myTurtle.backward(l)
    myTurtle.right(2 * s)
    myTurtle.forward(l)

    if level < lv:
        draw_tree(l, level + 1)
    myTurtle.backward(l)
    myTurtle.left(s)

    # restore the previous pen width
    myTurtle.width(w)


myTurtle.pencolor()
myTurtle.speed(0)

draw_tree(l, 4)

turtle.done()
