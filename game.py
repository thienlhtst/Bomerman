import pygame
import sys
import random
import tkinter as tk

from tkinter import messagebox
from enums.power_up_type import PowerUpType
from player import Player
from explosion import Explosion
from enemy import Enemy
from enums.algorithm import Algorithm
from enums.map import Map
from Map import CreateMap
from power_up import PowerUp
BACKGROUND_COLOR = (107, 142, 35)
font = None
player = None
player1 = None
backgroundmusic = None
enemy_list = []
ene_blocks = []
bombs = []
explosions = []
power_ups = []
checkplayer = None
Pick = None
def game_init(PickMap,surface, path, player_alg, player_alg1, en2_alg, en3_alg, scale):
    global checkplayer
    checkplayer = player_alg1
    global font
    font = pygame.font.SysFont('Bebas', scale)
    global Pick
    Pick = PickMap
    global enemy_list
    global ene_blocks
    global player
    global player1
    global backgroundmusic
    enemy_list = []
    ene_blocks = []
    global explosions
    global bombs
    global power_ups
    bombs.clear()
    explosions.clear()
    power_ups.clear()
    player1 = Player(13*4,13*4)
    player = Player(4,4)
    
    
    if(Pick.ChooseMap is Map.Map1):
        backgroundmusic=pygame.mixer.Sound('music/nongtrai.wav')
        grid = Pick.GRID_BASE_MapGrass
    if(Pick.ChooseMap is Map.Map2):
        backgroundmusic=pygame.mixer.Sound('music/nongtrai.wav')
        grid = Pick.GRID_BASE_MapGrass1
    if(Pick.ChooseMap is Map.Map3):
        backgroundmusic=pygame.mixer.Sound('music/map2.wav')
        grid = Pick.GRID_BASE_MapBox
    if(Pick.ChooseMap is Map.Map4):
        backgroundmusic=pygame.mixer.Sound('music/map2.wav')
        grid = Pick.GRID_BASE_MapBox1
    backgroundmusic.play(-1)
    # if en1_alg is not Algorithm.NONE:
    #     en1 = Enemy(11, 11, en1_alg)
    #     en1.load_animations('1', scale)
    #     enemy_list.append(en1)
    #     ene_blocks.append(en1)

    
    if en2_alg is not Algorithm.NONE:
        en2 = Enemy(2, 13, en2_alg)
        en2.load_animations('2', scale)
        enemy_list.append(en2)
        ene_blocks.append(en2)

    if en3_alg is not Algorithm.NONE:
        en3 = Enemy(13, 2, en3_alg)
        en3.load_animations('3', scale)
        enemy_list.append(en3)
        ene_blocks.append(en3)

    if player_alg is Algorithm.PLAYER:
        player.load_animations(scale,"hero","p")
        ene_blocks.append(player)
    elif player_alg is not Algorithm.NONE:
        en0 = Enemy(1, 1, player_alg)
        en0.load_animations('', scale)
        enemy_list.append(en0)
        ene_blocks.append(en0)
        player.life = False
    else:
        player.life = False
    print(enemy_list.__len__)
    if player_alg1 is Algorithm.PLAYER2:
        player1.load_animations(scale,"Player2Image","hero")
        ene_blocks.append(player1)
    elif player_alg1 is not Algorithm.NONE:
        en1 = Enemy(13, 13, player_alg1)
        en1.load_animations('1', scale)
        enemy_list.append(en1)
        ene_blocks.append(en1)
        player1.life = False
    else:
        player1.life = False


    block_img = pygame.image.load('images/terrain/block.png')
    block_img = pygame.transform.scale(block_img, (scale, scale))

    box_img = pygame.image.load('images/terrain/box.png')
    box_img = pygame.transform.scale(box_img, (scale, scale))

    bomb1_img = pygame.image.load('images/bomb/boom1.png')
    bomb1_img = pygame.transform.scale(bomb1_img, (scale, scale))

    bomb2_img = pygame.image.load('images/bomb/boom2.png')
    bomb2_img = pygame.transform.scale(bomb2_img, (scale, scale))

    bomb3_img = pygame.image.load('images/bomb/boom3.png')
    bomb3_img = pygame.transform.scale(bomb3_img, (scale, scale))
    bomb4_img = pygame.image.load('images/bomb/boom4.png')
    bomb4_img = pygame.transform.scale(bomb4_img, (scale, scale))
    
    bomb5_img = pygame.image.load('images/bomb/boom5.png')
    bomb5_img = pygame.transform.scale(bomb5_img, (scale, scale))
    
    bomb6_img = pygame.image.load('images/bomb/boom6.png')
    bomb6_img = pygame.transform.scale(bomb6_img, (scale, scale))
    
    bomb7_img = pygame.image.load('images/bomb/boom7.png')
    bomb7_img = pygame.transform.scale(bomb7_img, (scale, scale))
    
    bomb8_img = pygame.image.load('images/bomb/boom8.png')
    bomb8_img = pygame.transform.scale(bomb8_img, (scale, scale))

    explosion1_img = pygame.image.load('images/explosion/1.png')
    explosion1_img = pygame.transform.scale(explosion1_img, (scale, scale))

    explosion2_img = pygame.image.load('images/explosion/2.png')
    explosion2_img = pygame.transform.scale(explosion2_img, (scale, scale))

    explosion3_img = pygame.image.load('images/explosion/3.png')
    explosion3_img = pygame.transform.scale(explosion3_img, (scale, scale))
    
    
    Floor_img = pygame.image.load(Pick.CreateFloor)
    Floor_img = pygame.transform.scale(Floor_img, (scale, scale))
    
    Block_img = pygame.image.load(Pick.CreateBlock)
    Block_img = pygame.transform.scale(Block_img, (scale, scale))
    
    PossibleBox_img = pygame.image.load(Pick.CreatePossibleBox)
    PossibleBox_img = pygame.transform.scale(PossibleBox_img, (scale, scale))
    
    Outline_img = pygame.image.load(Pick.CreateOutlineBlock)
    Outline_img = pygame.transform.scale(Outline_img, (scale, scale))

    

    

    terrain_images = [Floor_img,Block_img,PossibleBox_img,Floor_img,Outline_img]
    
    bomb_images = [bomb1_img, bomb2_img, bomb3_img,bomb4_img,bomb5_img,bomb6_img,bomb7_img,bomb8_img]
    explosion_images = [explosion1_img, explosion2_img, explosion3_img]

    power_up_bomb_img = pygame.image.load('images/power_up/bomb.png')
    power_up_bomb_img = pygame.transform.scale(power_up_bomb_img, (scale, scale))

    power_up_fire_img = pygame.image.load('images/power_up/fire.png')
    power_up_fire_img = pygame.transform.scale(power_up_fire_img, (scale, scale))

    power_ups_images = [power_up_bomb_img, power_up_fire_img]

    main(surface, scale, path, terrain_images, bomb_images, explosion_images, power_ups_images,grid)
