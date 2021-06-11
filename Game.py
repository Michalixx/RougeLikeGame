import pygame as pg
from Bullet import Bullet
import math
import random
from Enemy import Enemy
import settings as stt
import stats
import time


# Collision
def collision(x1, y1, x2, y2, radius):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return radius >= distance


class Game:
    def __init__(self):

        pg.init()

        self.screen = pg.display.set_mode((1280, 720))  # 16:9
        pg.display.set_caption("Colours vs ASCII")
        pg.display.update()

        self.HP = stt.MAX_HP
        self.money = stt.money
        self.money_per_hit = stt.money_per_hit
        self.time = 0
        self.wave_counter = 0

        self.any_bullet_fired = False

        # Player
        self.player_img = pg.image.load('icons/player.png')
        self.player_x = 640  # Starting X coordinate
        self.player_y = 680  # Starting Y coordinate, this value is const (due to game rules)
        self.player_x_change = stt.player_speed  # Speed of player

        # Bullets are fired by 3 keys Z,X,C in order: Red Green Blue
        self.bullets = [Bullet('red', self.player_y, stt.bullet_red_level, stt.bullet_red_speed, stt.bullet_red_power),
                        Bullet('green', self.player_y, stt.bullet_green_level, stt.bullet_green_speed,
                               stt.bullet_green_power),
                        Bullet('blue', self.player_y, stt.bullet_blue_level, stt.bullet_blue_speed,
                               stt.bullet_blue_power)]

        # Enemies
        self.enemies = []
        self.MAX_ENEMIES = 100
        self.wave_enemies = 0

        # Text settings
        self.font = pg.font.Font('fonts/AmaticSC-Regular.ttf', 48)
        self.money_x = 60
        self.money_y = 10
        self.time_x = 740
        self.time_y = 10
        self.hp_x = 1200
        self.hp_y = 10
        self.wave_x = 440
        self.wave_y = 10

    # FUNCTION
    # Draw player
    def draw_player(self):
        self.screen.blit(self.player_img, (self.player_x, self.player_y))

    # Draw bullets
    def draw_bullet(self, bullet):
        self.screen.blit(bullet.get_image(), (bullet.get_x(), bullet.get_y()))

    # Draw enemy
    def draw_enemy(self, enemy):
        self.screen.blit(enemy.get_image(), enemy.get_coordinate())

    # Draw interface
    def draw_money(self):
        tmp = self.font.render(str(self.money), True, (255, 255, 255))
        self.screen.blit(pg.image.load('icons/money.png'), (self.money_x - 40, self.money_y + 15))
        self.screen.blit(tmp, (self.money_x, self.money_y))

    # Draw time
    def draw_time(self):
        tmp = self.font.render(str(self.time), True, (255, 255, 255))
        self.screen.blit(tmp, (self.time_x, self.time_y))

    def draw_hp(self):
        tmp = self.font.render(str(self.HP), True, (255, 255, 255))
        self.screen.blit(tmp, (self.hp_x, self.hp_y))
        self.screen.blit(pg.image.load('icons/heart.png'), (self.hp_x - 40, self.hp_y + 15))

    def draw_wave(self):
        tmp = self.font.render("Wave: " + str(self.wave_counter), True, (255, 255, 255))
        self.screen.blit(tmp, (self.wave_x, self.wave_y))

    # Add enemies
    def add_enemies(self):
        if self.wave_enemies == 0:
            if self.wave_counter != 0: stats.total_wave_completed += 1
            self.wave_counter += 1
            self.wave_enemies = min(random.randrange(self.wave_counter, 2*self.wave_counter)*2+5, self.MAX_ENEMIES)
            self.enemies.clear()
            for i in range(self.wave_enemies):
                self.enemies.append(Enemy(self.wave_counter))  # Real enemies
            for i in range(self.MAX_ENEMIES - self.wave_enemies):
                self.enemies.append(Enemy(self.wave_counter, False))  # Fake enemies

    def run_game(self):
        t0 = time.time()
        while self.HP > 0:
            self.screen.fill((132, 164, 207))  # Setting background colour

            # Quit
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.HP = 0

            # self.time = pg.time.get_ticks() / 1000  # Time counter
            self.time = round(time.time() - t0, 2)

            # Keys event
            pg.event.pump()
            keys = pg.key.get_pressed()

            # Player movement
            if keys[pg.K_LEFT]:
                if self.player_x > 0:
                    self.player_x -= self.player_x_change
            if keys[pg.K_RIGHT]:
                if self.player_x < 1248:
                    self.player_x += self.player_x_change

            # Fire bullets
            if keys[pg.K_z]:
                if not self.any_bullet_fired:
                    self.bullets[0].set_fired(True)
                    self.any_bullet_fired = True
                    self.bullets[0].set_x(self.player_x)
                    stats.bullet_red_fired += 1
            if keys[pg.K_x]:
                if not self.any_bullet_fired:
                    self.bullets[1].set_fired(True)
                    self.any_bullet_fired = True
                    self.bullets[1].set_x(self.player_x)
                    stats.bullet_green_fired += 1
            if keys[pg.K_c]:
                if not self.any_bullet_fired:
                    self.bullets[2].set_fired(True)
                    self.any_bullet_fired = True
                    self.bullets[2].set_x(self.player_x)
                    stats.bullet_blue_fired += 1

            # Bullets movement
            for bullet in self.bullets:
                if bullet.is_fired():
                    if bullet.get_y() <= 1:
                        bullet.set_fired(False)
                        self.any_bullet_fired = False
                        bullet.set_y(self.player_y)
                    else:
                        bullet.set_y(bullet.get_y() - bullet.get_speed())
                        self.draw_bullet(bullet)

            # Draw enemy
            for enemy in self.enemies:
                if enemy.is_alive():
                    self.draw_enemy(enemy)

            # Check hit and delete killed enemies
            for enemy in self.enemies:
                for bullet in self.bullets:
                    if enemy.is_alive():
                        if collision(bullet.get_x(), bullet.get_y(), enemy.get_x(), enemy.get_y(), bullet.get_radius()):
                            tmp1 = enemy.get_hp()
                            enemy.mark_hit(bullet)
                            tmp2 = enemy.get_hp()
                            print(tmp1, "-->", tmp2)
                            bullet.set_fired(False)
                            self.any_bullet_fired = False
                            bullet.set_y(self.player_y)
                            self.money += self.money_per_hit
                            if not enemy.is_alive():
                                self.enemies.remove(enemy)
                                self.wave_enemies -= 1
                                self.enemies.append(Enemy(self.wave_counter, False))
                                enemy.update_stats()
                        enemy.move()
                        if enemy.get_x() >= 1270 and not enemy.get_y() == 2000:
                            self.HP -= enemy.get_hp()
                            enemy.kill()
                            self.enemies.remove(enemy)
                            self.wave_enemies -= 1
                            self.enemies.append(Enemy(self.wave_counter, False))

            self.add_enemies()

            self.draw_money()
            self.draw_time()
            self.draw_hp()
            self.draw_wave()
            self.draw_player()
            pg.display.update()

        stt.money = self.money
        stats.time_played += self.time
        stats.total_money_earned += self.money
        pg.display.quit()
