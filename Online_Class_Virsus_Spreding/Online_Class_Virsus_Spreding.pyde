Xlst = list()
Ylst = list()
HealthState =[False, True] #False - infected
NumOfHumans = 25
CriticalDist = 40 
iteration = 0
Healthy = NumOfHumans - 1
Infected = 1

def setup():
    global Xlst,Ylst, NumOfHumans,HealthState
    size(600,600)
    
    for i in range(NumOfHumans):
        ValX = int(random(50,450))
        Xlst.append(ValX)
        ValY = int(random(50,450))
        Ylst.append(ValY)
        ValY = int(random(50,450))
        Ylst.append(ValY)
        HealthState.append(True)
        
def distance(x1,x2,y1,y2):
    a = (x1 - x2)
    b = (y1 - y2)
    c = sqrt(a**2 + b**2)
    return c
    
def draw():
    global Xlst,Ylst, HealthState, NumOfHumans, CriticalDist, iteration, Healthy, Infected
    background(255)
    strokeWeight(2)

    
    
    for ind in range(NumOfHumans):
        if HealthState[ind] == True:
            fill(255)   #healthy
            hs = True
        else:
            fill(255, 0, 0) #infected
            hs = False

            
                         
        #movement of the circles   
        circle(Xlst[ind], Ylst[ind], 40) 
        
        #calculating the distance between the circles
        for nei in range(NumOfHumans):
            d = distance(Xlst[ind], Xlst[nei], Ylst[ind], Ylst[nei])
            if nei==ind:
                continue
            
            
            if d < CriticalDist and (HealthState[ind] == False or HealthState[nei] == False):
                #Infection process
                if HealthState[ind] == False and HealthState[nei] == True:
                    Healthy = Healthy - 1
                    Infected = Infected + 1

                
                if HealthState[ind] == True and HealthState[nei] == False:
                    Healthy = Healthy - 1
                    Infected = Infected + 1

   
                    
                    
                HealthState[ind] = False
                HealthState[nei] = False 
                

                       

    for m in range(NumOfHumans):
        Xlst[m] = Xlst[m] + random(-10,10)
        Ylst[m] = Ylst[m] + random(-10,10)
        
        if Xlst[m] > 500:
            Xlst[m] = 500
        if Xlst[m] < 0:
            Xlst[m] = 0
        if Ylst[m] > 500:
            Ylst[m] = 500
        if Ylst[m] < 0:
            Ylst[m] = 0

 

    
    iteration = iteration + 1
    fill(0)
    textSize(20)
    text("iteration = ",50,550)
    text(iteration,160,550)
    
    text("Infected",230, 545)
    text(Infected,550, 545)
    fill(255,0,0)
    rect(315, 530,Infected*5,20)
    fill(0)
    text("Healthy",230, 575)
    text(Healthy,550, 585)
    stroke(0)
    fill(255)
    rect(315, 560,Healthy*5,20)
    
    delay(10)

    
