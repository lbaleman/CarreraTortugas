import turtle
import random

class Circuito():
    corredores=[]
    __colorTurtle= ('red','blue','yellow','green')
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 +20
        self.__finishLine = width/2 -100
        
        self.__createrunners()
    
    def __createrunners(self):
        for i in range(4):
            newTurtle = turtle.Turtle()
            newTurtle.shape('turtle')
            newTurtle.color(self.__colorTurtle[i])
            newTurtle.penup()
            newTurtle.setpos(self.__startLine, i*20-30)
            self.corredores.append(newTurtle)
            
    def getganador(self,valor):
        return self.corredores[valor].color()
            
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for i in self.corredores:
                avance=random.randint(1,6)
                i.forward(avance)
                
                
                if i.position()[0] >= self.__finishLine:
                    hayGanador= True
                    print(i.color()[0])
                

            
    
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()
        
    