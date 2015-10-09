import pygame
import random
pygame.init()

SUBTILES = 100

class Player(pygame.sprite.Sprite):                             
    def __init__(self):
        super().__init__()

        self.rotation = "Right"  
        self.rotatable = False  
        self.life = 1
        self.pos = [200, 200]
        self.change = [0,0]
        self.queue = 0
        self.easy = True        #Rotate to left or right
        self.speed = 4
        self.x = 0
        self.imageR  = pygame.image.load("Robot.png").convert()
        self.imageL  = pygame.transform.flip(self.imageR, True, False)
        self.imageRU = pygame.transform.rotate(self.imageR,  90)
        self.imageLU = pygame.transform.rotate(self.imageL, -90)
        self.imageRD = pygame.transform.rotate(self.imageL,  90)
        self.imageLD = pygame.transform.rotate(self.imageR, -90)
        self.Image   = self.imageR

    def move(self,x,y,diro):
            
        if self.queue == 0:
            self.queue += 24

        if self.pos[y] % SUBTILES == 0:
            self.change[x] = self.speed * diro

        if self.change == [0,0]:
            if not self.pos[x] % SUBTILES == 0:
                self.change[y] = self.speed * diro
            if not self.pos[y] % SUBTILES == 0:
                self.change[x] = self.speed * diro

                  
    def rotate(self, con1, con2, rota1, rota2, fin1, fin2):
        if self.rotatable:      #If its allowed to rotate
            if self.easy:       #If its rotating to left or right
                self.rotation = rota1
            if self.rotation in con1:
                self.rotation = rota1
            if self.rotation in con2:
                self.rotation = rota2

            if self.rotation in rota1:
                self.Image = fin1
            if self.rotation in rota2:
                self.Image = fin2
                
            self.rotatable = False
            

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):

        self.rotation = "Left"
        self.state = 0

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):

        self.rotation = "Left"
        self.state = 0

class Tiles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        Up = pygame.image.load("TunnelU.png").convert()
        Do = pygame.image.load("TunnelD.png").convert()
        Le = pygame.image.load("TunnelL.png").convert()
        Ri = pygame.image.load("TunnelR.png").convert()
        a  = 0
        u  = 1
        d  = 2
        l  = 3
        r  = 4
        
        
        self.texture     = {
                            
                            u : Up,
                            d : Do,
                            l : Le,
                            r : Ri
                            }
        
        self.list  = pygame.sprite.Group()
        self.tilemap = [#1 2 3  4 5 6  7 8 9 101112 13
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#1
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#2
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#3
                        [a,a,[l,r], [l,r],[l,r],[l,r], [l,r],[l,r],[l,r], [l,r],[l,r],[l,r], [l,r],a, a],#4
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#5
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#6
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#7
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#8
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#9
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#10
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#11
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#12
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#13
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#14
                        ]                               
                    

        
