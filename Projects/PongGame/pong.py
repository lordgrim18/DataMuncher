import turtle
import winsound

#window
window = turtle.Screen()
window.title("pong game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)       #prevents auto updation, forcing users to manually update it

#paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()    #no drawing when moving
paddle_a.goto(-350,0)

#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() 
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#score board 
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0    Player B: 0    ", align="center", font=("Courier", 24,"normal" ))


#paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard bindings
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")


#ball movement
def ball_mov():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#setting border
def set_border():
    global score_a
    global score_b
    #top 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #left 
    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24,"normal" ))
        ball.goto(0,0)  #if the ball reaches the border then it begins from the centre after adding score
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #right
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center",font=("Courier", 24,"normal" ))
        ball.goto(0,0)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    

#paddle and ball collisions
def collision():
    #left
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #right
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
       ball.setx(340)
       ball.dx *= -1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)




#main game loop
while True:
    window.update()
    
    ball_mov()
    set_border()
    collision()