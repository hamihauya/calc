# Base of Calculator
class CCdata:
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
