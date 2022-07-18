import os
import colorama
from colorama import Fore
from colorama import Style
from time import sleep

colorama.init(autoreset=True)
a = []
b= ""
astr = ""
top3 = 0
myBool =True
print("\nStarting In ...")
sleep(1)
print(f"{Fore.RED}\n3")
sleep(1)
print(f"{Fore.YELLOW}2")
sleep(1)
print(f"{Fore.GREEN}1!\n")
sleep(1.3)
arr = [Fore.RED, Fore.MAGENTA, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
for i in range(3):
   size = os.get_terminal_size()
   cols = size.columns
   color = 0
   for i in range(cols):
      a += "\\" # Backslash
   for i in range(cols):
      top3 += 1
      if top3 == 3:
         color += 1
         top3 = 0
      if color == 5:
         color = 0
      astr = ""
      a.pop(len(a)-1)
      size = os.get_terminal_size()
      cols = size.columns
      b += "#"
      for i in a:
         astr += i
      print(f"{Style.DIM}{astr}", end="")
      print(f"{arr[color]}{b}")
      sleep(0.015)
   a = []
   b= ""
   astr = ""
   myBool =True
   for i in range(cols):
      a += "#"
   for i in range(cols):
      top3 += 1
      if top3 == 3:
         color += 1
         top3 = 0
      if color == 5:
         color = 0
      astr = ""
      size = os.get_terminal_size()
      cols = size.columns
      a.pop(len(a)-1)
      b += "\\" # Backlash
      for i in a:
         astr += i
      print(f"{Style.DIM}{b}", end="")
      print(f"{arr[color]}{astr}")
      sleep(0.015)
   a = []
   b = ""
   astr = ""
