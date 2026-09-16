import pygame
vel = 2
def move_player(r):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        r.y -= vel
    if keys[pygame.K_s]:
        r.y += vel
    if keys[pygame.K_a] :
        r.x -= vel
    if keys[pygame.K_d]:
        r.x += vel

def player_can_not_go_off_screen(display,rect_player):
    window_rect = pygame.Surface.get_rect(display)
    rect_player.clamp_ip(window_rect)
