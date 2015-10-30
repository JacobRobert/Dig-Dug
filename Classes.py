import pygame
import random
pygame.init()

SUBTILES = 100
ALPHA = (255,   0, 255)

class Player(pygame.sprite.Sprite):                             
    def __init__(self):
        super().__init__()
        self.rotation = "Right"  
        self.rotatable = False  
        self.life = 10
        self.pos = [200, 200]
        self.change = [0,0]
        self.queue = 0
        self.easy = True        #Rotate to left or right
        self.speed = 4
        self.x = 0
        self.imageR  = pygame.image.load("robot2.png").convert()
        self.imageL  = pygame.transform.flip(self.imageR, True, False)
        self.imageRU = pygame.transform.rotate(self.imageR,  90)
        self.imageLU = pygame.transform.rotate(self.imageL, -90)
        self.imageRD = pygame.transform.rotate(self.imageL,  90)
        self.imageLD = pygame.transform.rotate(self.imageR, -90)
        self.Image   = self.imageR

        self.tunnelpos = [2,0]
        self.cachetunnel =[2,0]
        self.inventory = 0
        self.rect = self.Image.get_rect()

    def move(self,x,y,diro,obstacle):
            
        if self.queue == 0:
            self.queue += 24

        if self.pos[y] % SUBTILES == 0:
            self.change[x] = self.speed * diro
                  
    def rotate(self, con1, con2, rota1, rota2, fin1, fin2):
        if self.rotatable:      #If it's allowed to rotate
            if self.easy:       #If it's rotating to left or right
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

    def die(self):
        self.Image = pygame.transform.rotate(self.Image,1)

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagel = pygame.image.load("enemy.png").convert()
        self.imager = pygame.transform.flip(self.imagel,True,False)
        self.image = self.imager
        self.image.set_colorkey(ALPHA)
        self.rect  = self.image.get_rect()
        self.tunne = [3,4]
        self.diro  = -1
        self.delay = 0
        
    def update(self):
        if self.delay == 120:
            if self.diro == -1:
                self.diro = 1
                self.image = self.imager
                self.image.set_colorkey(ALPHA)
            if self.diro == 1:
                self.diro = -1
                self.image = self.imagel
                self.image.set_colorkey(ALPHA)

            self.delay = 0
        else:
            self.delay += 1


class projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagera = pygame.image.load("water1.png").convert()
        self.imagerb = pygame.image.load("water2.png").convert()
        self.imagerc = pygame.image.load("water3.png").convert()
        self.imagela = pygame.transform.flip(self.imagera,True,False)
        self.imagelb = pygame.transform.flip(self.imagerb,True,False)
        self.imagelc = pygame.transform.flip(self.imagerc,True,False)
        
        self.image   = self.imagera
        self.rect    = self.image.get_rect()
        
    def update(self,enemycoord,enemydiro):
        self.rect.x = enemycoord[0] + 100 * enemydiro
        self.rect.y = enemycoord[1]
        delay = 0
        self.image.set_colorkey(ALPHA)
        if enemydiro == 1:#right
            self.image = self.imagera
        if enemydiro == -1:#left
            self.image = self.imagela
        if delay < 5:
            delay += 1
            self.rect.x += 1 * enemydiro
        if delay > 4 and delay < 9:
            delay += 1
            self.rect.x += 1 * enemydiro
            if self.image == self.imagera:
                self.image = self.imagerb
            if self.image == self.imagela:
                self.image = self.imagelb
        if delay > 8 and delay < 13:
            delay += 1
            self.rect.x += 1 * enemydiro
            if self.image == self.imagerb:
                self.image = self.imagerc
            if self.image == self.imagelb:
                self.image = self.imagelc
        else:
            pygame.sprite.kill
            
            

class Objective(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image  = pygame.image.load("Crystal.png").convert()
        self.image.set_colorkey(ALPHA)
        self.rect   = self.image.get_rect()
        self.coord  = [[100,400],[300,600],[700,600]]
        self.number = 3
        

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image  = pygame.image.load("boulder.png").convert()
        self.image.set_colorkey(ALPHA)
        self.coord  = [[200,400],[400,600],[400,300]]
        self.rect   = self.image.get_rect()
        self.number = 3
            
                    
class Tiles():
    def __init__(self):
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
        
        self.texture     = {
                            0b1111: Alpha,  #Up  Down  Left  Right
                            0b0111: Up,  
                            0b1011: Do,     
                            0b1101: Le, 
                            0b1110: Ri,     
                            0b0011: UD,
                            0b1100: LR,
                            0b0110: UR,
                            0b0101: UL,
                            0b1010: DR,
                            0b1001: DL,
                            0b0010: TR,     
                            0b1000: TD,     
                            0b0001: TL,     
                            0b0100: TU,     
                            0b0000: AL  
                            }
        
        self.list  = pygame.sprite.Group()
        self.tilemap = [#1      2      3      4      5      6      7      8      9      10     11     12     13
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],#1
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1110,0b1100,0b1100,0b1100,0b1100,0b1100,0b1100,0b1100,0b1101,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111],
                        ]

    def addtunnel(self, x, y, direction):
        self.tilemap[y][x] &= direction
