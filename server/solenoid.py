import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
buzzer =21
lock = 20
fan = 19
pins = (13,6,5) # R=13, G=6, B=5

def lock_OFF() :
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(lock,GPIO.OUT)
    GPIO.output(lock,True)
    
def lock_ON() :
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(lock,GPIO.OUT)
    GPIO.output(lock,False)
    
def fan_ON() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan,GPIO.OUT)
    GPIO.output(fan,True)
    
    
def fan_OFF() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan,GPIO.OUT)
    GPIO.output(fan,False)
    

# buzzer

def buzz_ON() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(buzzer,780)
    pwm.start(80.0)
    time.sleep(0.2)
    pwm.stop()
    GPIO.cleanup(buzzer)
    
    
def led(pins, color, t):
    RGBs = (
        (1,1,1), #White
        (1,0,0), #Red
        (0,1,0), #Green
        (0,0,1), #Blue
        (0,1,1),
        (1,0,1), #Puple
        (1,1,0), #Yellow
        (0,0,0)
    )
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins[0], GPIO.OUT)
    GPIO.setup(pins[1], GPIO.OUT)
    GPIO.setup(pins[2], GPIO.OUT)
    GPIO.output(pins[0], RGBs[color][0])
    GPIO.output(pins[1], RGBs[color][1])
    GPIO.output(pins[2], RGBs[color][2])
    
def led2(pins, color, t):
    RGBs = (
        (1,1,1), #White
        (1,0,0), #Red
        (0,1,0), #Green
        (0,0,1), #Blue
        (0,1,1),
        (1,0,1), #Puple
        (1,1,0), #Yellow
        (0,0,0)
    )
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins[0], GPIO.OUT)
    GPIO.setup(pins[1], GPIO.OUT)
    GPIO.setup(pins[2], GPIO.OUT)
    GPIO.output(pins[0], RGBs[color][0])
    GPIO.output(pins[1], RGBs[color][1])
    GPIO.output(pins[2], RGBs[color][2])
    
    time.sleep(t)

    GPIO.cleanup(pins)
    
def ledOFF() :
    
    GPIO.cleanup()
    
    


    

    
    
    
