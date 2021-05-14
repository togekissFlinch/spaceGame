import turtle as t
import time
#fenêtre
window = t.Screen()
window.bgpic("background.gif")
#importer les sprites
t.register_shape("player1.gif")
t.register_shape("player2.gif")
t.register_shape("player3.gif")
t.register_shape("player4.gif")
#joueur
player = t.Turtle()
player.shape("player.gif")
player.penup()
player.setposition(0,90)

