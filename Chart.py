from LinearTurtle import *
from tkinter import *
from tkinter import ttk

def draw_chart(canvas):
    
    #Draws a chart with 0,0 in centre of page
    graphy = turtle.RawTurtle(canvas)
    graphy.ht()
    graphy.speed(0)
    graphy.penup()
    graphy.goto(250, 0)
    graphy.pendown()
    for i in range(0, 50):
        graphy.back(10)
        graphy.left(90)
        graphy.forward(3)
        graphy.back(3)
        graphy.right(90)
    graphy.penup()
    graphy.goto(0, -250)
    graphy.pendown()
    graphy.left(90)
    for i in range(0, 50):
        graphy.forward(10)
        graphy.left(90)
        graphy.forward(3)
        graphy.back(3)
        graphy.right(90)

class GUI():
    
    root = Tk()

    #This is the canvas the turtle will exist in
    canvas = Canvas(root, width = 500, height = 500)
    canvas.pack()

    draw_chart(canvas)

    
    turtles = [LinearTurtle(canvas)]

    turtles[0].penup()
    turtles[0].color("red")
    turtles[0].linear_plot([[10, 5],[12,7],[14, 9]])

    
    turtles[0].penup()
    turtles[0].color("black")
    turtles[0].brute_force(-10, 8, 2, 4)

    
    root.mainloop()



    
GUI()


