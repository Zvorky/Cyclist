import os, time

CWOffset = 0
selected = ''

splash = ['',
'                          ==================+++-----         ',
'                          ==============++                   ',
'                          ============+       *##########*   ',
'                          ==========+     *##################',
'                          ========+     *####################',
'                          =======+     ######################',
'                          ======+    *#######################',
'                          ======    *########################',
'                          =====     #########################',
'                          =====    *#########################',
'                          =====    ##########################',
'                          =++      *#########################',
'                                    #########################',
'                            *####*  *########################',
'                           ########  *#######################',
'                           ########    ######################',
'                            *####*      *####################',
'',
' -+=========== ==+       +== -*########### ##             ##  *############ ##############',
'+=+             +==     ==+ *#*            ##             ## ##                   ##      ',
'==                +== ==+   ##             ##             ##  *##########*        ##      ',
'+=+                 ===     *#*            *#*            ##             ##       ##      ',
' -+===========      ===      -*###########  -*########### ## ############*        ##      ',
'']

header = '''=====-                                                   |
===" .o@@o                                               |
==" /@@@@@  .""""" \\\\  // .""""" ||     || .""""" """""" |
""  @@@@@@  l       '||'  l      ||     ||  """".   ||   |
 @) \\@@@@@   """""   ''    """""  """"" '' """""    ''   |
_________________________________________________________|
                                                        /'''

clockwave = ['     ____ ',
             '____|    |']


#  --------------------   ===| Pages |===   --------------------

about = '''
           ==================+++-----         
           ==============++                   
           ============+       *##########*   
           ==========+     *##################
           ========+     *####################
           =======+     ######################
           ======+    *#######################
           ======    *########################
           =====     #########################
           =====    *#########################
           =====    ##########################
           =++      *#########################
                     #########################
             *####*  *########################
            ########  *#######################
            ########    ######################
             *####*      *####################

 Cyclist:  RISC-V Performance Measuremant Tool


          Initially made as a college project, it
        calculates how  much cycles a  multicycle
        RISC-V  processor spends to execute a ma-
        chine language  program,  and it's Cycles
        Per Second average.
        
          By now,  Cyclist supports RV32I instru-
        tions only, without System Calls.
        
                        ~ Enzo 'Zvorky' Delevatti
        
        
        
      See more at https://github.com/Zvorky/Cyclist
'''

commandlist = '''

                  --| Command List |--

             select     - Select file
             cpi        - Calculates CPI for selected file
             prev       - Return to previous page
             commands   - Command List (this page)
             about      - Shows About page
             help       - Shows Help page
             exit       - Finalize Cyclist
'''

help = '''

                      --| Help |--

          Type "commands" to see Command List.
          
          Below Cyclist logotype, at the header,
        you can see  the path to  selected file.

                  More information at:
            https://github.com/Zvorky/Cyclist
'''




def clear():
    if(os.getenv('OS')):
        os.system('cls')
    else:
        os.system('clear')


def ClockWave(offset = 0, repeat = 1):
    offset = offset % len(clockwave[1])

    return (clockwave[0][offset:len(clockwave[0])] + clockwave[0][0:offset] ) * repeat + '\n' + (clockwave[1][offset:len(clockwave[1])] + clockwave[1][0:offset]) * repeat


def CycleInput():
    global CWOffset
    CWOffset -= 1
    return input(ClockWave(CWOffset) + '   ')


def Splash():
    clear()
    for line in splash:
        print(line)
        time.sleep(0.05)
    time.sleep(3)


def Header():
    global selected
    clear()
    print(header)
    if(selected):
        print(ClockWave(CWOffset, 2) + '    ' + selected)
    else:
        print(ClockWave(CWOffset, 2) + '    any file selected')

def About():
    clear()
    print(about)

def Help():
    clear()
    Header()
    print(help)

def Commands():
    clear()
    Header()
    print(commandlist)

def Select():
    clear()
    Header()
    print('\n\n\t\tInsert file path to select\n\n')

def Selected():
    clear()
    Header()
    print('\n\n\t\tFile Selected.\n\n')