import pygame, math
from pygame.locals import *

# init ----------------------------------------------------
mainClock = pygame.time.Clock()

pygame.init()  # init
pygame.display.set_caption('🎲Yachz')
display_width = 1200
display_height = 550
screen = pygame.display.set_mode((display_width, display_height))

#  variable ----------------------------------------------------


# background ----------------------------------------------------
background = pygame.image.load("data/background/background.png")
background = pygame.transform.scale(background, (1200, 550))


#  score_board ----------------------------------------------------
class score_board:
    def __init__(self, type):
        self.image = pygame.image.load("data/score_board/score_board.png")
        self.image = pygame.transform.scale(self.image, (300, display_height - 20 * 2))
        self.type = type

        if self.type == 'Left':
            self.x = 10
            self.y = (display_height - self.image.get_height()) // 2
        else:
            self.x = display_width - self.image.get_width() - 10
            self.y = (display_height - self.image.get_height()) // 2

    # def set(self):
    #     screen.blit(self.image, (self.x, self.y))
    #
    # def fade_in(self):
    #     if self.type == 'Left':
    #         pass
    #     else:
    #         pass
    #
    # def fade_out(self):
    #     if self.type == 'Left':
    #         pass
    #     else:
    #         pass


left_score_board = score_board('Left')
right_score_board = score_board('Right')


# dice ----------------------------------------------------
class dice:
    def __init__(self, num):
        self.num = num
        self.image = pygame.image.load("data/dice/dice_" + num + '.png')


# title ----------------------------------------------------
tittle_font = pygame.font.Font("BlackHanSans-Regular.ttf", 100)
tittle = tittle_font.render('Yachz!', True, '#ffecd6')
tittle_shadow = tittle_font.render('Yachz!', True, '#0d2b45')

press_SPACE_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)
press_SPACE = press_SPACE_font.render('press SPACE', True, '#ffecd6')
press_SPACE_shadow = press_SPACE_font.render('press SPACE', True, '#0d2b45')

tittle_phase = True

tittle_x = display_width // 2 - tittle.get_width() // 2
tittle_y = display_height // 2 - (tittle.get_height() + press_SPACE.get_height() + 20) // 2
tittle_shadow_x = tittle_x + 6
tittle_shadow_y = tittle_y + 6

press_SPACE_x = display_width // 2 - press_SPACE.get_width() // 2
press_SPACE_y = tittle_y + tittle.get_height() + 20
press_SPACE_shadow_x = press_SPACE_x + 4
press_SPACE_shadow_y = press_SPACE_y + 4

# game prepare ----------------------------------------------------
game_prepare_phase = False

# running ----------------------------------------------------
running = True
while running:
    screen.blit(background, (0, 0))

    if tittle_phase:
        screen.blit(tittle_shadow, (tittle_shadow_x, tittle_shadow_y))
        screen.blit(tittle, (tittle_x, tittle_y))
        screen.blit(press_SPACE_shadow, (press_SPACE_shadow_x, press_SPACE_shadow_y))
        screen.blit(press_SPACE, (press_SPACE_x, press_SPACE_y))

    if game_prepare_phase:
        left_score_board.set()
        right_score_board.set()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if tittle_phase:
                    game_prepare_phase = True
                    tittle_phase = False

    pygame.display.update()
    mainClock.tick(60)

# pygame 종료
pygame.quit()
