import sys
from datetime import datetime

import pygame as pg
from pygame import Surface, Rect
from pygame.constants import KEYDOWN, K_BACKSPACE
from pygame.font import Font

from code.Const import SCORE_POS, COLOR_GREEN, MENU_OPTION, COLOR_ORANGE, COLOR_CYAN
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("./asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode:str, player_score:list[int]):
        pg.mixer_music.load('./asset/Score.mp3')
        pg.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ' '

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', COLOR_CYAN,SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Prayer 1 your name (4 characters): '
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (4 characters): '
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player name (4 characters): '
                else:
                    score = player_score[1]
                    text = 'Enter Player name (4 characters): '
            self.score_text(36, text, COLOR_ORANGE, SCORE_POS['EnterName'])
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == pg.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score,'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(48, name, COLOR_ORANGE, SCORE_POS['Name'])


            pg.display.flip()


    def show(self):
        pg.mixer_music.load('./asset/Score.mp3')
        pg.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_CYAN, SCORE_POS['Title'])
        self.score_text(20, 'NAME   SCORE   DATE  ',COLOR_ORANGE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()


        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}   {score:05d}   {date}', COLOR_GREEN,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
            pg.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name= 'Lucinda Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time =current_datetime.strftime('%H:%M')
    current_date =current_datetime.strftime('%d/%m/%y')
    return f'{current_time} - {current_date}'


