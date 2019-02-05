# A simple Finch dance in Python

from finch import Finch
from time import sleep

print("Finch's First Python program.")
# Instantiate the Finch object
snakyFinch = Finch()


# Do a dance.. think of a wheelchair
snakyFinch.buzzer(1.5, 450)
sleep(1.0)
snakyFinch.led(0,255,0)
snakyFinch.wheels(0,1)
sleep(3.05)

snakyFinch.led(0,255,255)
snakyFinch.wheels(0.2,-0.2)
sleep(1)

snakyFinch.led(255,0,0)
snakyFinch.wheels(1,1)  #moving forward
sleep(1.5)

snakyFinch.led(0,255,0)
snakyFinch.wheels(0,1) #more spinning
sleep(1)

snakyFinch.led(0,0,255)
snakyFinch.wheels(1,0) #spinning but in the other directions
sleep(1)

snakyFinch.led(0,255,0)
snakyFinch.wheels(0,1) #one more spin
sleep(1)

snakyFinch.led(255,0,255)
snakyFinch.wheels(-1,-1) #backing up
sleep(0.5)

snakyFinch.led(0,255,255)
snakyFinch.wheels(0.2,-1)
sleep(1)

snakyFinch.led(0,0,255)
snakyFinch.wheels(1,0) #going to the left
sleep(2)

snakyFinch.led(0,255,0)
snakyFinch.wheels(0,1) #going to the right
sleep(2)

snakyFinch.led(255,255,255)
snakyFinch.wheels(0.3,0.3)
sleep(2.5)

snakyFinch.led(255,0,255)
snakyFinch.wheels(-1,-1) #backing up
sleep(0.2)

snakyFinch.buzzer(1.5, 450)
sleep(1.0)

snakyFinch.close();

