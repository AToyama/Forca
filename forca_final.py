#FORCA

import turtle
import random

########################################## Lista
lista=[]
f = open("entrada.txt",encoding="utf-8")
lista1=f.readlines()
for j in lista1:
    lista.append(j.strip())

while lista != []:

    window = turtle.Screen()
    window. bgcolor("white")
    window.title("Forca")
    
    y = 0
    erros = 0
    acertos=[]
    tentativas=[]
    erradas=[]
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç']       
    word = random.choice(lista).lower().strip()
   
########################################## Funções   
        
    def head():
        turtle.penup()    
        turtle.setpos(-100,150)
        turtle.pendown()
        turtle.left(270)    
        turtle.circle(30)
            
    def body():
        turtle.penup()    
        turtle.setpos(-100, 90)
        turtle.pendown()
        turtle.right(90)    
        turtle.back(80)
    
    def left_leg():
        turtle.penup()
        turtle.setpos(-100,10)
        turtle.down()    
        turtle.right(315)
        turtle.back(40)
        
    def right_leg():
        turtle.penup()
        turtle.setpos(-100,10)
        turtle.pendown()
        turtle.left(90)
        turtle.back(40)
        
    def left_arm():
        turtle.penup()
        turtle.setpos(-100, 70)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(40)    
        
    def right_arm():
        turtle.penup()
        turtle.setpos(-100,70)
        turtle.pendown()
        turtle.left(180)
        turtle.forward(40)                
    
    ######################################### Turtles
    
    forca = turtle.Turtle()
    forca.hideturtle() 
    forca.speed(10)
    forca.pensize(3)   
        
    ########################################## Forca
    
    turtle = turtle.Turtle()
    turtle.hideturtle()
    turtle.speed(5)
    turtle.color('brown')
    turtle.pensize(10)
    turtle.penup()
    turtle.setpos(-250,-100)
    turtle.pendown()
    
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50) 
    
    turtle.speed(10)
    turtle.penup()
    turtle.pendown()
    turtle.color('black')
    turtle.pensize(5)
    turtle.hideturtle()
    
################################################ progama  
        
    while erros < 6:
       
        x = ''    
        for l in word:
            x += l if l in acertos else "_ "
        forca.hideturtle()    
        forca.penup()    
        forca.setpos(-230,-200)       
        forca.write(x, move=False, align="left", font=("Arial", 40, "normal"))
        
        forca.penup()
        forca.setpos(-40, 140)
        forca.write('Erros: ', move = False, align='Left', font=('Arial', 20, 'normal'))        
        
        
        if x == word:
            forca.penup()
            forca.setpos(-250,0)
            forca.color('red')
            forca.write('YOU WON!', move=False, align='left',font=('arial', 60, "normal"))        
            break

        tentativa = window.textinput('Letra','').lower().strip()
    
        if tentativa in abc:          
            if tentativa in word:
                acertos += tentativa
                forca.clear()
            else:
                erradas += tentativa
                erros += 1
                turtle.penup()
                turtle.setpos(40+y,140)
                turtle.write(tentativa,move=False, align='left', font=('Arial', 30, 'normal'))            
                y += 30
            
                if erros == 1:
                    head()
                if erros == 2:
                    body()
                if erros == 3:
                    left_arm()
                if erros == 4:
                    right_arm()
                if erros == 5:
                    left_leg()
                if erros == 6:
                    right_leg()
                    forca.penup()
                    forca.setpos(-250,0)
                    forca.color('red')
                    forca.write('GAME OVER', move=False, align='left',font=('arial', 60, "normal"))
    
window.exitonclick()