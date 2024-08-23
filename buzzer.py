
from gpiozero import Buzzer
from time import sleep

buz= Buzzer(17)

while True:
    buz.on()
    sleep(0.3)                                                                                                                                                                                                                                                                                                                                                                       
    buz.off()
    sleep(0.3)
