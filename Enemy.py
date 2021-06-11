# Types of enemies
# 1 - letter
# 2 - number
# 3 - sign

import pygame as pg
from Bullet import Bullet
import random
import stats

class Enemy:
    def __init__(self, wave, flag=True):
        self.hp = random.randrange(2*wave, 5*wave)
        self.enemy_x = random.randrange(50,150)
        if flag:
            self.enemy_y = random.randrange(50,620)
        else: self.enemy_y = 2000
        self.type = random.randrange(1,4)
        self.speed = random.uniform(0.1, 0.2)

    def get_coordinate(self):
        return self.enemy_x, self.enemy_y

    def get_x(self):
        return self.enemy_x

    def get_y(self):
        return self.enemy_y

    def move(self):
        self.enemy_x += self.speed

    def mark_hit(self, bullet):
        value = bullet.get_power()
        if self.type == 1:
            stats.letters_hits += 1
            if bullet.get_colour() == 'red':
                value *= 2
            elif bullet.get_colour() == 'green':
                value *= 0.5
            elif bullet.get_colour() == 'blue':
                value *= 1
        if self.type == 2:
            stats.numbers_hits += 1
            if bullet.get_colour() == 'red':
                value *= 1
            elif bullet.get_colour() == 'green':
                value *= 2
            elif bullet.get_colour() == 'blue':
                value *= 0.5
        if self.type == 3:
            stats.chars_hits += 1
            if bullet.get_colour() == 'red':
                value *= 0.5
            elif bullet.get_colour() == 'green':
                value *= 1
            elif bullet.get_colour() == 'blue':
                value *= 2
        self.hp -= value

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return "Level " + str(self.level)

    def kill(self):
        self.hp = 0

    def get_hp(self):
        return self.hp

    def update_stats(self):
        if self.type == 1: stats.letters_killed += 1
        elif self.type == 2: stats.numbers_killed += 1
        else: stats.chars_killed += 1

    def get_image(self):  # enemy_type_()_level_().png
        if self.type == 1:
            level = min(self.hp / 5 + 1, 24)
        elif self.type == 2:
            level = min(self.hp / 10 + 1, 9)
        else: level = min(self.hp/10 + 1, 13)
        tmp = "icons\enemy_type_" + str(self.type) + "_level_" + str(int(level)) + ".png"
        return pg.image.load(tmp)
