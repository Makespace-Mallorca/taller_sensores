import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#while True:
#	if GPIO.input(10) == GPIO.HIGH:
#		print("Button was pushed")
#		time.sleep(0.10)