def draw(s, grid, tile_size, show_path, game_ended, terrain_images, bomb_images, explosion_images, power_ups_images):
    s.fill(BACKGROUND_COLOR)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            s.blit(terrain_images[grid[i][j]], (i * tile_size, j * tile_size, tile_size, tile_size))

    for pu in power_ups:
        s.blit(power_ups_images[pu.type.value], (pu.pos_x * tile_size, pu.pos_y * tile_size, tile_size, tile_size))

    for x in bombs:
        s.blit(bomb_images[x.frame], (x.pos_x * tile_size, x.pos_y * tile_size, tile_size, tile_size))

    for y in explosions:
        for x in y.sectors:
            s.blit(explosion_images[y.frame], (x[0] * tile_size, x[1] * tile_size, tile_size, tile_size))
    if player.life:
        s.blit(player.animation[player.direction][player.frame],
               (player.pos_x * (tile_size / 4), player.pos_y * (tile_size / 4), tile_size, tile_size))
    if player1.life:
        s.blit(player1.animation[player1.direction][player1.frame],
               (player1.pos_x * (tile_size / 4), player1.pos_y * (tile_size / 4), tile_size, tile_size))
    for en in enemy_list:
        if en.life:
            s.blit(en.animation[en.direction][en.frame],
                   (en.pos_x * (tile_size / 4), en.pos_y * (tile_size / 4), tile_size, tile_size))
            if show_path:
                if en.algorithm == Algorithm.DFS:
                    for sek in en.path:
                        pygame.draw.rect(s, (255, 0, 0, 240),
                                         [sek[0] * tile_size, sek[1] * tile_size, tile_size, tile_size], 1)
                else:
                    for sek in en.path:
                        pygame.draw.rect(s, (255, 0, 255, 240),
                                         [sek[0] * tile_size, sek[1] * tile_size, tile_size, tile_size], 1)

        

    pygame.display.update()
def generate_map(grid):
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] != 0:
                continue
            elif (i < 3 or i > len(grid) - 4) and (j < 3 or j > len(grid[i]) - 4):
                continue
            if random.randint(0, 9) < 7:
                grid[i][j] = 2
    print(grid)
    return
