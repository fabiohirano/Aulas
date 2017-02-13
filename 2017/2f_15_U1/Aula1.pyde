def setup():
    size(500,500)
    
def draw():
    #background(0, 200, 0)
    rectMode(CENTER)
    i = int(random(200))
    print(i)
    # if (i % 2 == 0):
    #     fill(random(255), random(255), random(255))
    #     rect(mouseX, mouseY, random(20, 50), random(20,50))
    # else:
    #     fill(random(255), random(255), random(255))
    #     ellipse(mouseX, mouseY, random(20, 50), random(20,50))
    fill(random(255), random(255), random(255))
    rect(mouseX, mouseY, random(20, 50), random(20,50))
    o = random(20, 50)
    ellipse(mouseX, mouseY, o, o)
