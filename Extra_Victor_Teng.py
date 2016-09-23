VELOCIDADE = 10
TAMANHO_BOLA = 20
TAMANHO_JOGADOR = 50

def setup():
    global BOLAX, BOLAY, VELX, VELY
    global posicao_jogador
    global sobe, desce
    BOLAX, BOLAY = 200, 200
    VELX, VELY = 5, 5
    posicao_jogador = 200
    sobe, desce = False, False
    size(600, 400)
    noStroke()
    
def draw():
    background(0)
    desenha_bola()
    move_bola()
    desenha_jogador()
    move_jogador()
    
def desenha_bola():
    global BOLAX, BOLAY, VELX, VELY
    fill(255)
    ellipse(BOLAX, BOLAY, TAMANHO_BOLA, TAMANHO_BOLA)    

def move_bola():
    global BOLAX, BOLAY, VELX, VELY
    if not(BOLAX > 0):
        if rebate():
            VELX = -VELX
        else:
            BOLAX, BOLAY = 200, 200
    if not(BOLAX < width):
        VELX = -VELX
    if not(BOLAY > 0 and BOLAY < height):
        VELY = -VELY
    BOLAX, BOLAY = BOLAX + VELX, BOLAY + VELY
    
def desenha_jogador():
    global posicao_jogador
    fill(255)
    rect(10, posicao_jogador, 10, TAMANHO_JOGADOR)

def move_jogador():
    global sobe, desce
    global posicao_jogador
    if sobe: posicao_jogador = posicao_jogador - VELOCIDADE
    if desce: posicao_jogador = posicao_jogador + VELOCIDADE 
    
def keyPressed():
    global sobe, desce
    if key == 'w':
        sobe = True
    if key == 's':
        desce = True
    
def keyReleased():
    global sobe, desce
    if key == 'w':
        sobe = False
    if key == 's':
        desce = False
    
def rebate():
    global BOLAX, BOLAY, VELX, VELY
    global posicao_jogador
    if BOLAX <= 10 and (posicao_jogador - (TAMANHO_JOGADOR/2) < BOLAY < posicao_jogador + (TAMANHO_JOGADOR/2)):
        return True
    else:
        return False
