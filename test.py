import turtle as t
import time
t.register_shape("fire1.gif")
t.register_shape("fire2.gif")
t.register_shape("fire3.gif")
t.register_shape("fire4.gif")
wn = t.Screen()
wn.title("fire animation test")
fire = t.Turtle()
while True:
    fire.shape("fire1.gif")
    time.sleep(0.1)
    fire.shape("fire2.gif")
    time.sleep(0.1)
    fire.shape("fire3.gif")
    time.sleep(0.1)
    fire.shape("fire4.gif")
    time.sleep(0.1)

