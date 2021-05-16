import turtle as t
import time
#fenêtre
window = t.Screen()
window.bgpic("background.gif")
window.title("A Game Made By Boris")
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
t.register_shape("planet.gif")
#joueur
player = t.Turtle()
player.shape("player.gif")
player.x = 0
player.y = 0
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
#planet
planet1 = t.Turtle()
planet1.hideturtle()
planet1.shape("planet.gif")
#mouvements
def right():
    player.shape("player.gif")
    if player.x > 440:
        player.x = 400
    player.x += 10
    fire.setx(player.x)
    player.setx(player.x)
def left():
    player.shape("player2.gif")
    if player.x < -440:
        player.x = -400
    player.x -= 10
    player.setx(player.x)
    fire.setx(player.x)
t.listen()
t.onkey(right, "Right")
t.onkey(left, "Left")
#boucle & animation
while True:
    ex = enemy.xcor()
    if player.x == ex:
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
            enemy.hideturtle()
    fire.shape("fire1.gif")
    time.sleep(0.1)
    fire.shape("fire2.gif")
    time.sleep(0.1)
    fire.shape("fire3.gif")
    time.sleep(0.1)
    fire.shape("fire4.gif")
    time.sleep(0.1)
