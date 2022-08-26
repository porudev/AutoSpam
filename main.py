import pyautogui
import pyperclip
import random
import time
import os
from colorama import Fore

os.system("clear")
msg = input(Fore.CYAN+'[1] Enter the content (You can enter multiple content at the same time to the separator by ||): ').split(" || ")
times = int(input(Fore.CYAN+"[2] Enter the number of times: "))
delaytime = float(input(Fore.CYAN+"[3] Delay time: "))

print(Fore.YELLOW +"[>] Check dependencies ...")
print(Fore.GREEN +"[>] Check dependencies successfully")
print(Fore.MAGENTA +"Starting after ...")
time.sleep(0.8)

# Count to 5
for i in range(3,0,-1):
	print(Fore.RED +"[+]", i,end="\n",flush='True')
	time.sleep(0.5)
print(Fore.CYAN+"[>] Starting ...")
time.sleep(0.7)
print(Fore.YELLOW+"[>] Spamming ...")
time.sleep(0.7)

# Spam
for i in range(times):
	pyperclip.copy(random.choice(msg))
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	time.sleep(delaytime) #delay time

os.system("clear")
time.sleep(0.3)
print(Fore.GREEN+"[ ✔️ ] Done.")
time.sleep(0.4)
print(Fore.CYAN+"[ ⛔ ] Source code was remake by jirodev. Thanks for using it.")
