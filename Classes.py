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

        self.tunnelpos    = [2,0]

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

            

class Tiles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        Alpha = pygame.image.load("Alpha.png").convert()            #Load Images
        Alpha.set_colorkey((255,255,255))
        Up = pygame.image.load("TunnelU.png").convert()
        Do = pygame.image.load("TunnelD.png").convert()
        Le = pygame.image.load("TunnelL.png").convert()
        Ri = pygame.image.load("TunnelR.png").convert()
        UD = pygame.image.load("TunnelStraight.png").convert()
        LR = pygame.transform.rotate(UD, 90)
        UR = pygame.image.load("TunnelRight.png").convert()
        UL = pygame.transform.flip(UR, True, False)
        DL = pygame.transform.rotate(UR, 180)
        DR = pygame.transform.flip(DL, True, False)
        TR = pygame.image.load("Tunnel3.png").convert()
        TD = pygame.transform.rotate(TR, -90)
        TL = pygame.transform.rotate(TR, 180)
        TU = pygame.transform.rotate(TR,  90)
        AL = pygame.image.load("TunnelAll.png").convert()
        
        a  = 0
        u  = 1
        d  = 2
        l  = 3
        r  = 4
        ud = 5
        lr = 6
        ur = 7
        ul = 8
        dr = 9
        dl = 10
        tr = 11
        td = 12
        tl = 13
        tu = 14
        al = 15
        
        self.texture     = {
                            a : Alpha,  #a = None
                            u : Up,     #u = Up
                            d : Do,     #d = Down
                            l : Le,     #l = Left
                            r : Ri,     #r = Right
                            ud: UD,
                            lr: LR,
                            ur: UR,
                            ul: UL,
                            dr: DR,
                            dl: DL,
                            tr: TR,     #Up Right Down
                            td: TD,     #Left Down Right
                            tl: TL,     #Up Left Down
                            tu: TU,     #Left Up Right
                            al: AL      #Left Right Up Down
                            }
        
        self.list  = pygame.sprite.Group()
        self.tilemap = [#1 2 3  4 5 6  7 8 9 101112 13
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#1
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#2
                        [a,a,r, lr,lr,lr, lr,lr,lr, lr,l,a, a],#3
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#4
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#5
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#6
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#7
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#8
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#9
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#10
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#11
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#12
                        [a,a,a, a,a,a, a,a,a, a,a,a, a],#13
                        ]

        def addtunnel(self, x, y, final):
            if self.tilemap[y[x]] == a :
            if self.tilemap[y[x]] == u :
            if self.tilemap[y[x]] == d :
            if self.tilemap[y[x]] == l :
            if self.tilemap[y[x]] == r :
            if self.tilemap[y[x]] == ud:
            if self.tilemap[y[x]] == lr:
            if self.tilemap[y[x]] == ur:
            if self.tilemap[y[x]] == ul:
            if self.tilemap[y[x]] == dr:
            if self.tilemap[y[x]] == dl:
            if self.tilemap[y[x]] == tr:
            if self.tilemap[y[x]] == td:
            if self.tilemap[y[x]] == tl:
            if self.tilemap[y[x]] == tu:
            if self.tilemap[y[x]] == 
            
            
            
            
            
                    

        
