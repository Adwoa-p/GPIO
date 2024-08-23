
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

from subprocess import call

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing()
