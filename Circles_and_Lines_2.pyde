prevX = 0
prevY = 0
x=500
y=500
def setup():
    size(1000,1000)
    background(255)
    textAlign(CENTER)

def draw():
    
    print("")

    
def mouseClicked():
     global prevX, prevY, x,y
     prevX=x
     prevY=y
     x=mouseX
     y=mouseY
     s = random(10,100)
     R = random(0,255)
     G = random(0,255)
     B = random(0,255)
     fill(R,G,B)
     circle(mouseX,mouseY,s)
     stroke(0)
     print(R,G,B)
     fill(0)
     textSize(s/4)
     text("T&G",mouseX,mouseY)
     line(prevX,prevY,mouseX,mouseY)
     
     
    


  

    
