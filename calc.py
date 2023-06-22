 # calculate.py
 # Made by pnkprst 2022-09-14
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

# Base of Calculator
class CalculaterData:
    display = 0.0 # main value
    op = ''
    def disp_setting(self, value):
        self.display = float(value)
    def disp_clear(self):
        self.display = 0.0
    def disp_change(self, value=0.0):
        match self.op:
            case '+':
                self.display += float(value)
            case '-':
                self.display -= float(value)
            case '*':
                self.display *= float(value)
            case '/':
                if not float(value):
                    raise Exception("Do not divide by 0.")
                self.display /= float(value)
            case '|':
                self.display *= -1
            case 'S':
                self.display **= 2
            case 'C':
                self.display **= 3
            case 'v':
                if self.display < 0:
                    raise Exception("Do not get root from negative.")
                self.display **= 1 / 2
            case 'V':
                self.display **= 1 / 3
        self.set_prev(float(value))
        self.op = ''

    memory = 0.0
    def mem_change(self, op: str):
        match op:
            case '+':
                self.memory += self.display
            case '-':
                self.memory -= self.display
            case 'r':
                self.display = self.memory
            case 'c':
                self.memory = 0.0
                
    prev_num = 0.0
    prev_op = ''
    def set_prev(self, num: float):
        self.prev_op = self.op
        self.prev_num = num
    def repeat(self):
        self.op = self.prev_op
        self.disp_change(self.prev_num)
        
    
        
if __name__ == "__main__":
    # Set
    calc = CalculaterData()
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