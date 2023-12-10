#speed is in milliseconds
#Makes robot go forward and backwards
from cyberbot import *  #I had to download the cyberbot library for this import

bot(18).servo_speed(75)             # Full speed forward
bot(19).servo_speed(-75)
sleep(3000)
bot(18).servo_speed(None)
bot(19).servo_speed(None)

bot(18).servo_speed(-75)            # Full speed backwards
bot(19).servo_speed(75)
 
sleep(3000)
 
bot(18).servo_speed(None)           # Stop
bot(19).servo_speed(None)           #flash code while at position 1 the flip to position 2, reset button is on the bottom of the microbit next to the usb port 

#makes robot turn in a square
from cyberbot import *

for y in range (0,4):
    bot(18).servo_speed(75)
    bot(19).servo_speed(-75)
    sleep (4000)
    
    bot(18).servo_speed(75)
    bot(19).servo_speed(0)
    
bot(18).servo_speed(0)
bot(19).servo_speed(0)

# USES FUNCTIONS 
from cyberbot import *
# functions with arguments
def straight():         #different functions for the cyber bot
 bot(18).servo_speed(75)
 bot(19).servo_speed(-75)
 sleep (3000)
def right():
 bot(18).servo_speed(75)
 bot(19).servo_speed(0)
 sleep (1100)

def stop():
 bot(18).servo_speed(0)
 bot(19).servo_speed(0)
straight()
right()
straight()
right()
stop()

from microbit import *
import math
import radio

radio.on()
radio.config(channel=7, queue=1, length=64)

sleep(1000)
# rc car controller
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y() 
    
    angle = round( math.degrees( math.atan2(y, x) ) )  #This part of the code acts as a compass for the rc car 
    needle = ( angle + 90 + 15 ) // 30

    print("Send:")
    print("x =", x, ", y =", y, ", needle =", needle)
    print()
    display.show(Image.ALL_CLOCKS[needle])
    
    dictionary = { }
    dictionary['x'] = x
    dictionary['y'] = y
    dictionary['needle'] = needle

    packet = str(dictionary)
    radio.send(packet)

    sleep(500)

# This is what the rc car recieves
from microbit import *
import radio

radio.on()
radio.config(channel=7, queue=1, length=64)

sleep(1000)

while True:

    packet = radio.receive()

    if packet:

        dictionary = eval(packet)

        x = dictionary.get('x')
        y = dictionary.get('y')
        needle = dictionary.get('needle')
        
        print("Receive:")
        print("x =", x, ", y =", y, ", needle =", needle)
        print()
        
        display.show(Image.ALL_CLOCKS[needle])
        
        sleep(500)
def forward():
    bot(18).servo_speed(75)
    bot(19).servo_speed(-75)

def backwards():
    bot(18).servo_speed(-75)
    bot(19).servo_speed(75)
    sleep(250)

def right():
    bot(18).servo_speed(75)
    bot(19).servo_speed(75)
    sleep(250)

def left():
    bot(18).servo_speed(-75)
    bot(19).servo_speed(-75)
    sleep(250)

while True:   #Whiskers used as sensory for the robot 
    whisker_left = bot(7).read_digital()
    whisker_right = bot(9).read_digital()
    
    if whisker_left == 0 and whisker_right == 0:     
        backwards()                                 
        right()
    elif whisker_left == 1 and whisker_right == 0:   
        backwards()                                  
        left()
    elif whisker_left == 0 and whisker_right == 1:  
        backwards()                                   
        right()
    else:                                           
        forward()                         

        #REMEMBER TO SCREW THE BLACK THING IF THE MOTHERBOARD DICONNECTS 
