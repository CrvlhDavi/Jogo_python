#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Const import ENTITY_SPEED, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.entity1 import Entity1


class Player(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):#Player1
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_KEY_DOWN [self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_HEIGHT:
            self.rect.centerx += ENTITY_SPEED[self.name]

        #apos pressed_key [Player_key] puxa os paramentros da Const.py, e [self.name] é utilizado para informar o python que os comandos sao para todos os players




