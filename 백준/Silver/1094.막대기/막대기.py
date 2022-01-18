class mkStick:
    def __init__(self, ins):
        self.init = 64 
        self.ins = int(ins)

    def mkDiv(self):
        bin = [0]*7
        var = self.ins
        stick = self.init
        for t in range( len(bin) ):
            while(var >= stick):
                bin[t] += 1
                var -= stick
            stick /= 2
        return bin
           
    def getStick(self):
        result = 0
        bin = self.mkDiv()
        for m in bin:
            result += m
        return result

x = input()
stick = mkStick(x)
print( stick.getStick() )