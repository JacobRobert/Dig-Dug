import Classes                                    
import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
ALPHA = (255,   0, 255)

FILL  = "I Don't Know!"                                     #My Filler Variable

def main():
    """ Main Function of the Game """
    pygame.init()

    size = (1300,700)                                       #Set size of Window
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Crusader Dig")              #Title

    player  = Classes.Player()  #Sets Class Variable
    tunnels = Classes.Tiles()
        
    background = pygame.image.load("Level.png").convert()
    explosion  = pygame.image.load("Explosion.png").convert()
    explosion.set_colorkey(ALPHA)
    
    font = pygame.font.SysFont('Calibri', 120, True, False)  #Set Function

    done = False                                            #Set While Variable
    clock = pygame.time.Clock()
    
    obdiro = 0b1111
    indiro = 0b1111

    objlist = pygame.sprite.Group()
    obslist = pygame.sprite.Group()
    enemylist = pygame.sprite.Group()
    deathlist = pygame.sprite.Group()
    projectilelist = pygame.sprite.Group()

    for obj in range(3):
        objective = Classes.Objective()
        objective.rect.x = objective.coord[obj][0]
        objective.rect.y = objective.coord[obj][1]
        objlist.add(objective)
            
    for obs in range(15):
        obstacle = Classes.Obstacle()
        obstacle.rect.x = obstacle.coord[obs][0]
        obstacle.rect.y = obstacle.coord[obs][1]
        obslist.add(obstacle)

    for ene in range(2):
        enecoord = [[400,400],[800,500]]
        enemy = Classes.Enemy1()
        enemy.rect.x = enecoord[ene][0]
        enemy.rect.y = enecoord[ene][1]
        enemylist.add(enemy)
        deathlist.add(enemy)


    while not done:
        """ Main Game Loop """
    
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           #X Exits
                main()
                
            if event.type == pygame.KEYDOWN:        #Arrows Move
                if event.key == pygame.K_ESCAPE:
                    main()
                
                if event.key == pygame.K_LEFT:      
                    player.easy = True
                    if player.change == [0,0]:
                        player.move(0,1,-1,obstacle)
                    player.rotatable = True
                    obdiro = 0b1110
                    indiro = 0b1101
                    player.rotate(FILL,FILL, "Left",FILL, player.imageL, FILL)

                if event.key == pygame.K_RIGHT:
                    player.easy = True
                    if player.change == [0,0]:
                        player.move(0,1, 1,obstacle)
                    player.rotatable = True
                    obdiro = 0b1101
                    indiro = 0b1110
                    player.rotate(FILL,FILL, "Right",FILL, player.imageR, FILL)

                if event.key == pygame.K_UP:
                    player.easy = False
                    if player.change == [0,0]:
                        player.move(1,0,-1,obstacle)
                    player.rotatable = True
                    backgroundcoord = 1
                    obdiro = 0b1011
                    indiro = 0b0111
                    player.rotate(["Left","LeftDown"],["Right","RightDown"],"LeftUp","RightUp", player.imageLU, player.imageRU)

                if event.key == pygame.K_DOWN:
                    player.easy = False
                    if player.change == [0,0]:
                        player.move(1,0, 1,obstacle)
                    player.rotatable = True
                    obdiro = 0b0111
                    indiro = 0b1011
                    player.rotate(["Right","LeftUp"],["Left","RightUp"],"LeftDown","RightDown", player.imageLD, player.imageRD)

        if player.change[0] > 0 or player.change[0] < 0:
            player.change[1] 
        if player.change[1] > 0 or player.change[1] < 0:
            player.change[0] 
        
        for obstacle in obslist:
            if player.rect.colliderect(obstacle.rect):
                player.pos[0] -= player.change[0]
                player.pos[1] -= player.change[1]

                player.change[:] = [0, 0]

        player.pos[0] += player.change[0]
        player.pos[1] += player.change[1]
        if player.pos[1] < 200:
            player.pos[1] = 200
        if player.pos[1] > 600:
            player.pos[1] = 600
        if player.pos[0] < 0:
            player.pos[0] = 0
        if player.pos[0] > 1200:
            player.pos[0] = 1200
        if player.queue > 0:
            player.queue -= 1
        else:
            player.change = [0,0]
            
        player.rect.x = player.pos[0]
        player.rect.y = player.pos[1]

        prolist = pygame.sprite.Group()

        if player.change == [0,0]:
            player.tunnelpos[0] = player.pos[0]//100
            player.tunnelpos[1] = player.pos[1]//100 -2
            if not player.tunnelpos[1] == 0:
                tunnels.addtunnel(player.tunnelpos[0], player.tunnelpos[1],obdiro)
        else:
            if not player.cachetunnel[1] == 0:
                tunnels.addtunnel(player.cachetunnel[0],player.cachetunnel[1],indiro)
            player.cachetunnel = player.tunnelpos

        if player.change == [0,0]:
            objcollide = pygame.sprite.spritecollide(player,objlist,True)    

        for objective in objcollide:
            player.inventory +=1

                        
        backgroundcoord = [0,0]
        screen.blit(background,backgroundcoord)    

        for enemy in enemylist:
            if enemy.change == [0, 0]:
                enemy.change[:] = random.choice([(-1, 0), (1, 0), (0, 1), (0, -1)])
            if (enemy.rect.y + enemy.rect.x) % 100 == 0:
                x = enemy.rect.x // 100
                y = enemy.rect.y // 100 - 2
                tile = tunnels.tilemap[y][x]
                if random.random() > 0.66:
                    enemy.change[:] = [0, 0]
                elif y == 0:
                    enemy.change[:] = [0, 1]
                elif tile & 0b1000 and enemy.change[1] == -1:
                    enemy.change[1] = 0
                elif tile & 0b0100 and enemy.change[1] == 1:
                    enemy.change[1] = 0
                elif tile & 0b0010 and enemy.change[0] == -1:
                    enemy.change[0] = 0
                elif tile & 0b0001 and enemy.change[0] == 1:
                    enemy.change[0] = 0
 
            x, y = enemy.change
            if enemy.rect.y + y >= 600 or enemy.rect.y + y <= 0 or enemy.rect.x + x >= 1200 or enemy.rect.x + x <= 0:
                enemy.change[:] = [0, 0]
            else:
                enemy.rect.y += y
                enemy.rect.x += x
                
            if enemy.change[0] == 1:
                enemy.image = enemy.imager
            if enemy.change[0] == -1:
                enemy.image = enemy.imagel
            enemy.image.set_colorkey(ALPHA)

       
        for row in range(13):
            for column in range(12):
                screen.blit(tunnels.texture[tunnels.tilemap[row][column]],(column*100,row*100+200))

        objlist.draw(screen)
        obslist.draw(screen)
        enemylist.draw(screen)
        

        player.Image.set_colorkey(ALPHA)
        screen.blit(player.Image,player.pos)        #Draw Player

        deathcollide = pygame.sprite.spritecollide(player,deathlist,False)
        for death in deathcollide:
            player.life = 0
            deathtime = 30
            if deathtime > 0:
                player.die()
                screen.blit(explosion,player.pos)
                deathtime -= 1
                
                gameover = font.render("GAME OVER", True, WHITE)
                screen.blit(gameover, [300,300])    
            else:
                done = True

        if player.inventory == 3:
            if player.life == 1:
                youwin   = font.render("You Win!", True, WHITE)
                screen.blit(youwin, [300,300])
        
        pygame.display.flip()
        clock.tick(60)                                      #Set Framerate

    for reset in pygame.event.get():
        main()

if __name__ == "__main__":
    main()





                
