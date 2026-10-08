#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractclassmethod, abstractmethod  # classe abstrata
import pygame.image

from code.Const import ENTITY_HEALTH


class Entity1(ABC):
    #background paralax
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()#otimiza a imagem png
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self):

        pass
