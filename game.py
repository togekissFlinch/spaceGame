#importer les packages
import turtle as t
import time
#fenêtre
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
def faire_exploser(objet):
    objet.shape("sprite/explosion.gif")
    for i in range(8):
        objet.shape("sprite/explosion" + str(i + 2) + ".gif")
        time.sleep(0.1)
    objet.hideturtle()
def animation(objet,image,nombre):
    for i in range(nombre):
        objet.shape("sprite/" + image + str(i + 2) + ".gif")
        time.sleep(0.1)
#player
player = t.Turtle()
creer(player,0,50,"sprite/player.gif")
#fire
fire = t.Turtle()
creer(fire,0,-40,"sprite/fire1.gif")
#rocket
rocket = t.Turtle()
creer(rocket,600,0,"sprite/rocket.gif")
rocket.hideturtle()
#alien
enemy = t.Turtle()
creer(enemy,0,350,"sprite/alien.gif")
#bomb
bomb = t.Turtle()
creer(bomb,enemy.xcor(),enemy.ycor(),"sprite/bomb.gif")
#cinématic
bomb.hideturtle()
bomb.showturtle()
bomb.setposition(player.x,player.y)
faire_exploser(bomb)
player.shape("sprite/player.gif")
fire.hideturtle()
time.sleep(0.1)
player.shape("sprite/player3.gif")
for i in range(10):
    player.y -= 10
    player.sety(player.y)
for i in range(33):
    animation(enemy,"alien",2)
    player.y += 10
    player.sety(player.y)
for i in range(10):
    player.y += 10
rocket.showturtle()
rocket.setposition(enemy.xcor(),enemy.ycor())
faire_exploser(rocket)
rocket.hideturtle()
enemy.setposition(-999,350)
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
    animation(fire,"fire",3)
def left():
    player.x -= 10
    player.shape("sprite/player2.gif")
    player.setx(player.x)
    fire.setx(player.x)
    animation(fire,"fire",3)
t.listen()
t.onkey(right,"Right")
t.onkey(left,"Left")
t.mainloop()
