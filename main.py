import pygame
from game.game import Game
from player.player import Player
from player.move_player import move_player, player_can_not_go_off_screen
from Enemy.enemy import create_enemy, move_enemy_to_player,enemy_collider_with_player,bool_collider

def main():
    games = Game()
    player = Player(games.width, games.height)
    pygame.init()
    screen = pygame.display.set_mode((games.width, games.height))
    pygame.display.set_caption("CyberSurvivor")
    clock = pygame.time.Clock()
    running = True
    r = pygame.Rect(player.x, player.y, 50, 50)
    r.center = (player.x, player.y)
    enemy = create_enemy()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")
        move_player(r)
        pygame.draw.rect(screen, "black", r)
        pygame.draw.rect(screen, "red", enemy)
        player_can_not_go_off_screen(screen,r)
        move_enemy_to_player(enemy, r)
        value = enemy_collider_with_player(enemy,r)
        print(bool_collider(value,player))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()