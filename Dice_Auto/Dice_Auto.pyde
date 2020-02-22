InvertNum1= 0
InvertNum2= 0
InvertNum3= 0
InvertNum4= 0
InvertNum5= 0
InvertNum6= 0
counter = 0
RandNum = random(1,6)
def setup():
    size(700,700)
    background(255)
    stroke(0,0,0)
    strokeWeight(4)
    fill(255, 255, 255)
    rect(100,100,400,400,20)
    
        
def draw():
    global counter,InvertNum1, InvertNum2,InvertNum3,InvertNum4,InvertNum5,InvertNum6
    background(255)
    fill(255, 255, 255)
    rect(100,100,400,400,20)
        
    RandNum = random(0,6)
    if(0<=RandNum<1):
        fill(0)
        circle(300,300,50)
        InvertNum1 = InvertNum1 -1  
    if(1<=RandNum<2):
        fill(0)
        circle(200,200,50)
        fill(0)
        circle(400,400,50)
        InvertNum2 = InvertNum2 -1 
    if(2<=RandNum<3):
        fill(0)
        circle(200,200,50)
        fill(0)
        circle(300,300,50)
        fill(0)
        circle(400,400,50)
        InvertNum3 = InvertNum3 -1 
    if(3<=RandNum<4):
        fill(0)
        circle(200,200,50)
        fill(0)
        circle(200,400,50)
        fill(0)
        circle(400,200,50)
        fill(0)
        circle(400,400,50)
        InvertNum4 = InvertNum4 -1 
    if(4<=RandNum<5):
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
        InvertNum5 = InvertNum5 -1 
    if(5<=RandNum<6):
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
        InvertNum6 = InvertNum6 -1 

    fill(255,0,0)
    rect(550,500,10,InvertNum1)
    fill(0,255,0)
    rect(570,500,10,InvertNum2)
    fill(0,0,255)
    rect(590,500,10,InvertNum3)
    fill(0,255,255)
    rect(610,500,10,InvertNum4)
    fill(255,255,0)
    rect(630,500,10,InvertNum5)
    fill(255,170,0)
    rect(650,500,10,InvertNum6)
    counter+=1
    fill(0)
    textSize(30)
    text("rolls",350,550,100)
    text(counter,430,550)
    delay(15);
