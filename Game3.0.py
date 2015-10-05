import Classes                                    
import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
ALPHA = (255,   0, 255)

FILL  = "I Don't Know!"                                     #My Filler Variable

x = 1

def main():
    """ Main Function of the Game """
    pygame.init()

    size = (1400,700)                                       #Set size of Window
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Crusader Dig")              #Title

    player  = Classes.Player()  #Sets Class Variable
    tunnels = Classes.Tunnels()
        
    background  = pygame.image.load("Level.png").convert()

    font = pygame.font.SysFont('Calibri', 25, True, False)  #Set Function

    done = False                                            #Set While Variable
    clock = pygame.time.Clock()

    while not done:
        """ Main Game Loop """
    
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           #X Exits
                done = True
                
            if event.type == pygame.KEYDOWN:        #Arrows Move
                
                if event.key == pygame.K_LEFT:      
                    player.easy = True
                    player.move(0,1,-1)
                    player.rotatable = True
                    tunnels.num += 1
                    player.rotate(FILL,FILL, "Left",FILL, player.imageL, FILL)

                if event.key == pygame.K_RIGHT:
                    player.easy = True
                    player.move(0,1, 1)
                    player.rotatable = True
                    tunnels.num += 1
                    player.rotate(FILL,FILL, "Right",FILL, player.imageR, FILL)

                if event.key == pygame.K_UP:
                    player.easy = False
                    player.move(1,0,-1)
                    player.rotatable = True
                    tunnels.num += 1
                    player.rotate(["Left","LeftDown"],["Right","RightUp"],"LeftUp","RightUp", player.imageLU, player.imageRU)

                if event.key == pygame.K_DOWN:
                    player.easy = False
                    player.move(1,0, 1)
                    player.rotatable = True
                    tunnels.num += 1
                    player.rotate(["Left","LeftUp"],["Right","RightUp"],"LeftDown","RightDown", player.imageLD, player.imageRD)
                    

        player.pos[0] += player.change[0]
        player.pos[1] += player.change[1]
        if player.pos[1] < 200:
            player.pos[1] = 200
        if player.queue > 0:
            player.queue -= 1
        else:
            player.change = [0,0]

        for i in range(tunnels.num):
            tunnel = Classes.Tunnels()
            if player.pos[1] > 300:
                tunnel.rect.x = player.pos[0]
                tunnel.rect.y = player.pos[1]
            tunnels.list.add(tunnel)

        tunnels.list.draw(screen)
        
        screen.blit(background,[0,0])

        player.Image.set_colorkey(ALPHA)
        screen.blit(player.Image,player.pos)         #Draw Player
        pygame.display.flip()
        clock.tick(60)                                      #Set Framerate
        
    pygame.quit()

if __name__ == "__main__":
    main()





                        
