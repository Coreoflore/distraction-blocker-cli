import time 
import platform
from datetime import datetime 

def WindowsBlocker(Websites):
    with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as hosts:
        hosts.writelines(Websites)
        print("Websites blocked! ", Websites)

def WindowsUnblocker(Websites):
    Clean = []
    with open(r"C:\Windows\System32\drivers\etc\hosts", "r") as hosts:
        Content = hosts.readlines()
    
    for line in Content:
        is_safe_to_keep = True
        for site in Websites:
            if site in line:
                is_safe_to_keep = False 
                break  
        
        if is_safe_to_keep:
            Clean.append(line)

    with open(r"C:\Windows\System32\drivers\etc\hosts", "w") as hosts:
        for line in Clean:
            hosts.write(line)
        
def MacBlocker(Websites):
    with open(r"/etc/hosts", "a") as hosts:
        hosts.writelines(Websites)
        print("Websites blocked! ", Websites)

def MacUnblocker(Websites):
    Clean = []
    with open(r"/etc/hosts", "r") as hosts:
        Content = hosts.readlines()
    
    for line in Content:
        is_safe_to_keep = True
        for site in Websites:
            if site in line:
                is_safe_to_keep = False 
                break  
        
        if is_safe_to_keep:
            Clean.append(line)

    with open(r"/etc/hosts", "w") as hosts:
        for line in Clean:
            hosts.write(line)

Websites = []
blockcounter = 0
starthr = int(input("Please enter your starting hour of working hour: "))
endhr = int(input("Please enter your ending hour of working hour: "))
count = int(input("Enter the number of websites to be blocked during working hours: "))

for i in range(count):
    Website = str(input("Enter the website url (Do not use URL) Example- www.youtube.com :-  "))
    Websites.append("127.0.0.1 " + Website + "\n")

while True:
    Currenthr = datetime.now().hour
    
    if platform.system() == "Windows":
        if starthr <= Currenthr <= endhr:
            if blockcounter == 0:
                WindowsBlocker(Websites)
                blockcounter = 1
        else: 
            if blockcounter == 1:
                WindowsUnblocker(Websites)
                blockcounter = 0
    
    if platform.system() in ["Darwin", "Linux"]:
        if starthr <= Currenthr <= endhr:
            if blockcounter == 0:
                MacBlocker(Websites)
                blockcounter = 1
        else: 
            if blockcounter == 1:
                MacUnblocker(Websites)
                blockcounter = 0

    time.sleep(60)
