import turtle
from playsound import playsound
import winsound, sys

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_1 = 0
score_2 = 0


# Raquette 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Raquette 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#déplacement de la balle
ball.dx = .4
ball.dy = .4

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Joueur 1 : {}        Joueur 2 : {}".format(score_1, score_2), align="center", font=("Arial", 24, "normal"))



####################################     Fonctions     ##################################################

def paddle_1_up():
    if paddle_1.ycor() >= 220:
        paddle_1.sety(220)
    y = paddle_1.ycor()
    y +=20
    paddle_1.sety(y)
   


def paddle_1_down():
    if paddle_1.ycor() <= -220:
        paddle_1.sety(-220)
    y = paddle_1.ycor()
    y -=20
    paddle_1.sety(y)

def paddle_2_up():
    if paddle_2.ycor() >= 220:
        paddle_2.sety(220)
    y = paddle_2.ycor()
    y +=20
    paddle_2.sety(y)

def paddle_2_down():
    if paddle_2.ycor() <= -220:
        paddle_2.sety(-220)
    y = paddle_2.ycor()
    y -=20
    paddle_2.sety(y)


# keyboard binding

window.listen()
window.onkeypress(paddle_1_up, "a")
window.onkeypress(paddle_1_down, "q")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

# Main game loop
while True:
    window.update()
    
    # mouvement de la balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Brordure de l'ecran
    if ball.ycor() > 290:
        ball.sety(290)
         
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290) 
                
        ball.dy *= -1       
       

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Joueur 1 : {}        Joueur 2 : {}".format(score_1, score_2), align="center", font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1        
        pen.clear()
        pen.write("Joueur 1 : {}        Joueur 2 : {}".format(score_1, score_2), align="center", font=("Arial", 24, "normal"))

    # collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
         
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
         
        ball.dx *= -1