
def setup():
    size(600,600)
    background(255)
    stroke(0,0,0)
    strokeWeight(4);
    fill(255, 255, 255)
    rect(100,100,400,400,20)
def draw():
    print("")


def mouseClicked():
    if(100<mouseX<400 and 100<mouseY<400):
        RandNum = random(1,6)
        if(1<=RandNum<2):
            fill(255, 255, 255)
            rect(100,100,400,400,20)
            fill(0)
            circle(300,300,50)
        if(2<=RandNum<3):
            fill(255, 255, 255)
            rect(100,100,400,400,20)
            fill(0)
            circle(200,200,50)
            fill(0)
            circle(400,400,50)
        if(3<=RandNum<4):
           fill(255, 255, 255)
           rect(100,100,400,400,20)
           fill(0)
           circle(200,200,50)
           fill(0)
           circle(300,300,50)
           fill(0)
           circle(400,400,50)
        if(4<=RandNum<5):
            fill(255, 255, 255)
            rect(100,100,400,400,20)
            fill(0)
            circle(200,200,50)
            fill(0)
            circle(200,400,50)
            fill(0)
            circle(400,200,50)
            fill(0)
            circle(400,400,50)
        if(5<=RandNum<6):
            fill(255, 255, 255)
            rect(100,100,400,400,20)
            fill(0)
            circle(200,200,50)
            fill(0)
            circle(200,400,50)
            fill(0)
            circle(300,300,50)
            fill(0)
            circle(400,200,50)
            fill(0)
            circle(400,400,50)
        if(6<=RandNum<7):
            fill(255, 255, 255)
            rect(100,100,400,400,20)
            fill(0)
            circle(200,200,50)
            fill(0)
            circle(200,300,50)
            fill(0)
            circle(200,400,50)
            fill(0)
            circle(400,200,50)
            fill(0)
            circle(400,300,50)
            fill(0)
            circle(400,400,50)
    
    

    
    
    


    

    
    
