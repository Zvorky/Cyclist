#!/usr/bin/env python3
# Cyclist.py

#	~ Enzo Zavorski Delevatti
#	Aug 2022


import os
from modules import CPI, Pages

slash = '\\' if os.getenv('OS') else '/'
selected = ''


def CPI_Page():
    global selected

    Pages.clear()
    Pages.Header()
    
    if(not selected):
        print('\n\n\t\tType "select" to select a file before.\n\n')
        return False

    if(not CPI.checkFile(selected)):
        selected = ''
        print('\n\n\t\tIncompatible or Inexistent File.\n\n')
        return False
    
    cpi = CPI.CPI(selected)
    print('\n\n\t\tCPI = {}\n\n\t\tTotal\n\t\tInstructions: \t{}\n\t\tCycles: \t{}\n'.format(cpi.cpi, cpi.instructions, cpi.cycles))
    Pages.time.sleep(1)
    print('\t\tInstructions with:')
    for i in cpi.CyclesLog():
        print('\t\t' + i)
    Pages.time.sleep(1)
    print('\n')
    log = cpi.log
    while(log):
        print(log[:log.find('\n')])
        log = log[log.find('\n')+1:]
        Pages.time.sleep(0.05)
    print('\n\n')


pages = {   'about':    Pages.About,
            'help':     Pages.Help,
            'commands': Pages.Commands,
            'select':   Pages.Select,
            'cpi':      CPI_Page
        }


if __name__ == "__main__":
    page = 'about'
    prev = []

    Pages.Splash()
    while(page != 'exit'):
        Pages.selected = selected

        if(page == 'back'):
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
                selection = CPI.pathInput(Pages.ClockWave() + '   ')
                if(CPI.checkFile(selection)):
                    Pages.selected = selected = selection
                    Pages.Selected()
                    page = Pages.CycleInput()
                else:
                    page = selection

            else:
                page = Pages.CycleInput()
    
    Pages.clear()
    Pages.Splash()
    Pages.clear()