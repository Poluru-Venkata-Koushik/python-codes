class car:
    def __init__(self,com,mo,yea,cc,sea,door,regno):
        self.make=com
        self.model=mo
        self.year=yea
        self.cceng=cc
        self.seats=sea
        self.doors=door
        self.reg=regno

data=[]

Triber=car("Renault","Triber-RXT-EASY R AMT",2020,999,8,5,"AP39JA9999")
print(Triber.model)