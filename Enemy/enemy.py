import random
import pygame

from Enemy.class_enemy import Enemy
from game.game import Game


hp = 100
def create_enemy():
    game = Game()
    x = random.randint(0, game.width - 50)
    y = random.randint(0, game.height - 50)
    enemy = Enemy(game.width, game.height, x, y)
    rectEnemy = pygame.Rect(enemy.x,enemy.y,50,50)
    return rectEnemy

def move_enemy_to_player(enemy,player):
    speed = 2
    snake_case = pygame.Vector2(enemy.center)
    player = pygame.Vector2(player.center)
    distance_vector = player - snake_case
    rec = distance_vector.length()
    if rec > 0:
        distance = pygame.math.Vector2.normalize(distance_vector)
        result = distance * speed
        pygame.Rect.move_ip(enemy,result.x,result.y)
        print(result)

def enemy_collider_with_player(enemy,player):
    if pygame.Rect.colliderect(enemy,player):
        return True
    return False

def bool_collider(value,player):
    if value:
        player.hp = player.hp -5
        if player.hp <= 0:
            return True
        else:
            return False

