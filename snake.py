import turtle

def drawSnake(red,angle,len,neckrad):
    for i in range(len):
        turtle.pencolor("green")
        turtle.circle(red,angle)
        turtle.pencolor("red")
        turtle.circle(-red,angle)
        turtle.pencolor("blue")
    turtle.circle(red,angle/2)
    turtle.pencolor("green")
    turtle.fd(red)
    turtle.pencolor("blue")
    turtle.circle(neckrad+1,180)
    turtle.pencolor("yellow")
    turtle.fd(red*2/3)
def main():
    turtle.setup(1300,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)
main()

'''from turtle import *

def drawSnake(red,angle,len,neckrad):
    for i in range(len):
        pencolor("green")
        circle(red,angle)
        pencolor("red")
        circle(-red,angle)
        pencolor("blue")
    circle(red,angle/2)
    pencolor("green")
    fd(red)
    pencolor("blue")
    circle(neckrad+1,180)
    pencolor("yellow")
    fd(red*2/3)
def main():
    setup(1300,800,0,0)
    pythonsize=30
    pensize(pythonsize)
    seth(-40)
    drawSnake(40,80,5,pythonsize/2)
main()
'''
