y = 0
y1 = 270
y2 = 220
y3 = 320
interval = 4000
timer = 0
def setup():
   size(500,600)
   background(255)
   timer=millis()
    
    
def draw():
    global interval, timer
    stroke(0)
    #line 1
    #line main
    line(100,100,400,100)
    #left side
    line(50,50,100,100)
    line(50,150,100,100)
    #right side
    line(400,100,450,50)
    line(400,100,450,150)
    stroke(0)
    #line 2
    #line main
    line(100,y1,400,y1)
    #left side
    line(150,y2,100,y1)
    line(150,y3,100,y1)
    #right side
    line(400,y1,350,y2)
    line(400,y1,350,y3)
    rect(150,350,200,100,10)
    if(150 <= mouseX <= 350 and 350 <= mouseY <= 450 ): 
        fill(105)
        rect(150,350,200,100,10)
        fill(255)
        textSize(45)
        text("same",190,412)
        stroke(255,0,0)
        line(100,0,100,height)
        line(400,0,400,height)
    else:
        fill(255)
        rect(150,350,200,100,10)
        stroke(255)
        line(100,0,100,height)
        line(400,0,400,height)

    # if(millis() > timer + interval):
    #     timer = millis()
        

    
     
    

    

    



   

        


    

    
