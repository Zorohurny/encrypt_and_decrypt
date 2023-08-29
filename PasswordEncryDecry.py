import time
import os
import sys

banner = '''
████████████████████████████████████████████████
█░░░░░░░░░░░░░░██████████████████████░░░░░░░░███
█░░▄▀▄▀▄▀▄▀▄▀░░██████████████████████░░▄▀▄▀░░███
█░░░░░░░░░░▄▀░░████████░░░░░░████████░░░░▄▀░░███
█████████░░▄▀░░████████░░▄▀░░██████████░░▄▀░░███
█░░░░░░░░░░▄▀░░████░░░░░░▄▀░░░░░░██████░░▄▀░░███
█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀░░███
█░░░░░░░░░░▄▀░░████░░░░░░▄▀░░░░░░██████░░▄▀░░███
█████████░░▄▀░░████████░░▄▀░░██████████░░▄▀░░███
█░░░░░░░░░░▄▀░░████████░░░░░░████████░░░░▄▀░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░██████████████████████░░▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░██████████████████████░░░░░░░░░░█
████████████████████████████████████████████████

Note :- Password must be at least 8 characters'''

options = '''
1. Encryption 
2. Decryption
3. Exit
:- '''

def Encryption(): #Encryption
    passw = input("Enter Password :- ")  # Get User password
    i = 3
    lengh = len(passw)

    if lengh<8:
        print("Password must be at least 8 characters")

    else:
        First_3 = passw[0:3]
        Last_3 = passw[lengh - i:]
        Fourth = passw[3]
        other = passw[4:-3:]

        revers = f"{Fourth}{Last_3}{other}{First_3}"
        print("\n",revers,"\n")

def Decryption(): #Decryption
    passw = input("Enter Password :- ")  # Get User password
    i = 3
    lengh = len(passw)

    First_3 = passw[1:4]
    Last_3 = passw[lengh - i:]
    Fourth = passw[0]
    other = passw[4:-3:]

    normal = f"{Last_3}{Fourth}{other}{First_3}"
    print("\n",normal,"\n")

def loading_animation(duration, interval=0.1):
    start_time = time.time()
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    while time.time() - start_time < duration:
        elapsed_time = time.time() - start_time
        progress = min(1.0, elapsed_time / duration)
        index = int(progress * len(animation)) % len(animation)
        symbol = animation[index]
        sys.stdout.write("\rLoading: {} {:.1%}".format(symbol, progress))
        sys.stdout.flush()
        time.sleep(interval)

    os.system("cls")
    sys.stdout.write(banner)
    sys.stdout.flush()


# --- main code start ---
loading_animation(duration=2)

while True:
    userOption = input(options)
    if userOption == "1":
        Encryption()
    elif userOption == "2":
        Decryption()
    elif userOption == "3":
        exit()
    else:
        print("Select Right Option")

