#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod  # classe abstrata
import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity1(ABC):
    #background paralax
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()#otimiza a imagem png
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):

        pass
