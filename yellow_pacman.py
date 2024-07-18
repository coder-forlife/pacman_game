import turtle
import random
import time
turtle.register_shape("enemy.gif")
turtle.register_shape("Right_Pacman.gif")
turtle.register_shape("Left_Pacman.gif")
turtle.register_shape("UP_Pacman.gif")
turtle.register_shape("Down_Pacman.gif")
turtle.register_shape("orange.gif")
turtle.register_shape("Crack_Land.gif")
background=turtle.Turtle()
background.shape("Crack_Land.gif")
enemy=turtle.Turtle()
enemy.shape("enemy.gif")
enemy.penup()
enemy.setpos(0,250)
pacman=turtle.Turtle()
pacman.shape("Right_Pacman.gif")
pacman.penup()
food=turtle.Turtle()
food.shape("orange.gif")
food.penup()
food.setpos(0,200)
score=0
screen=turtle.Screen()
border=turtle.Turtle()
border.penup()
border.setpos(-500,-500)
border.pendown()
border.forward(500)
border.left(90)
border.forward(500)
border.left(90)
border.forward(500)
border.left(90)
border.forward(500)
def up():
  pacman.setheading(90)
  pacman.forward(10)
  pacman.shape("UP_Pacman.gif")
  if((pacman.pos()[0]>food.pos()[0]-15)and(pacman.pos()[0]<food.pos()[0]+15)and(pacman.pos()[1]>food.pos()[1]-15)and(pacman.pos()[1]<food.pos()[1]+15)):
    global score
    score=score+1
    turtle.penup()
    turtle.setpos(0,350)
    turtle.clear()
    turtle.write("score="+str(score),font=("Ariel", 20, "bold"))
    food.hideturtle()
    x=random.randint(-230,230)
    y=random.randint(-230,230)
    food.setpos(x,y)
    food.showturtle()
    turtle.hideturtle()
  if((pacman.pos()[0]>enemy.pos()[0]-15)and(pacman.pos()[0]<enemy.pos()[0]+15)and(pacman.pos()[1]>enemy.pos()[1]-15)and(pacman.pos()[1]<enemy.pos()[1]+15)):
    screen.clear()
    time.sleep(1)
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.write("game over", font=("Calibri",20,"bold"))
def down():
  pacman.setheading(270)
  pacman.forward(10)
  pacman.shape("Down_Pacman.gif")
  if((pacman.pos()[0]>food.pos()[0]-15)and(pacman.pos()[0]<food.pos()[0]+15)and(pacman.pos()[1]>food.pos()[1]-15)and(pacman.pos()[1]<food.pos()[1]+15)):
    global score
    score=score+1
    turtle.penup()
    turtle.setpos(0,350)
    turtle.clear()
    turtle.write("score="+str(score),font=("Ariel",20,"bold"))
    food.hideturtle()
    x=random.randint(-230,230)
    y=random.randint(-230,230)
    food.setpos(x,y)
    food.showturtle()
  if((pacman.pos()[0]>enemy.pos()[0]-15)and(pacman.pos()[0]<enemy.pos()[0]+15)and(pacman.pos()[1]>enemy.pos()[1]-15)and(pacman.pos()[1]<enemy.pos()[1]+15)):
    screen.clear()
    time.sleep(1)
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.write("game over", font=("Calibri",20,"bold"))
def left():
  pacman.setheading(180)
  pacman.forward(10)
  pacman.shape("Left_Pacman.gif")
  if((pacman.pos()[0]>food.pos()[0]-15)and(pacman.pos()[0]<food.pos()[0]+15)and(pacman.pos()[1]>food.pos()[1]-15)and(pacman.pos()[1]<food.pos()[1]+15)):
    global score
    score=score+1
    turtle.penup()
    turtle.setpos(0,350)
    turtle.clear()
    turtle.write("score="+str(score),font=("Ariel",20,"bold"))
    food.hideturtle()
    x=random.randint(-230,230)
    y=random.randint(-230,230)
    food.setpos(x,y)
    food.showturtle()
  if((pacman.pos()[0]>enemy.pos()[0]-15)and(pacman.pos()[0]<enemy.pos()[0]+15)and(pacman.pos()[1]>enemy.pos()[1]-15)and(pacman.pos()[1]<enemy.pos()[1]+15)):
    screen.clear()
    time.sleep(1)
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.write("game over", font=("Calibri",20,"bold"))
def right():
  pacman.setheading(0)
  pacman.forward(10)
  pacman.shape("Right_Pacman.gif")
  if((pacman.pos()[0]>food.pos()[0]-15)and(pacman.pos()[0]<food.pos()[0]+15)and(pacman.pos()[1]>food.pos()[1]-15)and(pacman.pos()[1]<food.pos()[1]+15)):
    global score
    score=score+1
    turtle.penup()
    turtle.setpos(0,350)
    turtle.clear()
    turtle.write("score="+str(score), font=("Ariel",20,"bold"))
    food.hideturtle()
    x=random.randint(-230,230)
    y=random.randint(-230,230)
    food.setpos(x,y)
    food.showturtle()
  if((pacman.pos()[0]>enemy.pos()[0]-15)and(pacman.pos()[0]<enemy.pos()[0]+15)and(pacman.pos()[1]>enemy.pos()[1]-15)and(pacman.pos()[1]<enemy.pos()[1]+15)):
    screen.clear()
    time.sleep(1)
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.write("game over", font=("Calibri",20,"bold"))
screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
x=-250

while (True):
    enemy.setpos(x,250)
    x=x+1
    if (x==250):
        x=-250
    
    
    

