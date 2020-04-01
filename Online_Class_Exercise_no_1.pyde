posX = 300
posY = 300

def setup():
    size(500,500)
    
def draw():
    global posX,posY
    background(255)
    strokeWeight(2)
    
    circle(posX, posY, 40) 
    posX = posX + random(-10,10)
    posY = posY + random(-10,10)
    
    if posX > 500:
        posX = 500
    if posX < 0:
        posX = 0
    if posY > 500:
        posY = 500
    if posY < 0:
        posY = 0
