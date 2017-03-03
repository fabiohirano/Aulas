def setup():
    size(500,500)
    noStroke()
    
def draw():
    background(random(200), random(200), random(200))
    fill(200, 200, 200)
    ellipse(250, 250, 400, 400)
    fill(200, 0, 0)
    ellipse(250, 250, 400, 23)
    fill(0, 200, 0)
    ellipse(250, 250, 90, 90)
    line(250, 50, 250, 450)
    line(108, 108, 392, 392)
    print (mouseX, mouseY)
