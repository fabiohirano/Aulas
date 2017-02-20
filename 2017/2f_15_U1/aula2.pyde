def setup():
    global x, y
    x = width/2
    y = height/2
    size(500,500)
    background(0, 0, 0)
    
def draw():
    global x, y
    #background(random(255), random(255), random(255))
    step = 100
    rectMode(CENTER)
    this_x = x + random(-step, step)
    if (this_x > width):
        this_x = width
    if (this_x < 0):
        this_x = 0
    this_y = y + random(-step, step)
    if (this_y > height):
        this_y = height
    if (this_y < 0):
        this_y = 0
    
    stroke(255)
    strokeWeight(2)
    
    line (x, y, this_x, this_y)   
    #rect (this_x, this_y, 5, 5)
    x = this_x
    y = this_y
