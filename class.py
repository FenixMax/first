class mg():
    def __init__(self,b):
        self.b=b
    def h(self):
        self.b=str(self.b)
        return len(self.b)
    def u(self):
        if self.b.isdigit()==True:
            self.b=int(self.b)
        if type(self.b) is str:
            sogl=""
            gl=""
            nsogl=0
            ngl=0
            k="aeyuio"
            for i in self.b:
                if i in k:
                    gl+=i
                    ngl+=1
                else:
                    sogl+=i
                    nsogl+=1
            if ngl*nsogl<=self.h():
                print(gl)
            else:
                print(sogl)
        elif type(self.b) is int:
            j="02468"
            r=1
            self.b=str(self.b)
            for i in self.b:
                if i in j:
                    i=int(i)
                    r*=i
            print(r*self.h())
a=mg(input())
a.h()
a.u()


