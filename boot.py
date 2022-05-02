from board import *
import digitalio
import storage

btn1p = digitalio.DigitalInOut(GP18)
btn1p.switch_to_input(pull=digitalio.Pull.DOWN)

btn2p = digitalio.DigitalInOut(GP19)
btn2p.switch_to_input(pull=digitalio.Pull.DOWN)

btn3p = digitalio.DigitalInOut(GP26)
btn3p.switch_to_input(pull=digitalio.Pull.DOWN)

btn4p = digitalio.DigitalInOut(GP28)
btn4p.switch_to_input(pull=digitalio.Pull.DOWN)

storage.disable_usb_drive()

if (btn1p.value & btn2p.value & btn3p.value & btn4p.value):
    storage.enable_usb_drive()
    
    
