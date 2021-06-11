import pygame as pg


class Bullet:
    def __init__(self, colour, y, level, speed, power):
        self.colour = colour
        if level > 4: level = 1
        self.level = level
        self.x = 0
        self.y = y
        self.speed = speed
        self.radius = 32
        self.fired = False
        self.power = power

    def level_up(self):
        if self.level < 4:
            self.level += 1
            self.radius += 8

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_speed(self, speed):
        self.speed = speed

    def set_radius(self, radius):
        self.radius = radius

    def set_fired(self, fired):
        self.fired = fired

    def set_power(self, power):
        self.power = power

    def get_colour(self):
        return self.colour

    def get_image(self):
        tmp = 'icons/bullet_' + self.colour + "_size_" + str(self.level) + ".png"
        return pg.image.load(tmp)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_speed(self):
        return self.speed

    def get_radius(self):
        return 32 + (self.level-1)*8

    def is_fired(self):
        return self.fired

    def get_power(self):
        return self.power
