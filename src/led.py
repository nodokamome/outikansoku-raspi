#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep


def flash_led(color):
    if color=="blue":
        LED=16          #青がGPIO16
    elif color=="green":
        LED=20          #緑がGPIO20
    elif color=="red":
        LED=21          #赤がGPIO21
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)

    #5回点滅させる
    for i in range(5):
        GPIO.output(LED, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(LED, GPIO.LOW)
        sleep(0.5)
    else:
        GPIO.cleanup()

