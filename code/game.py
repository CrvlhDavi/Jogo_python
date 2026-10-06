#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))#inicia a tela com a imagem formatada

    def run(self):
         while True:
            menu = Menu(self.window)
            menu.run()


