def setup():
    global game_over
    global bolaX, bolaY, velX, velY
    global sobe_1, desce_1
    global sobe_2, desce_2
    global j1Y, j2Y
    bolaX = width/2
    bolaY = height/2
    velX = 5
    velY = -4
    j1Y = height/2
    j2Y = height/2
    sobe_1, desce_1 = False, False
    sobe_2, desce_2 = False, False
    game_over = False
    noStroke()
    size(600, 400)

def draw():
    background(0)
    if not game_over:
        desenha_bola()
        move_bola()
        desenha_jogador()
        move_jogador()
    else:
        escreve_game_over()
        
def keyPressed():
    global sobe_1, desce_1
    global sobe_2, desce_2
    if key == 'w': sobe_1 = True
    if key == 's': desce_1 = True
    if key == 'o': sobe_2 = True
    if key == 'l': desce_2 = True
    
def keyReleased():
    global sobe_1, desce_1
    global sobe_2, desce_2
    if key == 'w': sobe_1 = False
    if key == 's': desce_1 = False
    if key == 'o': sobe_2 = False
    if key == 'l': desce_2 = False

def desenha_jogador():
    rect(10, j1Y-50, 10, 80)
    rect(width - 20, j2Y-50, 10, 80)

def move_jogador():
    global sobe_1, desce_1
    global sobe_2, desce_2
    global j1Y, j2Y
        
    if sobe_1:
        if j1Y > 0:
            j1Y = j1Y - 5
    if desce_1:
        if j1Y < height:
            j1Y = j1Y + 5
    if sobe_2:
        if j2Y > 0:
            j2Y = j2Y - 5
    if desce_2:
        if j2Y < height:
            j2Y = j2Y + 5
        
def escreve_game_over():
    textSize(60)
    textAlign(CENTER)
    text("EL FIN DEL JUEGO", width/2, height/2)
    
def desenha_bola():
    fill(random(255), random(255), random(255))
    #fill(255)
    ellipse(bolaX, bolaY, 15, 15)
    
def move_bola():
    global bolaX, bolaY, velX, velY, game_over
    bolaX = bolaX + velX
    bolaY = bolaY + velY
    if bolaX < 0 or bolaX > width:
        velX = - velX
    if bolaY < 0 or bolaY > height:
        velY = - velY