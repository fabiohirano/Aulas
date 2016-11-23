global numeroDeTela
global gravidade
global bolaX, bolaY
global velY, velX
global resistencia
global tamanhoRaquete
global espessuraRaquete
global tamanhoBola
global forcaRaquete
global velocidadeMuro
global espessuraMuro
global alturaMuro
global muroX, muroY

forcaRaquete = 20
tamanhoRaquete = 100
espessuraRaquete = 15
tamanhoBola = 20
resistencia = 0.01
gravidade = 1
velX, velY = 2, 0
bolaX, bolaY = 200, 50
velocidadeMuro = 5
espessuraMuro = 100
alturaMuro = 20
muroX, muroY = 0, 0

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
    background(0)
    imageMode(CENTER)
    image(img, width/2, height/2)
    desenhaBola()
    desenhaRaquete()
    cai()
    quica(height, 1)
    quica(0, 1)
    quica(width, 0)
    quica(0, 0)
    bateRaquete()
    muro()

def muro():
    desenhaMuro()
    if muroX <= 0:
        reiniciaMuro()
    else:
        moveMuro()
        bateMuro()

def desenhaMuro():
    rectMode(CENTER)
    fill (255,69,0)
    rect (muroX, height - muroY, espessuraMuro, alturaMuro)

def bateMuro():
    pass

def reiniciaMuro():
    global muroX, muroY
    global alturaMuro
    alturaMuro = random(20, height - 100)
    muroX = width
    muroY = alturaMuro/2
    
def moveMuro():
    global muroX
    muroX -= velocidadeMuro
    
def bateRaquete():
    global bolaY, velY, velX
    overhead = mouseY - pmouseY
    if ((bolaX + (tamanhoBola/2) > (mouseX - tamanhoRaquete/2)) and
            (bolaX - (tamanhoBola/2) < (mouseX + tamanhoRaquete/2))):
        if ((dist(bolaX, bolaY, bolaX, mouseY) <= (tamanhoBola/2) + abs(overhead))):
                quica(mouseY, 1)
                velX = (bolaX - mouseX)/5
                if overhead < 0:
                    bolaY += overhead
                    velY += overhead/4    
    
def desenhaRaquete():
    fill (255)
    rectMode(CENTER)
    rect(mouseX, mouseY, tamanhoRaquete, espessuraRaquete)
    
def desenhaBola():
    fill (255, 0, 255)
    ellipse(bolaX, bolaY, tamanhoBola, tamanhoBola)    

def cai():
    global bolaY, bolaX
    global velY, velX
    velY += gravidade
    bolaY += velY
    bolaX += velX
    
def quica(onde, direcao):
    global bolaY, bolaX
    global velY, velX
    if direcao == 1:
        if onde == height:
            if bolaY > height:
                bolaY = height
                velY = (-(1 - resistencia)) * velY
        elif onde == 0:
            if bolaY < 0:
                bolaY = 0
                velY = (-(1 - resistencia)) * velY
        else:
            bolaY = onde
            velY = (-(1 - resistencia)) * velY                    
    if direcao == 0:    
        if onde == width:
            if bolaX > width:
                bolaX = width
                velX = (-(1 - resistencia)) * velX
        if onde == 0:
            if bolaX < 0:
                bolaX = 0
                velX = (-(1 - resistencia)) * velX
