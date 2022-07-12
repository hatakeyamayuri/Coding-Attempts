#multiplayer on one device or online?
#like Super Smash Bros?
#or incorperate slimes (already downloaded)

#Look at the paper for more info

import pygame
pygame.init()

winW = 912
winH = 285

window = pygame.display.set_mode((winW,winH))
pygame.display.set_caption("City Ghost")

bg = pygame.image.load('Untitled.png').convert()
walkright = pygame.image.load('pop.png').convert_alpha()
walkleft = pygame.image.load('lkl.png').convert_alpha()
laser = pygame.image.load('laser.png').convert_alpha()

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        
    def draw(self, window):
        if self.walkcount + 1 >= 9:
            self.walkcount = 0
            
        if not (self.standing):
            if self.left:
                window.blit(walkleft, (self.x, self.y))
                self.walkcount += 1
            elif self.right:
                window.blit(walkright, (self.x, self.y))
                self.walkcount += 1
        else:
            if self.right:
                window.blit(walkright, (self.x, self.y))
            else:
                window.blit(walkleft, (self.x, self.y))
            
class projectile(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing  
        self.vel = 8 * facing
        
    def draw(self, window):
        window.blit(laser, (self.x, self.y))

def redraw(window):
    window.blit(bg, (0,0))
    Urban.draw(window)
    for shot in shoot:
        shot.draw(window)
        #pygame.time.wait(10)
    
    pygame.display.update()    
    

Urban = player(20, 210, 64, 64)
shoot = []
run = True
while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for shot in shoot:
        if shot.x < 912 and shot.x > 0:
            shot.x += shot.vel
        else:
            shoot.pop(shoot.index(shot))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_PERIOD]:
        if Urban.left:
            facing = -1
        else: 
            facing = 1
        if len(shoot) < 10:
            shoot.append(projectile(Urban.x + Urban.width //2 - 26, Urban.y + Urban.height //2 - 15, facing))
                     
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

