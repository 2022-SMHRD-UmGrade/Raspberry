from solenoid import *
import time
import requests
import RPi.GPIO as GPIO
from flask import Flask, request, render_template

app = Flask(__name__)       # Flask라는 이름의 객체 생성

@app.route('/')             # 클라이언트가 ui창에다가 /로 접속하면 hello함수 호출
def hello():                # /로 실행하면 호출되는 뷰함수
   return "Hello Flask!"    # 뷰함수는 반드시 retrun이 있어야한다.

@app.route('/ledGreen')
def Qr():
    print("QR")
    buzz_ON()
    led(pins, 2, 0)
    
    return "QR"

@app.route('/OFF')
def OFF():
    fan_OFF()
    lock_ON()
    led(pins, 7, 0)
    return "Rental1"

@app.route('/Rental1')
def Rental1():
    
    buzz_ON()
    lock_OFF()
    led(pins, 2, 0)
    
    print("Rental-1")
    return "Rental1"

@app.route('/Rental2')
def Rental2():
    buzz_ON()
    lock_ON()
    led(pins, 7, 0)
    
    print("Rental-2")
    return "Rental2"

@app.route('/Return1')
def Return1():
    GPIO.cleanup()
    buzz_ON()
    lock_OFF()
    led(pins, 6, 0)
    
    print("Return-1")
    return "Rental1"

@app.route('/Return2')
def Return2():
    buzz_ON()
    led(pins, 7, 0)
    lock_ON()
    fan_ON()
    led(pins, 7, 0)
#     led(pins, 2, 0.)
    print("Return-2")
    return "Rental2"

@app.route('/Cancel')
def Cancel():
    buzz_ON()
    lock_ON()
    led2(pins, 5, 3)
    
    fan_ON()
    return "Cancel"

@app.route('/Broken')
def broken():
    buzz_ON()
    lock_ON()
    led(pins, 3, 0)    
    return "Broken"

@app.route('/Warning')
def warning():
    buzz_ON()
    lock_ON()
    led(pins, 1, 0)
    return "Warning"
 
@app.route('/Catch')
def catch():
    led(pins, 7, 0)
    lock_ON()
    return "Catch"

@app.route('/ledON')
def ledON():
    led(pins, 1, 3)
    return "ledON"

@app.route('/ledOFF')
def ledOFF():
    led(pins, 7, 0)
    return "fan_OFF"


@app.route('/lockOFF')
def lockOFF():
    lock_OFF()
    return "lockOFF"

@app.route('/lockON')
def lockON():
    lock_ON()
    return "lockON"

@app.route('/fanON')
def fanON():
    fan_ON()
    return "fanON"

@app.route('/fanOFF')
def fanOFF():
    fan_OFF()
    return "fanOFF"

@app.route('/buzzON')
def buzzON():
    buzz_ON()
    
    return "buzzON"


if __name__ == "__main__":  # 직접 main을 실행시키기위한 조건
   app.run(host="172.30.1.19", port = "8083")
