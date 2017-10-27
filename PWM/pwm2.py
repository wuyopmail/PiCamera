import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,50)
p.start(0)

#p.ChangeDutyCycle(-10)
#time.sleep(0.1)
for i in range(0,181,10):  
    p.ChangeDutyCycle(2.5 + 10 * i / 180) # tested worked.
    time.sleep(0.02)                    
    p.ChangeDutyCycle(0)                
    time.sleep(0.2)
     
p.stop()
GPIO.cleanup()
