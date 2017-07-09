import RPi.GPIO as GPIO
import time
import os

#set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Doorbell input (in this case pin 15)
GPIO.setup(3, GPIO.OUT) #Output towards relay (in this case pin 3)

#Startup
GPIO.output(3, 1) #Turns off relay

while True:
    input_state = GPIO.input(15)
    if input_state == False:
	time.sleep(0.1) #wait a bit
	GPIO.output(3, 0) #Switch relay on
	time.sleep(1.5) #Time to wait while the physical doorbell rings
	GPIO.output(3, 1) #Switch relay off
	os.system('killall omxplayer.bin') #Kill eventual orphaned instances of omxplayer
	os.system('omxplayer --no-keys /home/pi/doorbell.mp3 &') #trigger MP3
	os.system('./home/pi/tgecho.sh') #Echo doorbell towards Telegram API
	time.sleep(0.1)
        #print('Deurbel!') #Print to terminal as debug
        time.sleep(3) #Kills the doorbell button for 3 seconds

