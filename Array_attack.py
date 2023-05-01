import pygame
from sys import exit
import image_animations

def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_surface = time_font.render(f'Time Played: {current_time} seconds',True,('#ffffff'))
    time_rect = time_surface.get_rect(center = (1200,700))
    screen.blit(time_surface, time_rect)

def player_animation():
    global player_surface, player_index
    player_index += .35
    if player_index >= len(player_idle): player_index = 0
    player_surface = player_idle[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Python Array Attack')
clock = pygame.time.Clock()
game_font = pygame.font.Font('fonts/Blackcastlemf-BG5n.ttf', 40)
time_font = pygame.font.Font('fonts/Blackcastlemf-BG5n.ttf', 12)
game_active = False
start_time = 0
player_selection = 1
bg_music = pygame.mixer.Sound('music/simple-piano-melody.mp3')
bg_music.set_volume(.5)
bg_music.play(loops = -1)

instruction_surface = pygame.Surface((900,150))
instruction_surface.fill('#ffe5b4')
instruction_rectangle = instruction_surface.get_rect(topleft = (190,560))

game_background_surface = pygame.image.load('backgrounds/game_background_dragon_cave.png').convert_alpha()
text_surface = game_font.render('Use your array attack!', True, 'white')
text_rectangle = text_surface.get_rect(midtop = (640,560))

player_idle = []
for i in range(len(image_animations.player_idle_images)):
    image_animations.player_idle_images[i] = pygame.image.load(image_animations.player_idle_images[i]).convert_alpha()
    player_idle.append(image_animations.player_idle_images[i])


for i in range(len(image_animations.player_idle_images)):
    player_idle[i] = pygame.transform.rotozoom(player_idle[i], 0, .25)

player_index = 0
player_x_pos = 200
player_y_pos = 500
player_surface = player_idle[player_index]
player_rectangle = player_surface.get_rect(midbottom = (player_x_pos,player_y_pos))

player_start_screen = pygame.image.load('characters/0_Archer_Idle Blinking_015.png').convert_alpha()
player_start_screen = pygame.transform.rotozoom(player_start_screen, 0, .5)
player_start_screen_rectangle = player_start_screen.get_rect(center = (640,360))

text_start_screen = game_font.render("Press Enter to Start", True, 'white')
text_start_screen_rectangle = text_surface.get_rect(midtop = (640, 500))


class Enemy:
    def __init__(self, image, health, position): 
        self.image_path = image
        self.health = health
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.surface = pygame.image.load(self.image_path).convert_alpha()
        self.rectangle = self.surface.get_rect(midbottom = (self.x_pos,self.y_pos))


js_bat_enemy01 = Enemy('enemies\js_bat_idle_0.png', 100, (800,550))
js_bat_enemy02 = Enemy('enemies\js_bat_idle_0.png', 100, (800,400))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_rectangle.bottom -= 5
            if event.key == pygame.K_s:
                player_rectangle.bottom += 5
            if event.key == pygame.K_d:
                player_rectangle.right += 50
            if event.key == pygame.K_UP:
                player_selection += 1
            if event.key == pygame.K_DOWN:
                player_selection -= 1
            if event.key == pygame.K_RETURN:
                player_rectangle.midbottom = (player_x_pos,player_y_pos)
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
            
    
    if game_active:
        
        screen.blit(game_background_surface, (0,0))
        screen.blit(instruction_surface, (190,560))
        pygame.draw.rect(screen, 'pink', text_rectangle)
        pygame.draw.rect(screen, 'white', instruction_rectangle, 3 )
        screen.blit(text_surface, text_rectangle)

        display_time()

        player_animation()
        screen.blit(player_surface, player_rectangle)
        screen.blit(js_bat_enemy01.surface, js_bat_enemy01.rectangle)
        screen.blit(js_bat_enemy02.surface, js_bat_enemy02.rectangle)

        if player_rectangle.colliderect(js_bat_enemy01.rectangle):
            game_active = False
    
    else: 
        screen.blit(game_background_surface, (0,0))
        screen.blit(player_start_screen, player_start_screen_rectangle)
        if (player_selection == 1):
            pygame.draw.rect(screen, 'pink', text_start_screen_rectangle )
        screen.blit(text_start_screen, text_start_screen_rectangle)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     print("up")

        # if player_rectangle.colliderect(js_bat_enemy01.rectangle):
        #     player_rectangle.left = 200

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rectangle.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60)

