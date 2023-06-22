 # calculate.py
 # Made by pnkprst 2022-09-14
import ccbase
import os
def clrscr():
    os.system("cls")
def getstdin():
    try:
        return input()
    except KeyboardInterrupt:
        clrscr()
        exit(0)

operator_char = '+-*/'
soloargv_opchar = '|SCvV'
numchar = '0123456789.-'

def chknum(numstr):
    for i in numstr:
        if i not in numchar:
            return False
    return True

        
            
if __name__ == "__main__":
    # Set
    calc = ccbase.CCdata()
    in_data = ""
    
    # Loop
    while True:
        # displaying
        clrscr()
        print(calc.display, end=' ')
        print(calc.op if calc.op !='' else "")
        
        in_data = getstdin()
        
        if not in_data:
            calc.repeat()
            continue
            
        elif in_data == 'c':
            calc.disp_clear()
            continue
            
        elif in_data[0] == 'm':
            calc.mem_change(in_data[1])
            continue
        
        if in_data in soloargv_opchar:
            calc.op = in_data
            calc.disp_change()
        
        if in_data in operator_char:
            calc.op = in_data   
        elif chknum(in_data):
            if calc.op:
                calc.disp_change(in_data)
            else:
                calc.disp_setting(in_data)
