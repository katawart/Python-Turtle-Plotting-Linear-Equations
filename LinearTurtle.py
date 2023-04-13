import turtle
class LinearTurtle (turtle.RawTurtle):
    
    #Variables
    __factor = 10

    #Constructor
    def __init__(self,canvas):
        super(LinearTurtle,self).__init__(canvas)
        

    #Getter and setter methods
    def set_factor(self, change):
        self.__factor = change

    def get_factor(self):
        return self.__factor

    #Plots points for a graph, if the turtle's pen is up
    #it will also draw a line.
    #The position set will be x * the factor and y * the factor.
    #Preconditions: Takes two parameters an x and y coordiate as real numbers.
    #Postcondtions: None
    def plot_points(self, x, y):
        self.setpos(x * self.__factor ,y * self.__factor)
        self.dot()


    #Uses multiple points to draw a line graph.
    #To prevent a line from 0,0 to the first point the trutle's pen
    #is set to up if the point is index 0
    #otherwise it put the pen down to draw a line.
    #It calls plot_point for each index in the list.
    #Preconditions: Takes a list of points which are x, y coords.
    #Postcinditions: None
    def linear_plot(self, points):
        for i in points:
            if points.index(i) == 0:
                self.penup()
            else:
                self.pendown()
            self.plot_points(i[0], i[1])

            
    #A brute force  algorithm for line drawing.
    #Preconditions: x1 is a decimal for the first x coord in sequence.
    #x2 is a decimal for the last x coord in s a sequence.
    #m is the gradient/slope
    #c is the point that the point that the line intercepts the y axis when x is 0
    #Postconditions: None
    def brute_force(self, x1, x2, m, c):
        self.penup()
        self.goto(0 ,c * self.__factor)
        first_point = True
        for x in range(x1, x2): #For loop with the range set from the first to last
            if first_point:
                self.penup()
                first_point = False
            else:
                self.pendown()
            y = (m * x) + c     #Standard maths to find y.
            self.plot_points (x, round(y, 2))

    

        
                
