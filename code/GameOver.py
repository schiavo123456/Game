import sys

import pygame
from pygame.constants import KEYDOWN, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_YELLOW, GAME_OVER_POS


class GameOver:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/GameOverBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show_game_over(self):
        pygame.mixer_music.load('./asset/GameOver.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.game_over_text(48, 'GAME', C_YELLOW, GAME_OVER_POS['Title0'])
        self.game_over_text(48, 'OVER', C_YELLOW, GAME_OVER_POS['Title1'])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def game_over_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
