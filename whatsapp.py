import pywhatkit
import keyboard
from pyautogui import click , position
import time
def whatsapp_msg(num,msg):
    pywhatkit.sendwhatmsg_instantly(f"+20{num}",msg)
    time.sleep(5)
    click(x=704, y=704)
    keyboard.press('enter')



phone_contact = dict()
def add_new_contact(name,num):
    phone_contact[name] = num

while True:
    name = input("Enter contact name : ")
    number = input("Enter contact number : ")
    if not number.startswith('1') or len(number)!=10:
        break 
    else:
        add_new_contact(name,number)

File = open('contact.txt','a')
File.write(f'{phone_contact}')
File.close() 


