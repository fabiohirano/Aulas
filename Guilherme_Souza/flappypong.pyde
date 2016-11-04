global tela
global bolaX, bolaY
global velBolaVertical
tela = 0
bolaX, bolaY = 0, 0
tamanhoBola = 20
corBola = color(255)
gravidade = 1
velBolaVertical = 1

def setup():
    global bolaX, bolaY
    size(500, 500)
    bolaX, bolaY = width/2, height/5




def draw():
    if tela == 0:
        telaInicial()
    elif tela == 1:
        joga()
    elif tela == 2:
        PERDESTE()
    else:
        BUGOU()

def telaInicial():
    background(0)
    textAlign(CENTER)
    text("PUREY", width/2, height/2)
    textSize(30)
    fill(27, 194, 89)
    
def joga():
    background(55, 20, 0)
    aplicagravidade()
    desenhaBola()
    naoFoge()
    
    
def desenhaBola():
    fill(corBola)
    rectMode(CENTER)
    rect(bolaX,  bolaY, tamanhoBola, tamanhoBola)
    
def aplicagravidade():
    global velBolaVertical
    global bolaX, bolaY
    velBolaVertical += gravidade
    bolaY += velBolaVertical
    
def quicachao(superficie):
    global velBolaVertical
    global bolaX, bolaY
    bolaY = superficie - (tamanhoBola/2)
    velBolaVertical *= -1

def quicateto(superficie):
    global velBolaVertical
    global bolaX, bolaY
    bolaY = superficie + (tamanhoBola/2)
    velBolaVertical *= -1
    
def naoFoge():
    if (bolaY + (tamanhoBola/2) > height):
        quicachao(height)
    if (bolaY - (tamanhoBola/2) < 0):
        quicateto(0)
    
def PERDESTE():
    pass
    
def BUGOU():
    pass
    
def mousePressed():
    if tela == 0:
        iniciaJogo()
    
def iniciaJogo():
    global tela
    tela = 1
    
