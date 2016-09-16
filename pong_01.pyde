def setup():
    global game_over
    global bolaX, bolaY, velX, velY
    global sobe_1, desce_1
    global sobe_2, desce_2
    global j1Y, j2Y
    bolaX = width/2
    bolaY = height/2
    velX = 3
    velY = 2
    game_over = False
    noStroke()
    size(600, 400)

def draw():
    background(0)
    if not game_over:
        desenha_bola()
        move_bola()
    else:
        escreve_game_over()
        
def escreve_game_over():
    textSize(60)
    textAlign(CENTER)
    text("EL FIN DEL JUEGO", width/2, height/2)
    
def desenha_bola():
    fill(255, 255, 0)
    ellipse(bolaX, bolaY, 15, 15)
    
def move_bola():
    global bolaX, bolaY, velX, velY, game_over
    bolaX = bolaX + velX
    bolaY = bolaY + velY
    if bolaX < 0 or bolaX > width:
        velX = - velX
    if bolaY < 0 or bolaY > height:
        velY = - velY