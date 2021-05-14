import turtle as t
import time
#fenêtre
window = t.Screen()
window.bgpic("background.gif")
#importer les sprites
t.register_shape("player.gif")
t.register_shape("player2.gif")
t.register_shape("fire.gif")
t.register_shape("alien.gif")
#joueur
player = t.Turtle()
player.shape("player.gif")
player.penup()
player.setposition(0,90)
#fire
fire = t.Turtle()
fire.shape("fire.gif")
fire.penup()
#enemy
enemy = t.Turtle()
enemy.shape("alien.gif")
enemy.hideturtle()
enemy.penup()
enemy.setposition(-400,-40)
enemy.showturtle()
#mouvements
def right():
    x = player.xcor() 
    ex = enemy.xcor()
    player.shape("player.gif")
    if x > 400:
        x = 400
    if x == ex:
        enemy.shape("fire.gif")
    x += 10
    player.setx(x)
    fire.setx(x)
def left():
    x = player.xcor()
    ex = enemy.xcor()
    player.shape("player2.gif")
    if x < -400:
        x = -400
    if x == ex:
        enemy.shape("fire.gif")
    x -= 10
    player.setx(x)
    fire.setx(x)
t.listen()
t.onkey(right, "Right")
t.onkey(left, "Left")
#boucle
t.mainloop()

