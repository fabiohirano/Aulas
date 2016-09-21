TAMANHO_BOLA = 20
VEL_JOGADOR = 5
ALTURA_JOGADOR = 100
LARGURA_JOGADOR = 10

def setup():
    global bolaX
    global bolaY
    global velX, velY
    global j1Y, j2Y
    global sobe1, desce1, sobe2, desce2
    j1Y = height/2
    j2Y = height/2
    bolaX, bolaY = 90, 333
    velX, velY = 1, 2
    sobe1, desce1 = False, False
    sobe2, desce2 = False, False
    size(600, 400)

def draw():
    global bolaX, bolaY
    background(0,0,0)
    move_bola()
    desenha_bola()
    move_jogador()
    desenha_jogador()
    
def desenha_jogador():
    global j1Y, j2Y
    fill(255, 255, 255)
    rect(10, j1Y - (ALTURA_JOGADOR/2), LARGURA_JOGADOR, ALTURA_JOGADOR)
    rect(width - 20, j2Y - (ALTURA_JOGADOR/2), LARGURA_JOGADOR, ALTURA_JOGADOR)

def keyPressed():
    global sobe1, desce1
    global sobe2, desce2
    if key == 'w':
        sobe1 = True
    if key == 's':
        desce1 = True
    if key == 'o':
        sobe2 = True
    if key == 'l':
        desce2 = True


def keyReleased():
    global sobe1, desce1
    global sobe2, desce2
    if key == 'w':
        sobe1 = False
    if key == 's':
        desce1 = False
    if key == 'o':
        sobe2 = False
    if key == 'l':
        desce2 = False 

def move_jogador():
    global j1Y, sobe1, desce1
    global j2Y, sobe2, desce2
    if sobe1:
        if j1Y  - (ALTURA_JOGADOR/2) > 0:
            j1Y = j1Y - VEL_JOGADOR
    if desce1:
        if j1Y + (ALTURA_JOGADOR/2) < height:
            j1Y = j1Y + VEL_JOGADOR
    if sobe2:
        if j2Y - (ALTURA_JOGADOR/2) > 0:
            j2Y = j2Y - VEL_JOGADOR
    if desce2:
        if j2Y + (ALTURA_JOGADOR/2) < height:
            j2Y = j2Y + VEL_JOGADOR

def desenha_bola():
    fill (random(255), random(255), random(255))
    ellipse(bolaX, bolaY, TAMANHO_BOLA, TAMANHO_BOLA)

def move_bola():
    global bolaX, bolaY, velX, velY
    bolaX = bolaX + velX
    bolaY = bolaY + velY
    if bolaX < 10 + LARGURA_JOGADOR or bolaX > width-10-LARGURA_JOGADOR:
        if rebate(1) or rebate(2):
            velX = -velX
    if bolaY < 0 or bolaY > height:
        velY = -velY
        
def rebate(numero_jogador):
    if numero_jogador == 1:
        return (bolaX <= 10 + LARGURA_JOGADOR and j1Y - (ALTURA_JOGADOR/2) < bolaY < j1Y + (ALTURA_JOGADOR/2))
    else:
        return (bolaX >= width - 10 - LARGURA_JOGADOR and j2Y - (ALTURA_JOGADOR/2) < bolaY < j2Y + (ALTURA_JOGADOR/2))
