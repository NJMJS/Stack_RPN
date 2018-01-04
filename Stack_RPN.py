class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        ret = self.stack[len(self.stack)-1]
        self.stack = self.stack[:len(self.stack)-1]
        return ret

    def peak(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

        
class postfix:
    def __init__(self,eq):
        self.ops = {"+","-","*","/"}
        self.infix = eq
        self.post_fix()

    def precedence(self,a):
        if a == "+" or a == "-":
            return 2
        if a == "*" or a == "/":
            return 3
        if a == "(":
            return 1

    def isOpp(self, a):
        if a in self.ops:
            return True
        return False

    def post_fix(self):
        loc = 0
        self.pollish = []
        tokens = self.infix.split()
        opps = stack()
        
        for tok in tokens:
            if tok == ")":
                cont = opps.pop()
                while cont != "(":
                    self.pollish.append(cont)
                    cont = opps.pop()
                    
            elif tok == "(":
                opps.push("(")

            else:
                if self.isOpp(tok):
                    peak = opps.peak()
                    if opps.peak() == None:
                        opps.push(tok)
                    elif self.precedence(tok) > self.precedence(opps.peak()):
                        opps.push(tok)
                    else:
                        peak = opps.peak()
                        while peak != None and self.precedence(tok) <= self.precedence(peak):
                            self.pollish.append(opps.pop())
                            peak = opps.peak()
                        opps.push(tok)
                        
                else:
                    num = int(tok)
                    self.pollish.append(num)
                    
        peak = opps.peak()
        while peak != None:
            self.pollish.append(opps.pop())
            peak = opps.peak()

    def solve(self):
        temp = stack()
        good = True
        for token in self.pollish:
            if self.isOpp(token):
                b = temp.pop()
                a = temp.pop()
                if token == "+":
                    temp.push(a+b)
                elif token == "-":
                    temp.push(a-b)
                elif token == "*":
                    temp.push(a*b)
                elif token == "/":
                    try:
                        temp.push(a/b)
                    except:
                        print("Attempted to div by 0.")
                        good = False
                        break
            else:
                temp.push(token)
        if good:
            return temp.pop()
        else:
            return float('inf')


def test():
    test = postfix("3 + 4 * 2 / ( 1 - 5 )")
    #print(test.pollish)
    print(test.solve())
    test2 = postfix("15 + 15 * 15 / ( 15 - 15 )")
    #print(test2.pollish)
    print(test2.solve())
