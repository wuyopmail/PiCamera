import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,50)
p.start(5)

#p.ChangeDutyCycle(-10)
#time.sleep(0.1)
i = 45
p.ChangeDutyCycle(5) # tested worked.
    

time.sleep(5)
    #p.ChangeDutyCycle(0)                
    #time.sleep(0.2)
     
p.stop()
GPIO.cleanup()