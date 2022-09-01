#!/usr/bin/env python3
# Cyclist.py

#	~ Enzo Zavorski Delevatti
#	Aug 2022


import os
from modules import CPI, Pages

slash = '\\' if os.getenv('OS') else '/'
selected = ''

pages = {   'about':    Pages.About,
            'help':     Pages.Help,
            'commands': Pages.Commands,
            'select':   Pages.Select,
            'cpi':      None
        }

if __name__ == "__main__":
    page = 'about'
    prev = []

    Pages.Splash()
    while(page != 'exit'):
        Pages.selected = selected

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
                selection = Pages.CycleInput()
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