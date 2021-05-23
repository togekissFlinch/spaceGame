import turtle as t
import time
window = t.Screen()
window.bgpic("sprite/background.gif")
window.title("A Game Made By Boris")
t.register_shape("sprite/player.gif")
t.register_shape("sprite/player2.gif")
t.register_shape("sprite/player3.gif")
t.register_shape("sprite/fire1.gif")
t.register_shape("sprite/fire2.gif")
t.register_shape("sprite/fire3.gif")
t.register_shape("sprite/fire4.gif")
t.register_shape("sprite/alien.gif")
t.register_shape("sprite/alien2.gif")
t.register_shape("sprite/alien3.gif")
t.register_shape("sprite/bomb.gif")
t.register_shape("sprite/explosion.gif")
t.register_shape("sprite/explosion2.gif")
t.register_shape("sprite/explosion3.gif")
t.register_shape("sprite/explosion4.gif")
t.register_shape("sprite/explosion5.gif")
t.register_shape("sprite/explosion6.gif")
t.register_shape("sprite/explosion7.gif")
t.register_shape("sprite/explosion8.gif")
t.register_shape("sprite/explosion9.gif")
t.register_shape("sprite/explosion10.gif")
t.register_shape("sprite/rocket.gif")
def creer(objet,objet_x,objet_y,image):
    objet.x = objet_x
    objet.y = objet_y
    objet.penup()
    objet.hideturtle()
    objet.shape(image)
    objet.setposition(objet.x,objet.y)
    objet.showturtle()
#player
player = t.Turtle()
creer(player,0,50,"sprite/player.gif")
print(player.x)
#fire
fire = t.Turtle()
creer(fire,0,-40,"sprite/fire1.gif")
#rocket
rocket = t.Turtle()
creer(rocket,600,0,"sprite/rocket.gif")
#alien
enemy = t.Turtle()
creer(enemy,0,350,"sprite/alien.gif")
#bomb
bomb = t.Turtle()
creer(bomb,enemy.xcor(),enemy.ycor(),"sprite/bomb.gif")
bomb.hideturtle()
def jeter_bombe():
    bomb.showturtle()
    bomb.setposition(player.x,player.y)
    bomb.shape("sprite/explosion.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion2.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion3.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion4.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion5.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion6.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion7.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion8.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion9.gif")
    time.sleep(0.1)
    bomb.shape("sprite/explosion10.gif")
    time.sleep(0.1)
    bomb.hideturtle()
    bomb.setposition(enemy.xcor(),enemy.ycor())
    bomb.shape("sprite/bomb.gif")
jeter_bombe()
ex = enemy.xcor()
ey = enemy.ycor()
player.shape("sprite/player.gif")
fire.hideturtle()
time.sleep(0.1)
player.shape("sprite/player3.gif")
for i in range(10):
    player.y -= 10
    player.sety(player.y)
enemy.setx(player.x)
for i in range(10):
    enemy.shape("sprite/alien.gif")
    time.sleep(0.1)
    enemy.shape("sprite/alien2.gif")
    time.sleep(0.1)
    enemy.shape("sprite/alien3.gif")
    ey -= 30
    enemy.sety(ey)
for i in range(10):
    enemy.shape("sprite/alien.gif")
    time.sleep(0.1)
    enemy.shape("sprite/alien2.gif")
    time.sleep(0.1)
    enemy.shape("sprite/alien3.gif")
    ey += 10
    player.y += 10
    enemy.sety(ey)
    player.sety(player.y)
rocket.showturtle()
rocket.setposition(ex + 50,ey)
time.sleep(0.1)
rocket.shape("sprite/explosion.gif")
rocket.setx(ex)
time.sleep(0.1)
rocket.shape("sprite/explosion2.gif")
time.sleep(0.1)
ex -= 30
enemy.setx(ex)
rocket.shape("sprite/explosion3.gif")
time.sleep(0.1)
ex -= 40
enemy.setx(ex)
rocket.shape("sprite/explosion4.gif")
time.sleep(0.1)
ex -= 50
enemy.setx(ex)
rocket.shape("sprite/explosion5.gif")
time.sleep(0.1)
ex -= 60
enemy.setx(ex)
rocket.shape("sprite/explosion6.gif")
time.sleep(0.1)
ex -= 70
enemy.setx(ex)
rocket.shape("sprite/explosion7.gif")
time.sleep(0.1)
ex -= 80
enemy.setx(ex)
rocket.shape("sprite/explosion8.gif")
time.sleep(0.1)
ex -= 90
enemy.setx(ex)
rocket.shape("sprite/explosion9.gif")
time.sleep(0.1)
ex -= 100
enemy.setx(ex)
rocket.shape("sprite/explosion10.gif")
time.sleep(0.1)
ex -= 110
enemy.setx(ex)
rocket.hideturtle()
for i in range(10):
    player.y -= 10
    player.sety(player.y)
player.shape("sprite/player.gif")
time.sleep(0.1)
player.setposition(0,10)
fire.showturtle()
time.sleep(0.1)
player.setposition(0,50)
def right():
    player.x += 10
    player.shape("sprite/player.gif")
    player.setx(player.x)
    fire.setx(player.x)
    if player.x == 510:
        print("Chapitre 2")
def left():
    player.x -= 10
    player.shape("sprite/player2.gif")
    player.setx(player.x)
    fire.setx(player.x)
t.listen()
t.onkey(right,"Right")
t.onkey(left,"Left")
while True:
    if player.x == 510:
        print("chapitre 2")
    enemy.shape("sprite/alien.gif")
    time.sleep(0.1)
    enemy.shape("sprite/alien2.gif")
    time.sleep(0.1)
    enemy.shape("sprite/alien3.gif")
    time.sleep(0.1)
    fire.shape("sprite/fire1.gif")
    time.sleep(0.1)
    fire.shape("sprite/fire2.gif")
    time.sleep(0.1)
    fire.shape("sprite/fire3.gif")
    time.sleep(0.1)
    fire.shape("sprite/fire4.gif")
    time.sleep(0.1)


