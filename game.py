import turtle as t
import time
#fenêtre
window = t.Screen()
window.bgpic("background.gif")
#importer les sprites
t.register_shape("player.gif")
t.register_shape("player2.gif")
t.register_shape("fire1.gif")
t.register_shape("fire2.gif")
t.register_shape("fire3.gif")
t.register_shape("fire4.gif")
t.register_shape("alien.gif")
t.register_shape("alien2.gif")
t.register_shape("alien3.gif")
t.register_shape("alien4.gif")
t.register_shape("alien5.gif")
#joueur
player = t.Turtle()
player.shape("player.gif")
player.penup()
player.setposition(0,90)
#fire
fire = t.Turtle()
fire.shape("fire1.gif")
fire.penup()
#enemy
enemy = t.Turtle()
enemy.shape("alien.gif")
enemy.hideturtle()
enemy.penup()
enemy.setposition(-400,-40)
enemy.showturtle()
enemy_is ="NOT KILLED"
#mouvements
def right():
    x = player.xcor() 
    ex = enemy.xcor()
    player.shape("player.gif")
    if x > 400:
        x = 400
    x += 10
    player.setx(x)
    fire.setx(x)
def left():
    x = player.xcor()
    ex = enemy.xcor()
    player.shape("player2.gif")
    if x < -400:
        x = -400
    x -= 10
    player.setx(x)
    fire.setx(x)
t.listen()
t.onkey(right, "Right")
t.onkey(left, "Left")
#boucle & animation
while True:
    x = player.xcor()
    ex = enemy.xcor()
    if x == ex + 40:
        if enemy_is == "NOT KILLED":
            enemy_is = "KILLED"
            enemy.shape("alien2.gif")
            time.sleep(0.1)
            enemy.shape("alien3.gif")
            time.sleep(0.1)
            enemy.shape("alien4.gif")
            time.sleep(0.1)
            enemy.shape("alien5.gif")
            time.sleep(0.1)
    fire.shape("fire1.gif")
    time.sleep(0.1)
    fire.shape("fire2.gif")
    time.sleep(0.1)
    fire.shape("fire3.gif")
    time.sleep(0.1)
    fire.shape("fire4.gif")
    time.sleep(0.1)
