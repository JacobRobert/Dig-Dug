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
        
      #  ob0111= 7
     #   ob1011= 11
    #    ob1101= 13
   #     ob1110= 14 
  #      ob0011= 3
 #       ob1100= 12
#        ob0110= 6
        #ob0101= 5
       # ob1010= 10
      #  ob1001= 9
     #   ob0010= 2  
    #    ob1000= 8
   #     ob0001= 1 
  #      ob0100= 4 
 #       ob0000= 0
#        ob1111= 15  #Up  Down  Left  Right
        
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
        self.tilemap[y[x]] &= direction
