import turtle
import random
import math

wn = turtle.Screen()
wn.title("jump")
wn.bgcolor("black")
wn.tracer(0)
wn.setup(1000, 1000)


pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()



player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(-450,-350)

Mini_enemys = []

for _ in range(20):
    Mini_enemy = turtle.Turtle()
    Mini_enemy.shape("square")
    Mini_enemy.color("white")
    Mini_enemy.shapesize(stretch_wid=0.4, stretch_len=2, outline=None)
    Mini_enemy.penup()
    x = random.randint(-450, 450)
    y = random.randint(100, 200)
    Mini_enemy.setposition(x, y)
    Mini_enemys.append(Mini_enemy)


def Collision(t1,t2):
  distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
  if distance < 15:
    return True
  else:
    return False



playerspeed = 10

def move_left():
  x = player.xcor()
  x = x - playerspeed
  if x < -450:
    x = -450
  player.setx(x)

def move_right():
  x = player.xcor()
  x = x + playerspeed
  if x > 450:
    x = 450
  player.setx(x)




wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")





while True:
    wn.update()






    #move and other enemy stuff

    for Mini_enemy in Mini_enemys:
        y = Mini_enemy.ycor()
        y -= 2
        Mini_enemy.sety(y)

        if Collision(player, Mini_enemy):
            # for linux use os.system("aplay explosion.wav&")
            player.hideturtle()
            Mini_enemy.hideturtle()

            pen.write("Game Over", font=("Roboto", 26, "normal"))
            break


        if Mini_enemy.ycor() < -350:
            x = random.randint(-450, 450)
            y = random.randint(100, 200)
            Mini_enemy.setposition(x, y)





    

wn.mainloop()
