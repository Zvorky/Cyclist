#!/usr/bin/env python3
# Cyclist.py

#	~ Enzo Zavorski Delevatti
#	Aug 2022


import os, time
import Cyclist_ASCII
import CPI

slash = '\\' if os.getenv('OS') else '/'
CWOffset = 0
selected = ''

def clear():
    if(os.getenv('OS')):
        os.system('cls')
    else:
        os.system('clear')


def ClockWave(offset = 0, repeat = 1):
    clockwave = Cyclist_ASCII.clockwave

    offset = offset % len(clockwave[1])

    return (clockwave[0][offset:len(clockwave[0])] + clockwave[0][0:offset] ) * repeat + '\n' + (clockwave[1][offset:len(clockwave[1])] + clockwave[1][0:offset]) * repeat


def CycleInput():
    global CWOffset
    CWOffset -= 1
    return input(ClockWave(CWOffset) + '   ')


def Splash():
    clear()
    for line in Cyclist_ASCII.splash:
        print(line)
        time.sleep(0.05)
    time.sleep(3)


def Header():
    global selected
    clear()
    print(Cyclist_ASCII.header)
    if(selected):
        print(ClockWave(CWOffset, 2) + '    ' + selected)
    else:
        print(ClockWave(CWOffset, 2) + '    any file selected')

def About():
    clear()
    print(Cyclist_ASCII.about)

def Help():
    clear()
    Header()
    print(Cyclist_ASCII.help)

def Commands():
    clear()
    Header()
    print(Cyclist_ASCII.commandlist)

def Select():
    global selected
    selection = ''
    while(selection != 'prev' and not CPI.checkFile(selection)):
        clear()
        Header()
        print('\n\n\tInsert file path to select\n\n')
        selection = CycleInput()
    if(selection != 'prev'):
        selected = selection
        clear()
        Header()
        print('\n\n\tSelected.')
        time.sleep(3)

def cpi():
    clear()
    Header()
    

pages = {   'about':    About,
            'help':     Help,
            'commands': Commands,
            'select':   Select,
            'cpi':      cpi
        }


if __name__ == "__main__":
    page = 'about'
    prev = []

    # Splash()
    while(page != 'exit'):
        if(page == 'prev'):
            if(len(prev) > 1):
                prev.pop()
            page = prev.pop()

        try:
            pages[page]()

        except KeyError:
            page = prev.pop()
            pages[page]()

            if(page != 'help' and page != 'commands'):
                print('(you can type "help")')

        finally:
            prev.append(page)
            if(page == 'select'):
                prev.pop()
                page = prev.pop()

            else:
                page = CycleInput()
    
    clear()
    Splash()
    clear()