from turtle import *

def drawSnake(angle,len,neckrad):
    for i in range(len):
        pencolor("red")
        circle(0,angle)
        pencolor("yellow")
        fd(150)
def main():
    setup(1300,800,0,0)
    pythonsize=20
    pensize(pythonsize)
    seth(-120)
    drawSnake(120,3,pythonsize/2)
main()

