#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from code.entity1 import Entity1
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode): #paremetros
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity1] = [] #lista de entidades vazias
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))


    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pg.display.flip()


