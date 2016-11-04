global JogoDaTela
global bolaX, bolaY
global velocidadeBolaVertical
JogoDaTela = 0
bolaX, bolaY = 0, 0
tamanhoBola = 20
corBola = color(255)
gravidade = 1
velocidadeBolaVertical = 0



def setup():
    global bolaX, bolaY
    size(500, 500)
    bolaX, bolaY = width/2, height/5
    
def draw():
    if JogoDaTela == 0:
        telaInicial()
    elif JogoDaTela == 1:
        joga()
    elif JogoDaTela == 2:
        perdeuTroxa
    else:
        deuRuim()
        
def telaInicial():
    background(0)
    textAlign(CENTER)
    textSize(30)
    fill(158, 156, 252)
    text("Clika pa jogah", width/2, height/2)

    
def joga():
    background(51, 204, 255)
    aplicaGravidade()
    desenhaBola()
    naoFoge()
    
def desenhaBola():
    fill(corBola)
    ellipse(bolaX, bolaY, tamanhoBola, tamanhoBola)

def aplicaGravidade():
    global velocidadeBolaVertical
    global bolaX, bolaY
    
    velocidadeBolaVertical += gravidade
    bolaY += velocidadeBolaVertical

def quicaChao(superfice):
    global velocidadeBolaVertical
    global bolaX, bolaY
    bolaY = superfice - (tamanhoBola/2)
    velocidadeBolaVertical *= -1



def quicaTeto(superfice):
    global velocidadeBolaVertical
    global bolaX, bolaY
    bolaY = superfice - (tamanhoBola/2)
    velocidadeBolaVertical *= -1


def naoFoge():
    if (bolaY + (tamanhoBola/2) > height):
        quicaChao(height)
    if (bolaY - (tamanhoBola/2) < 0):
        quicaChao(0)

def perdeuTroxa():
    pass

def deuRuim():
    pass
    
def mousePressed():
    if JogoDaTela == 0:
        iniciaJogo()
        
def iniciaJogo():
    global JogoDaTela
    JogoDaTela = 1
