#multiplayer on one device or online?
#like Super Smash Bros?
#or incorperate slimes (already downloaded)

#Look at the paper for more info

from threading import Timer
from threading import Thread
import time
import pygame
pygame.init()

winW = 912
winH = 285

window = pygame.display.set_mode((winW,winH))
pygame.display.set_caption("City Ghost")

bg = pygame.image.load('Untitled.png').convert()
U_walkright = pygame.image.load('pop.png').convert_alpha()
U_walkleft = pygame.image.load('lkl.png').convert_alpha()
U_laser = pygame.image.load('U_laser.png').convert_alpha()
M_walkright = pygame.image.load('M_walkright.png').convert_alpha()
M_walkleft = pygame.image.load('M_walkleft.png').convert_alpha()
M_laser = pygame.image.load('M_laser.png').convert_alpha()

clock = pygame.time.Clock()

class Team1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjump = False
        self.jumpcount = 10
        self.left = True
        self.right = False
        self.walkcount = 0
        self.standing = True
        
    def draw(self, window):
        if self.walkcount + 1 >= 9:
            self.walkcount = 0  
            
        if not (self.standing):
            if self.right:
                window.blit(U_walkright, (self.x, self.y))
                self.walkcount += 1
            else:
                window.blit(U_walkleft, (self.x, self.y))
                self.walkcount += 1
        else:
            if self.right:
                window.blit(U_walkright, (self.x, self.y))
            else:
                window.blit(U_walkleft, (self.x, self.y))
        
        
class Team2(object):
    def __init__(char, x, y, width, height):
        char.x = x
        char.y = y
        char.width = width
        char.height = height
        char.vel = 5
        char.isjump = False
        char.jumpcount = 10
        char.left = False
        char.right = True
        char.walkcount = 0
        char.standing = True
        
    def draw(char, window):
        if char.walkcount + 1 >= 9:
            char.walkcount = 0        
            
        if not (char.standing):
            if char.left:
                window.blit(M_walkleft, (char.x, char.y))
                char.walkcount += 1
            else:
                window.blit(M_walkright, (char.x, char.y))
                char.walkcount += 1
        else:
            if char.right:
                window.blit(M_walkright, (char.x, char.y))
            else:
                window.blit(M_walkleft, (char.x, char.y))            
            
class projectile(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing  
        self.vel = 8 * facing
        
    def __init__(char, x, y, facing):
        char.x = x
        char.y = y
        char.facing = facing  
        char.vel = 8 * facing    
        
    def draw(self, window):
        window.blit(U_laser, (self.x, self.y))
        
    def draw(char, window):
        window.blit(M_laser, (char.x, char.y))
        
"""
        
def M_timeout():
    shoot.append(projectile(Metro.x + Metro.width //2 - 26, Metro.y + Metro.height //2 - 15, facing))

times = Timer(4, M_timeout)

def M_timers():
    times.start()
    
"""
    
def redraw(window):
    window.blit(bg, (0,0))
    Urban.draw(window)
    Metro.draw(window)
    for shot in M_shoot:
        shot.draw(window)
    for shot in U_shoot:
        shot.draw(window)
        #pygame.time.wait(10)
    
    pygame.display.update()    
    

Urban = Team1(836, 210, 64, 64)
Metro = Team2(20, 210, 64, 64)
U_shoot = []
M_shoot = []
run = True
while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for shot in U_shoot:
        if shot.x < 912 and shot.x > 0:
            shot.x += shot.vel
        else:
            U_shoot.pop(U_shoot.index(shot))
            
    for shot in M_shoot:
        if shot.x < 912 and shot.x > 0:
            shot.x += shot.vel
        else:
            M_shoot.pop(M_shoot.index(shot))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_c]:
        if Metro.left:
            facing = -1
        else: 
            facing = 1
            
        if len(M_shoot) < 10:
            M_shoot.append(projectile(Metro.x + Metro.width //2 - 26, Metro.y + Metro.height //2 - 15, facing))
            
            pygame.time.wait(100)
                   
        """
        a = len(shoot)
        thread'a' = Thread(target = M_timers)
        thread+len(shoot).start()
        thread+len(shoot).join()
        thread+len(shoot) = Thread(target=M_timers)
        """
        
        #time.sleep(1)
                     
    elif keys[pygame.K_a] and Metro.x > Metro.vel:
        Metro.x -= Metro.vel
        Metro.left = True
        Metro.right = False
        Metro.standing = False
    
    elif keys[pygame.K_d] and Metro.x < winW - Metro.width - Metro.vel:
        Metro.x += Metro.vel
        Metro.right = True
        Metro.left = False
        Metro.standing = False
    else:
        Metro.standing = True
        Metro.walkcount = 0
        
    if not (Metro.isjump):
        if keys[pygame.K_w]:
            Metro.isjump = True
            Metro.right = False
            Metro.left = False
            Metro.walkcount = 0        
    else:
        if Metro.jumpcount >= -10:
            neg = 1
            if Metro.jumpcount < 0:
                neg = -1
            Metro.y -= (Metro.jumpcount ** 2) //3 * neg
            Metro.jumpcount -= 1
        else:
            Metro.isjump = False
            Metro.jumpcount = 10
    
    if keys[pygame.K_PERIOD]:
        if Urban.left:
            facing = -1
        else: 
            facing = 1
            
        if len(U_shoot) < 10:
            U_shoot.append(projectile(Urban.x + Urban.width //2 - 26, Urban.y + Urban.height //2 - 15, facing))
        
        pygame.time.wait(10)
                             
    elif keys[pygame.K_LEFT] and Urban.x > Urban.vel:
        Urban.x -= Urban.vel
        Urban.left = True
        Urban.right = False
        Urban.standing = False
            
    elif keys[pygame.K_RIGHT] and Urban.x < winW - Urban.width - Urban.vel:
        Urban.x += Urban.vel
        Urban.right = True
        Urban.left = False
        Urban.standing = False
    else:
        Urban.standing = True
        Urban.walkcount = 0
                
    if not (Urban.isjump):
        if keys[pygame.K_UP]:
            Urban.isjump = True
            Urban.right = False
            Urban.left = False
            Urban.walkcount = 0        
    else:
        if Urban.jumpcount >= -10:
            neg = 1
            if Urban.jumpcount < 0:
                neg = -1
            Urban.y -= (Urban.jumpcount ** 2) //3 * neg
            Urban.jumpcount -= 1
        else:
            Urban.isjump = False
            Urban.jumpcount = 10    
            
    redraw(window)
    
pygame.quit()

