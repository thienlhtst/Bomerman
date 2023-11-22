import pygame
import math

from bomb import Bomb
from enums.power_up_type import PowerUpType
class Player:
    direction = 0
    frame = 0
    animation = []
    range = 3
    bomb_limit = 2
    TILE_SIZE = 4
    def __init__(self,x,y):
        self.life = True
        self.pos_x = x
        self.pos_y = y
    
    def move(self, dx, dy, grid, enemys, power_ups):
        tempx = int(self.pos_x / Player.TILE_SIZE)
        tempy = int(self.pos_y / Player.TILE_SIZE)

        map = [row[:] for row in grid]
        for x in enemys:
            if x == self:
                continue
            elif not x.life:
                continue
            else:
                map[int(x.pos_x / Player.TILE_SIZE)][int(x.pos_y / Player.TILE_SIZE)] = 2
                
        

        if self.pos_x % Player.TILE_SIZE != 0 and dx == 0:
            if self.pos_x % Player.TILE_SIZE == 1:
                self.pos_x -= 1
            elif self.pos_x % Player.TILE_SIZE == 3:
                self.pos_x += 1
            return
        if self.pos_y % Player.TILE_SIZE != 0 and dy == 0:
            if self.pos_y % Player.TILE_SIZE == 1:
                self.pos_y -= 1
            elif self.pos_y % Player.TILE_SIZE == 3:
                self.pos_y += 1
            return

        # right
        if dx == 1:
            if map[tempx+1][tempy] == 0:
                self.pos_x += 1
        # left
        elif dx == -1:
            tempx = math.ceil(self.pos_x / Player.TILE_SIZE)
            if map[tempx-1][tempy] == 0:
                self.pos_x -= 1

        # bottom
        if dy == 1:
            if map[tempx][tempy+1] == 0:
                self.pos_y += 1
        # top
        elif dy == -1:
            tempy = math.ceil(self.pos_y / Player.TILE_SIZE)
            if map[tempx][tempy-1] == 0:
                self.pos_y -= 1

        for pu in power_ups:
            if pu.pos_x == math.ceil(self.pos_x / Player.TILE_SIZE) \
                    and pu.pos_y == math.ceil(self.pos_y / Player.TILE_SIZE):
                self.consume_power_up(pu, power_ups)

    def plant_bomb(self, map):
        b = Bomb(self.range, round(self.pos_x / Player.TILE_SIZE), round(self.pos_y / Player.TILE_SIZE), map, self)
        return b

    def check_death(self, exp):
        for e in exp:
            for s in e.sectors:
                if int(self.pos_x / Player.TILE_SIZE) == s[0] and int(self.pos_y / Player.TILE_SIZE) == s[1]:
                    self.life = False

    def consume_power_up(self, power_up, power_ups):
        if power_up.type == PowerUpType.BOMB:
            self.bomb_limit += 1
        elif power_up.type == PowerUpType.FIRE:
            self.range += 1

        power_ups.remove(power_up)

    def load_animations(self, scale,image,hero):
        front = []
        back = []
        left = []
        right = []
        resize_width = scale
        resize_height = scale

        f1 = pygame.image.load('images/'+image+'/'+hero+'f0.png')
        f2 = pygame.image.load('images/'+image+'/'+hero+'f1.png')
        f3 = pygame.image.load('images/'+image+'/'+hero+'f2.png')
        f4 = pygame.image.load('images/'+image+'/'+hero+'f3.png')
        f5 = pygame.image.load('images/'+image+'/'+hero+'f4.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))
        f4 = pygame.transform.scale(f4, (resize_width, resize_height))
        f5 = pygame.transform.scale(f5, (resize_width, resize_height))

        front.append(f1)
        front.append(f2)
        front.append(f3)
        front.append(f4)
        front.append(f5)

        r1 = pygame.image.load('images/'+image+'/'+hero+'r0.png')
        r2 = pygame.image.load('images/'+image+'/'+hero+'r1.png')
        r3 = pygame.image.load('images/'+image+'/'+hero+'r2.png')
        r4 = pygame.image.load('images/'+image+'/'+hero+'r3.png')
        r5 = pygame.image.load('images/'+image+'/'+hero+'r4.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))
        r4 = pygame.transform.scale(r4, (resize_width, resize_height))
        r5 = pygame.transform.scale(r5, (resize_width, resize_height))

        right.append(r1)
        right.append(r2)
        right.append(r3)
        right.append(r4)
        right.append(r5)

        b1 = pygame.image.load('images/'+image+'/'+hero+'b0.png')
        b2 = pygame.image.load('images/'+image+'/'+hero+'b1.png')
        b3 = pygame.image.load('images/'+image+'/'+hero+'b2.png')
        b4 = pygame.image.load('images/'+image+'/'+hero+'b3.png')
        b5 = pygame.image.load('images/'+image+'/'+hero+'b4.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))
        b4 = pygame.transform.scale(b4, (resize_width, resize_height))
        b5 = pygame.transform.scale(b5, (resize_width, resize_height))

        back.append(b1)
        back.append(b2)
        back.append(b3)
        back.append(b4)
        back.append(b5)

        l1 = pygame.image.load('images/'+image+'/'+hero+'l0.png')
        l2 = pygame.image.load('images/'+image+'/'+hero+'l1.png')
        l3 = pygame.image.load('images/'+image+'/'+hero+'l2.png')
        l4 = pygame.image.load('images/'+image+'/'+hero+'l3.png')
        l5 = pygame.image.load('images/'+image+'/'+hero+'l4.png')

        l1 = pygame.transform.scale(l1, (resize_width, resize_height))
        l2 = pygame.transform.scale(l2, (resize_width, resize_height))
        l3 = pygame.transform.scale(l3, (resize_width, resize_height))
        l4 = pygame.transform.scale(l4, (resize_width, resize_height))
        l5 = pygame.transform.scale(l5, (resize_width, resize_height))

        left.append(l1)
        left.append(l2)
        left.append(l3)
        left.append(l4)
        left.append(l5)

        
        self.animation.append(front)
        self.animation.append(right)
        self.animation.append(back)
        self.animation.append(left)
