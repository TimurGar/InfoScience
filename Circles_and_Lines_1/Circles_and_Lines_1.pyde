

def setup():
    size(1000,1000)
    background(255)
    textAlign(CENTER)

def draw():
    print("")

    
def mouseClicked():
     x = random(0,1000)
     y = random(0,1000)
     s = random(10,100)
     R = random(0,255)
     G = random(0,255)
     B = random(0,255)
     line(500,500,mouseX,mouseY)
     fill(R,G,B)
     circle(mouseX,mouseY,s)
     print(R,G,B)
     fill(0)
     textSize(s/4)
     text("T&G",mouseX,mouseY)
     
    





    
