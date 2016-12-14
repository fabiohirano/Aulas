class Mover(object):
    def __init__(self, m, x, y):
        self.position = PVector(x, y)
        self.velocity = PVector(0,0)
        self.acceleration = PVector(0,0)
        self.mass = m
        
    def applyForce(self, force):
        # Newton's Second Law: F = M * A
        # or A = F / M

        # divide by mass
        f = PVector.div(force, self.mass)

        # accumulate all forces in a acceleration
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127, 200)
        ellipse(self.position.x, self.position.y, self.mass*16, self.mass*16)
    
    def checkEdges(self):
        # Bounce off the bottom of the window.
        if (self.position.y > height - self.mass*16/2):
            self.position.y = height - self.mass*8

            # A little dampening when hitting the bottom
            self.velocity.y *= -0.9
            
def setup():
    size(500, 500)
    global objetos
    objetos = []
    for i in range(20):
        objetos.append(Mover(random(1, 5), width/2, 0))
        
def draw():
    background(255)
    
    for m in objetos:
        gravidade = PVector(0, 0.1 * m.mass)
        vento = PVector(0.1, 0)
        m.applyForce(gravidade)
        m.applyForce(vento)
        
        m.update()
        m.display()
        m.checkEdges()
