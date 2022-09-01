#!/usr/bin/env python3
# Cyclist.py

#	~ Enzo Zavorski Delevatti
#	Aug 2022


import os, time
import Cyclist_ASCII

slash = '\\' if os.getenv('OS') else '/'

def clear():
    if(os.getenv('OS')):
        os.system('cls')
    else:
        os.system('clear')



def Splash():
    clear()
    for line in Cyclist_ASCII.splash:
        print(line)
        time.sleep(0.05)
    time.sleep(3)


def Menu():
    clear()
    print()


if __name__ == "__main__":
    Splash()
    Menu()