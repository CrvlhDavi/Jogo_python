#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # CHECK ALL EVENTS
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()  # Close window
            #         quit()  # end pygame

