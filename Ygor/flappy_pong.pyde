global numeroDeTela
global gravidade
global bolaX, bolaY
global velY
global resistencia
resistencia = 0.01
gravidade = 1
velY = 0
bolaX, bolaY = 200, 50

def setup():
    global numeroDeTela
    global img
    numeroDeTela = 0
    size(500, 500)
    img = loadImage("suplexcity.jpg")
       
def draw():
    if numeroDeTela == 0:
        mostraTelaInicial()
    if numeroDeTela == 1:
        joga()
        
def mostraTelaInicial():
    background(0)
    imageMode(CENTER)
    image(img, width/2, height/2)
    
def mousePressed():
    global numeroDeTela
    if numeroDeTela == 0:
        numeroDeTela = 1
        
def joga():
    imageMode(CENTER)
    image(img, width/2, height/2)
    desenha()
    cai()
    quica()
    
def desenha():
    fill (255, 255, 255)
    ellipse(bolaX, bolaY, 20, 20)    

def cai():
    global bolaY
    global velY
    velY += gravidade
    bolaY += velY
    
def quica():
    global bolaY
    global velY
    if bolaY > height:
        bolaY = height
        velY = (-(1 - resistencia)) * velY
