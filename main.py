import pygame,random,math

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("ufo.png"))

backgroundImg = pygame.image.load("background.jpg")

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
    
enemy_num = 5
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for enemy in range(enemy_num):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(10,150))
    enemyX_change.append(0.4)
    enemyY_change.append(40)
    

bulletImg = pygame.image.load("bullet.png")
bulletX = playerX+16
bulletY = playerY+10
bulletY_change = 0
bullet_state="ready"

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 5
scoreY = 5

def show_score(x,y):
    screen.blit(font.render("Score : " + str(score), True, (255,255,255)),(x,y))

game_over_condition = False
def game_over():
    font = pygame.font.Font("freesansbold.ttf", 64)
    screen.blit(font.render("GAME OVER", True, (255,255,255)),(200,150))
    
def collision(enemyX,enemyY,bulletX,bulletY):
    dist = math.sqrt(((enemyX-bulletX)**2)+((enemyY-bulletY)**2))
    return dist<35

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
            if event.key == pygame.K_SPACE:
                bullet_state = "Not Ready"
                bulletY_change = 1
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
    playerX += playerX_change   
    
    if playerX < 0:
        playerX = 0 
    elif playerX > 736:
        playerX = 736
    
    if bullet_state == "ready":
        bulletX = playerX+16
        
    bulletY -= bulletY_change
    
    if bulletY < 0:
        bulletY = playerY+10
        bullet_state = "ready"
        bulletY_change = 0
    
    for enemy in range(enemy_num):    
        enemyX[enemy] += enemyX_change[enemy]   
        
        if enemyX[enemy] < 0:
            enemyX[enemy] = 0 
            enemyX_change[enemy] = 0.4
            enemyY[enemy] += enemyY_change[enemy]
        elif enemyX[enemy] > 736: 
            enemyX[enemy] = 736
            enemyX_change[enemy] = -0.4
            enemyY[enemy] += enemyY_change[enemy]
         
        if enemyY[enemy] > 440:
            
            for i in range(enemy_num):
                enemyY[i] = 2000
            
            game_over_condition = True
            break     
                        
        if collision(enemyX[enemy], enemyY[enemy], bulletX, bulletY):
            bulletY = playerY+10
            bullet_state = "ready"
            bulletY_change = 0
            enemyX[enemy] = random.randint(0,800)
            enemyY[enemy] = random.randint(10,150)
            score += 1
        
    screen.fill((0,0,0))
    screen.blit(backgroundImg,(-130,-130))
    screen.blit(bulletImg,(bulletX,bulletY))
    screen.blit(playerImg,(playerX,playerY))
    show_score(scoreX, scoreY)
    
    for enemy in range(enemy_num):
        screen.blit(enemyImg[enemy],(enemyX[enemy],enemyY[enemy]))
    
    if game_over_condition:
        game_over()
        
    pygame.display.update()