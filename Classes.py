import pygame                               #Import modules
import random
import time
pygame.init()

SUBTILES = 100              #Pixels in Tiles
ALPHA = (255,   0, 255)     #Set Color Preset

class Player(pygame.sprite.Sprite):         #Create Player                         
    def __init__(self):                     #Set Attributes and Functions
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
        self.imageR  = pygame.image.load("robot2.png").convert()        #Preloads all rotated images
        self.imageL  = pygame.transform.flip(self.imageR, True, False)
        self.imageRU = pygame.transform.rotate(self.imageR,  90)
        self.imageLU = pygame.transform.rotate(self.imageL, -90)
        self.imageRD = pygame.transform.rotate(self.imageL,  90)
        self.imageLD = pygame.transform.rotate(self.imageR, -90)
        self.Image   = self.imageR

        self.tunnelpos = [2,0]      #Tilemap position
        self.cachetunnel =[2,0]     #Previous Tilemap position
        self.inventory = 0
        self.rect = self.Image.get_rect()#Finds Dimensions from image for collision
        self.deathtime = None

    def move(self,x,y,diro):        #Move Player Function
            
        if self.queue == 0:         #Move 100 pixels, 1 tile
            self.queue += 24

        if self.pos[y] % SUBTILES == 0:
            self.change[x] = self.speed * diro
                  
    def rotate(self, con1, con2, rota1, rota2, fin1, fin2):#Rotate Player   Conditions and Rotations and Final
        if self.rotatable:              #If it's allowed to rotate
            if self.easy:               #If it's rotating to left or right
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

    def die(self):  #Death function
        if self.deathtime == None:                       #Sets time for death animation       
            self.deathtime = time.time()
        elif self.deathtime + 1 > time.time():
            self.Image = pygame.transform.rotate(self.Image,1)

class Enemy1(pygame.sprite.Sprite):#Create Enemy
    def __init__(self):
        super().__init__()
        self.imagel = pygame.image.load("enemy.png").convert()      
        self.imager = pygame.transform.flip(self.imagel,True,False)
        self.image = self.imager
        self.image.set_colorkey(ALPHA)
        self.rect  = self.image.get_rect()
        self.change = [0,0]
        
        
class Objective(pygame.sprite.Sprite):#Create Objective
    def __init__(self):
        super().__init__()
        self.image  = pygame.image.load("Crystal.png").convert()
        self.image.set_colorkey(ALPHA)
        self.rect   = self.image.get_rect()
        self.coord  = [[0,400],[400,600],[1000,500]]
                

class Obstacle(pygame.sprite.Sprite):#Create Obstacle
    def __init__(self):
        super().__init__()
        self.image  = pygame.image.load("boulder.png").convert()
        self.image.set_colorkey(ALPHA)
        self.coord  = [[1200,300],[1200,400],[1200,500],[1200,600],
                       [0,300],[100,300],[0,500],[500,500],[600,500],[700,500],
                       [900,300],[900,400],[1000,300],[1100,300],[1100,400]]
        self.rect   = self.image.get_rect()
                    
                    
class Tiles():      #Create Tilemap
    def __init__(self):
        Alpha = pygame.image.load("Alpha.png").convert()            #Preload Images
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
        
        self.texture     = {        #Associate each image with these variables
                            0b1111: Alpha,
                            0b0111: Up,  
                            0b1011: Do,     
                            0b1101: Le,         #     Up  Down  Left Right
                            0b1110: Ri,         # 0b   1     1     1     1  
                            0b0011: UD,
                            0b1100: LR,         #    0 = Opened
                            0b0110: UR,         #    1 = Closed
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
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1011,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1110,0b1100,0b1100,0b1101,0b1111,0b1111,0b1111,0b0011,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b0011,0b1111,0b1111,0b1111,0b1111],
                        [0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b1111,0b0111,0b1111,0b1111,0b1111,0b1111],
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
