Xlst = list()
Ylst = list()
Color = list()

NumOfHumans = 10


def setup():
    global Xlst,Ylst, NumOfHumans
    size(500,500)
    
    for i in range(NumOfHumans):
        ValX = int(random(50,450))
        Xlst.append(ValX)
        ValY = int(random(50,450))
        Ylst.append(ValY)
        
    print(Xlst)
    print(Ylst)  
    
def draw():
    global Xlst,Ylst, NumOfHumans
    background(255)
    strokeWeight(2)
    
    for i in range(NumOfHumans):
        circle(Xlst[i], Ylst[i], 40) 
        Xlst[i] = Xlst[i] + random(-10,10)
        Ylst[i] = Ylst[i] + random(-10,10)
        
        if Xlst[i] > 500:
            Xlst[i] = 500
        if Xlst[i] < 0:
            Xlst[i] = 0
        if Ylst[i] > 500:
            Ylst[i] = 500
        if Ylst[i] < 0:
            Ylst[i] = 0
        
    delay(100)
    
