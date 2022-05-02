from board import *
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import json

time.sleep(3)
print ('author: zdridox')
print ('Version 2.1')
print('config.json')

btn1p = digitalio.DigitalInOut(GP18)
btn1p.switch_to_input(pull=digitalio.Pull.DOWN)

btn2p = digitalio.DigitalInOut(GP19)
btn2p.switch_to_input(pull=digitalio.Pull.DOWN)

btn3p = digitalio.DigitalInOut(GP26)
btn3p.switch_to_input(pull=digitalio.Pull.DOWN)

btn4p = digitalio.DigitalInOut(GP28)
btn4p.switch_to_input(pull=digitalio.Pull.DOWN)

Keyboard1 = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(Keyboard1)

with open("config.json", "r") as f:
    data = json.load(f)

def chat():
    if(data['CHAT'] == 'On'):
        Keyboard1.send(Keycode.T)
        time.sleep(0.1)

def enter():
    if(data['ENTER'] == 'On'):
        Keyboard1.send(Keycode.ENTER)

while True:
    if btn1p.value:
        print("1")
        chat()
        layout.write(data['btn1'])
        enter()
        time.sleep(0.4)
        
        
    if btn2p.value:
        print("2")
        chat()
        layout.write(data['btn2'])
        enter()
        time.sleep(0.4)

        
    if btn3p.value:
        print("3")
        chat()
        layout.write(data['btn3'])
        enter()
        time.sleep(0.4)

        
    if btn4p.value:
        print("4")
        chat()
        layout.write(data['btn4'])
        enter()
        time.sleep(0.4)


    