def main(s, tile_size, show_path, terrain_images, bomb_images, explosion_images, power_ups_images,pickmap):
    
    grid = [row[:] for row in pickmap]
    generate_map(grid)
    
   
    clock = pygame.time.Clock()

    running = True
    game_ended = True
    while running:
        dt = clock.tick(15)
        for en in enemy_list:
            en.make_move(grid, bombs, explosions, ene_blocks)

        if player.life:
            keys = pygame.key.get_pressed()
            temp = player.direction
            movement = False
            if keys[pygame.K_DOWN]:
                temp = 0
                player.move(0, 1, grid, ene_blocks, power_ups)
                movement = True
            elif keys[pygame.K_RIGHT]:
                temp = 1
                player.move(1, 0, grid, ene_blocks, power_ups)
                movement = True
            elif keys[pygame.K_UP]:
                temp = 2
                player.move(0, -1, grid, ene_blocks, power_ups)
                movement = True
            elif keys[pygame.K_LEFT]:
                temp = 3
                player.move(-1, 0, grid, ene_blocks, power_ups)
                movement = True
            if temp != player.direction:
                player.frame = 0
                player.direction = temp
            if movement:
                if player.frame == 2:
                    player.frame = 0
                else:
                    player.frame += 1
        if player1.life:
            keys = pygame.key.get_pressed()
            temp2 = player1.direction
            movement = False            
            if keys[pygame.K_s]:
                temp2 = 0
                player1.move(0, 1, grid, ene_blocks, power_ups)
                movement = True
            elif keys[pygame.K_d]:
                temp2 = 1
                player1.move(1, 0, grid, ene_blocks, power_ups)
                movement = True
            elif keys[pygame.K_w]:
                temp2 = 2
                player1.move(0, -1, grid, ene_blocks, power_ups)
                movement = True
            elif keys[pygame.K_a]:
                temp2 = 3
                player1.move(-1, 0, grid, ene_blocks, power_ups)
                movement = True
            if temp2 != player1.direction:
                player1.frame = 0
                player1.direction = temp2
            if movement:
                if player1.frame == 2:
                    player1.frame = 0
                else:
                    player1.frame += 1

        draw(s, grid, tile_size, show_path, game_ended, terrain_images, bomb_images, explosion_images, power_ups_images)
        if game_ended:
            
            Result,game_ended = check_end_game()
            window = tk.Tk()
            window.withdraw()
           
            if(Result == 1):
                win= pygame.mixer.Sound('music/win.wav')
                win.play()  
                result = messagebox.showinfo("Notification","Player 2 win")
                running = False
            if(Result == 2):
                win= pygame.mixer.Sound('music/win.wav')
                win.play()  
                result = messagebox.showinfo("Notification","Player 1 win")
                running = False
            if(Result ==3):
                win= pygame.mixer.Sound('music/win.wav')
                win.play()  
                result = messagebox.showinfo("Notification","Monster win")
                running = False
                
            if(Result == 4):
                win= pygame.mixer.Sound('music/win.wav')
                win.play()  
                result = messagebox.showinfo("Notification","Monster win")
                running = False
            if(Result == 5):
                win= pygame.mixer.Sound('music/win.wav')
                win.play()  
                result = messagebox.showinfo("Notification","Player 1 win")
                running = False
            if(Result == 7):
                win= pygame.mixer.Sound('music/win.wav')
                win.play()  
                result = messagebox.showinfo("Notification","Player 2 win")
                running = False
            if(Result == 8):
                win= pygame.mixer.Sound('music/win.wav')
                win.play()  
                result = messagebox.showinfo("Notification","Player 1 win")
                running = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                
                sys.exit(0)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RSHIFT:
                    if player.bomb_limit == 0 or not player.life:
                        continue
                    temp_bomb = player.plant_bomb(grid)
                    bombs.append(temp_bomb)
                    grid[temp_bomb.pos_x][temp_bomb.pos_y] = 3
                    player.bomb_limit -= 1
                if e.key == pygame.K_SPACE:
                    if player1.bomb_limit == 0 or not player1.life:
                        continue
                    temp_bomb = player1.plant_bomb(grid)
                    bombs.append(temp_bomb)
                    grid[temp_bomb.pos_x][temp_bomb.pos_y] = 3
                    player1.bomb_limit -= 1
                elif e.key == pygame.K_ESCAPE:
                    running = False

        update_bombs(grid, dt)

    explosions.clear()
    enemy_list.clear()
    ene_blocks.clear()
    power_ups.clear()
def update_bombs(grid, dt):
    for b in bombs:
        b.update(dt)
        if b.time < 1:
            b.bomber.bomb_limit += 1
            grid[b.pos_x][b.pos_y] = 0
            exp_temp = Explosion(b.pos_x, b.pos_y, b.range)
            exp_temp.explode(grid, bombs, b, power_ups)
            exp_temp.clear_sectors(grid, random, power_ups)
            explosions.append(exp_temp)
    if player not in enemy_list:
        player.check_death(explosions)
    if player1 not in enemy_list:
        player1.check_death(explosions)
    for en in enemy_list:
        en.check_death(explosions)
    for e in explosions:
        e.update(dt)
        if e.time < 1:
            a=pygame.mixer.Sound('music/bomb_bang.wav')
            a.set_volume(0.5)
            a.play()
            explosions.remove(e)
def check_end_game():
    
    if(checkplayer is Algorithm.PLAYER2):
        if(enemy_list == []):
            if not player.life:
                    return 7,False
            if not player1.life:
                    return 8,False
        else:
            if not player.life:
                for en in enemy_list:
                    if not en.life:
                        return 1,False
                
            if not player1.life:
                for en in enemy_list:
                    if not en.life:
                        return 2,False
            for en in enemy_list:
                if(not player.life and not player1.life):
                    return 3,False
    else:
        if(not player.life):
            return 4,False
            
        for en in enemy_list:
            if not en.life:
                return 5,False
        return 6,True
    return -1,True

    