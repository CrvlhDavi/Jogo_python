#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Const import ENTITY_SPEED, WIN_HEIGHT
from code.entity1 import Entity1


class Player(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[pg.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_keys[pg.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_keys[pg.K_RIGHT] and self.rect.right < WIN_HEIGHT:
            self.rect.centerx += ENTITY_SPEED[self.name]

