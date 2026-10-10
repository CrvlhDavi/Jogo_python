#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
from tkinter.font import Font

import pygame as pg
from pygame import Surface, Rect

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAW_TIME, COLOR_GREEN, COLOR_CYAN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.EntityMediator import EntityMediator
from code.enemy import Enemy
from code.entity1 import Entity1
from code.entityFactory import EntityFactory
from code.player import Player
#construtor
class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]): #paremetros
        self.timeout = TIMEOUT_LEVEL  #segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity1] = [] #lista de entidades vazias
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]#position player 1 list game.py
        self.entity_list.append(player)

        if game_mode in[MENU_OPTION[1], MENU_OPTION[2]]: #const.py
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1] #position player 2 list game.py
            self.entity_list.append(player)

        #evento
        pg.time.set_timer(EVENT_ENEMY, SPAW_TIME)
        pg.time.set_timer(EVENT_TIMEOUT,  TIMEOUT_STEP) #100ms


    def run(self, player_score: list[int]):
            # pg.mixer_music.load(f'./asset/{self.name}.mp3')
            # pg.mixer_music.play(-1)
            clock = pg.time.Clock()#fps
            while True:
                clock.tick(60)#definição do fps
                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()

                    if isinstance(ent, (Player, Enemy)):
                        shoot= ent.shoot()
                        if shoot is not None:
                            self.entity_list.append(shoot)
                    if ent.name == 'Player1':
                        self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 25))
                    if ent.name == 'Player2':
                        self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', COLOR_CYAN, (10, 45))

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit() #permite fechar a janela do jogo
                    if event.type == EVENT_ENEMY:
                        choice = random.choice(('Enemy1', 'Enemy2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))
                    if event.type == EVENT_TIMEOUT:
                        self.timeout -= TIMEOUT_STEP #diminui o tempo de TIMEOUT_STEP até zerar
                        if self.timeout == 0:
                            for ent in self.entity_list:
                                if isinstance(ent, Player) and ent.name == 'Player1':
                                    player_score[0] = ent.score
                                if isinstance(ent, Player) and ent.name == 'Player2':
                                    player_score[1] = ent.score

                            return True

                        found_player = False #player live
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                found_player = True

                        if not found_player: #player die
                            return False


                #printed text
                self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
                self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 15))
                self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 25))
                pg.display.flip()

                #collisions
                EntityMediator.verify_collision(entity_list=self.entity_list)
                EntityMediator.verify_health(entity_list=self.entity_list)
            pass

    def level_text(self, text_size: int,text: str, text_color: tuple, text_pos: tuple ):
        text_font: Font = pg.font.SysFont('Lucinda Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
