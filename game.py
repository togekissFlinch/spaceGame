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
t.register_shape("planet.gif")
t.register_shape("monster.gif")
t.register_shape("bomb.gif")
t.register_shape("explosion.gif")
t.register_shape("explosion2.gif")
t.register_shape("explosion3.gif")
t.register_shape("explosion4.gif")
t.register_shape("explosion5.gif")
t.register_shape("explosion6.gif")
t.register_shape("explosion7.gif")
t.register_shape("explosion8.gif")
t.register_shape("explosion9.gif")
t.register_shape("explosion10.gif")
#joueur
player = t.Turtle()
player.shape("player.gif")
player.x = 0
player.y = 0
player.penup()
player.setposition(0,50)
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
#fire
fire = t.Turtle()
fire.shape("fire1.gif")
fire.penup()
fire.setposition(0,-40)
#enemy
enemy = t.Turtle()
enemy.hideturtle()
enemy.shape("alien.gif")
enemy.penup()
enemy.setposition(0,350)
enemy.showturtle()
#bomb
bomb = t.Turtle()
bomb.penup()
bomb.hideturtle()
bomb.x = enemy.xcor()
bomb.y = enemy.ycor()
bomb.shape("bomb.gif")
bomb.setposition(enemy.xcor(),enemy.ycor())
bomb.showturtle()
for i in range(65):
    bomb.y -= 5
    bomb.sety(bomb.y)
bomb.shape("explosion.gif")
time.sleep(0.1)
bomb.shape("explosion2.gif")
time.sleep(0.1)
bomb.shape("explosion3.gif")
time.sleep(0.1)
bomb.shape("explosion4.gif")
time.sleep(0.1)
bomb.shape("explosion5.gif")
time.sleep(0.1)
bomb.shape("explosion6.gif")
time.sleep(0.1)
bomb.shape("explosion7.gif")
time.sleep(0.1)
bomb.shape("explosion8.gif")
time.sleep(0.1)
bomb.shape("explosion9.gif")
time.sleep(0.1)
bomb.shape("explosion10.gif")
time.sleep(0.1)
bomb.hideturtle()
#monster
monster = t.Turtle()
monster.hideturtle()
monster.penup()
monster.shape("monster.gif")
#planet
planet1 = t.Turtle()
planet1.hideturtle()
planet1.shape("planet.gif")
#boucle & animation
while True:
    enemy.shape("alien.gif")
    time.sleep(0.1)
    enemy.shape("alien2.gif")
    time.sleep(0.1)
    enemy.shape("alien3.gif")
    time.sleep(0.1)
    fire.shape("fire1.gif")
    time.sleep(0.1)
    fire.shape("fire2.gif")
    time.sleep(0.1)
    fire.shape("fire3.gif")
    time.sleep(0.1)
    fire.shape("fire4.gif")
    time.sleep(0.1)


