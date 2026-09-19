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
    last_damage_time = pygame.time.get_ticks()
    damage_cooldown = 500
    font = pygame.font.SysFont("Arial", 50)
    output = font.render("Game over!", True, (255, 255, 255))
    text_rect = output.get_rect(center = screen.get_rect().center)
    game_over = False
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not game_over:
            screen.fill("white")
            move_player(r)
            pygame.draw.rect(screen, "black", r)
            pygame.draw.rect(screen, "red", enemy)
            player_can_not_go_off_screen(screen,r)
            move_enemy_to_player(enemy, r)
            value = enemy_collider_with_player(enemy,r)

            how_much_time_has_passed = (current_time - last_damage_time)

            if value and how_much_time_has_passed >= damage_cooldown:
                collider = bool_collider(value, player)
                last_damage_time = current_time
                if collider:
                    game_over = True
                else:
                    print("tracisz - 5 hp")
        else:
            screen.fill("black")
            screen.blit(output, text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()