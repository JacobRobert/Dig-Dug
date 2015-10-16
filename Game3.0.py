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
        
    background  = pygame.image.load("Level.png").convert()

    font = pygame.font.SysFont('Calibri', 25, True, False)  #Set Function

    done = False                                            #Set While Variable
    clock = pygame.time.Clock()
    
    obdiro = 0b1111

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
                    obdiro = 0b1110
                    player.rotate(FILL,FILL, "Left",FILL, player.imageL, FILL)

                if event.key == pygame.K_RIGHT:
                    player.easy = True
                    player.move(0,1, 1)
                    player.rotatable = True
                    obdiro = 0b1101
                    player.rotate(FILL,FILL, "Right",FILL, player.imageR, FILL)

                if event.key == pygame.K_UP:
                    player.easy = False
                    player.move(1,0,-1)
                    player.rotatable = True
                    backgroundcoord = 1
                    obdiro = 0b1011
                    player.rotate(["Left","LeftDown"],["Right","RightDown"],"LeftUp","RightUp", player.imageLU, player.imageRU)

                if event.key == pygame.K_DOWN:
                    player.easy = False
                    player.move(1,0, 1)
                    player.rotatable = True
                    obdiro = 0b0111
                    player.rotate(["Right","LeftUp"],["Left","RightUp"],"LeftDown","RightDown", player.imageLD, player.imageRD)
                    

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

        if player.change == [0,0]:
            player.tunnelpos[0] = player.pos[0]//100
            player.tunnelpos[1] = player.pos[1]//100 -2
            tunnels.addtunnel(player.tunnelpos[0], player.tunnelpos[1],obdiro)

        backgroundcoord = [0,0]
        screen.blit(background,backgroundcoord)
        
        for row in range(13):
            for column in range(12):
                screen.blit(tunnels.texture[tunnels.tilemap[row][column]],(column*100,row*100+200))

        player.Image.set_colorkey(ALPHA)
        screen.blit(player.Image,player.pos)         #Draw Player
        pygame.display.flip()
        clock.tick(60)                                      #Set Framerate
        
    pygame.quit()

if __name__ == "__main__":
    main()





                
