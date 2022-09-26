#multiplayer on one device or online?
#like Super Smash Bros?
#or incorperate slimes (already downloaded)

#Look at the paper for more info

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

U_score = 0
M_score = 0

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
        self.hitbox = (self.x -1.5, self.y -2, 64, 62)
        self.health = 10
        self.visible = True
        
    def draw(self, window):
        if self.visible:
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
        
                pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0] + 7, self.hitbox[1] -20, 50, 8))  
                pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0] + 7, self.hitbox[1] -20, 50 - (5 * (10 - self.health)), 8))  
                self.hitbox = (self.x -1.5, self.y -2, 64, 62)
                #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False        
        print("Urban is hit!!!")
        pass
        
        
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
        char.hitbox = (char.x -1.5, char.y -2, 64, 62)
        char.health = 10
        char.visible = True        
        
    def draw(char, window):
        if char.visible:
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
                
                pygame.draw.rect(window, (255, 0, 0), (char.hitbox[0] + 7, char.hitbox[1] - 20, 50, 8))  
                pygame.draw.rect(window, (0, 255, 0), (char.hitbox[0] + 7, char.hitbox[1] -20, 50 - (5 * (10 - char.health)), 8))         
                char.hitbox = (char.x -1.5, char.y -2, 64, 62)
                #pygame.draw.rect(window, (255, 0, 0), char.hitbox, 2)
        
    def hit(char):
        if char.health > 0:
            char.health -= 1
        else:
            char.visible = False
        print("Metro is hit!!!")
        pass
                
class arrow(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        #self.radius = radius
        self.facing = facing  
        self.vel = 8 * facing    
        
    def draw(self, window):
        window.blit(U_laser, (self.x, self.y))    
            
class projectile(object):
    def __init__(char, x, y, facing):
        char.x = x
        char.y = y
        #char.radius = radius
        char.facing = facing  
        char.vel = 8 * facing    
        
    def draw(char, window):
        window.blit(M_laser, (char.x, char.y ))
        #window.blit(M_laser, (char.x + 21, char.y + 8))
        
"""
        
def M_timeout():
    shoot.append(projectile(Metro.x + Metro.width //2 - 26, Metro.y + Metro.height //2 - 15, facing))

times = Timer(4, M_timeout)

def M_timers():
    times.start()
    
"""
    
def redraw(window):
    window.blit(bg, (0,0))
    U_text = font.render('Urban: ' + str(U_score), 1, 'aquamarine1')
    M_text = font.render('Metro: ' + str(M_score), 1, 'coral1')
    #text_size = 117, 21
    window.blit(U_text, (748, 16))
    window.blit(M_text, (45, 16))
    Urban.draw(window)
    Metro.draw(window)
    for shot2 in M_shoot:
        shot2.draw(window)
    for shot1 in U_shoot:
        shot1.draw(window)
        #pygame.time.wait(10)
    
    pygame.display.update()    
    

font = pygame.font.SysFont('georgia', 30)
Urban = Team1(836, 210, 64, 64)
Metro = Team2(20, 210, 64, 64)
shot_loop1 = 0
shot_loop2 = 0
U_shoot = []
M_shoot = []
run = True
while run:
    clock.tick(27)
    
    if shot_loop1 > 0:
        shot_loop1 += 1
    if shot_loop1 > 5:
        shot_loop1 = 0
        
    if shot_loop2 > 0:
        shot_loop2 += 1
    if shot_loop2 > 5:
        shot_loop2 = 0    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for shot1 in U_shoot:
        if shot1.y - 2.5 < Metro.hitbox[1] + Metro.hitbox[3] and shot1.y + 2.5> Metro.hitbox[1]:
            if shot1.x + 22.5> Metro.hitbox[0] and shot1.x + 22.5< Metro.hitbox[0] + Metro.hitbox[2]:
                Metro.hit()
                M_score += 1
                U_shoot.pop(U_shoot.index(shot1))
                
        if shot1.x < 912 and shot1.x > 0:
            shot1.x += shot1.vel
        else:
            U_shoot.pop(U_shoot.index(shot1))
            
    for shot2 in M_shoot:
        if shot2.y - 2.5 < Urban.hitbox[1] + Urban.hitbox[3] and shot2.y + 2.5> Urban.hitbox[1]:
            if shot2.x + 22.5> Urban.hitbox[0] and shot2.x + 22.5< Urban.hitbox[0] + Urban.hitbox[2]:
                Urban.hit()
                U_score += 1
                M_shoot.pop(M_shoot.index(shot2))    
                
        """
        if shot.y - radius < Urban.hitbox[1] + Urban.hitbox[3] and shot.y + shot.radius > Urban.hitbox[1]:
            if shot.x + shot.radius > Urban.hitbox[0] and shot.x - shot.radius < Urban.hitbox[0] + Urban.hitbox[2]:
                Urban.hit()
                M_shoot.pop(M_shoot.index(shot))
                
        """
        
        if shot2.x < 912 and shot2.x > 0:
            shot2.x += shot2.vel
        else:
            M_shoot.pop(M_shoot.index(shot2))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_c] and shot_loop2 == 0:
        if Metro.left:
            facing = -1
        else: 
            facing = 1
            
        if len(M_shoot) < 10:
            M_shoot.append(projectile(Metro.x + Metro.width //2 - 26, Metro.y + Metro.height //2 - 15, facing))
            
        shot_loop2 = 1
            
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
        
    if not Metro.isjump:
        if keys[pygame.K_w]:
            Metro.isjump = True
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
    
    
    if keys[pygame.K_PERIOD] and shot_loop1 == 0:
        if Urban.left:
            facing = -1
        else: 
            facing = 1
                    
        if len(U_shoot) < 10:
            U_shoot.append(arrow(Urban.x + Urban.width //2 - 26, Urban.y + Urban.height //2 - 15, facing))
        
        shot_loop1 = 1
        
        pygame.time.wait(100)
                     
    elif keys[pygame.K_RIGHT] and Urban.x < winW - Urban.width - Urban.vel:
        Urban.x += Urban.vel
        Urban.right = True
        Urban.left = False
        Urban.standing = False
        
    elif keys[pygame.K_LEFT] and Urban.x > Urban.vel:
        Urban.x -= Urban.vel
        Urban.left = True
        Urban.right = False
        Urban.standing = False
        
    else:
        Urban.standing = True
        Urban.walkcount = 0
                
    if not Urban.isjump:
        if keys[pygame.K_UP]:
            Urban.isjump = True
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
