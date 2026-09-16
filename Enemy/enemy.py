import random
import pygame

from Enemy.class_enemy import Enemy
from game.game import Game



def create_enemy():
    game = Game()
    x = random.randint(0, game.width - 50)
    y = random.randint(0, game.height - 50)
    enemy = Enemy(game.width, game.height, x, y)
    rectEnemy = pygame.Rect(enemy.x,enemy.y,50,50)
    return rectEnemy

def move_enemy_to_player(enemy,player):

    enemy = pygame.Vector2(enemy.center)
    player = pygame.Vector2(player.center)
    distance_vector = player - enemy
    rec = distance_vector.length()
    if rec > 0:
        result = pygame.math.Vector2.normalize(distance_vector)
        print(result)

