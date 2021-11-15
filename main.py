import pygame, random
from pygame.locals import *

# init ----------------------------------------------------
mainClock = pygame.time.Clock()

pygame.init()  # init
pygame.display.set_caption('🎲Yachz')
display_width = 874
display_height = 550
screen = pygame.display.set_mode((display_width, display_height))

#  variable ----------------------------------------------------
dice_inter = 10
game_prepare_tick = 2000
player1 = True
left = 3

# background ----------------------------------------------------
background = pygame.image.load("data/background/background.png")
background = pygame.transform.scale(background, (1200, 550))


#  score_board ----------------------------------------------------
class score_board:
    def __init__(self, type):
        self.image = pygame.image.load("data/score_board/score_board.png")
        self.image = pygame.transform.scale(self.image, (187, display_height - 20 * 2))
        self.type = type

        if self.type == 'Left':
            self.x = 10
            self.y = (display_height - self.image.get_height()) // 2
        else:
            self.x = display_width - self.image.get_width() - 10
            self.y = (display_height - self.image.get_height()) // 2

        self.turn = 1
        self.aces = None
        self.deuces = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.subtotal = 0
        self.bonus = None
        self.choice = None
        self.four_of_a_kind = None
        self.full_house = None
        self.s_straight = None
        self.l_straight = None
        self.yacht = None
        self.total = 0

    def set(self):
        screen.blit(self.image, (self.x, self.y))

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

turn_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)
turn = turn_font.render('Yachz!', True, '#0d2b45')
score_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)
score = score_font.render('Yachz!', True, '#0d2b45')
subtotal_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)
subtotal = subtotal_font.render('Yachz!', True, '#0d2b45')
total_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)
total = total_font.render('Yachz!', True, '#0d2b45')


# dice ----------------------------------------------------
class dice_class:
    def __init__(self, num, seq):
        self.num = num
        self.seq = seq

        self.width_sum = 0
        self.dice_image = []

        self.fixed = False
        self.y = display_height // 2 - 75 // 2

        for i in range(6):
            image = pygame.image.load('data/dice/dice_' + str(i + 1) + '.png')
            self.dice_image.append(pygame.transform.scale(image, (75, 75)))
            self.width_sum += self.dice_image[i].get_width()

    def set(self):
        if self.seq == 1:
            self.x = display_width // 2 - self.width_sum * 2.5 / 6 - dice_inter * 2
        elif self.seq == 2:
            self.x = display_width // 2 - self.width_sum * 1.5 / 6 - dice_inter
        elif self.seq == 3:
            self.x = display_width // 2 - self.width_sum * 0.5 / 6
        elif self.seq == 4:
            self.x = display_width // 2 + self.width_sum * 0.5 / 6 + dice_inter
        elif self.seq == 5:
            self.x = display_width // 2 + self.width_sum * 1.5 / 6 + dice_inter * 2

        screen.blit(self.dice_image[self.num - 1], (self.x, self.y))

    def roll(self):
        if not self.fixed:
            self.num = random.randint(1, 6)
            screen.blit(self.dice_image[self.num - 1],
                        (self.x + random.randint(-5, 5), self.y + random.randint(-5, 5)))
        else:
            screen.blit(self.dice_image[self.num - 1], (self.x, self.y))

    def up(self):
        self.y -= 100
        self.fixed = True

    def down(self):
        self.y += 100
        self.fixed = False


dice = []
for i in range(5):
    dice.append(dice_class(i + 2, i + 1))


# score ----------------------------------------------------
def score(score_board):
    if score_board.type == 'Left':
        pass
    else:
        pass


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

Left_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)
Left = Left_font.render('Left: ' + str(left), True, '#ffecd6')
Left_shadow = Left_font.render('Left: ' + str(left), True, '#0d2b45')

Left_x = display_width // 2 - Left.get_width() // 2
Left_y = 20
Left_shadow_x = Left_x + 4
Left_shadow_y = Left_y + 4


# roll ----------------------------------------------------
roll_phase = False


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

        for i in range(5):
            dice[i].set()
        screen.blit(press_SPACE_shadow, (press_SPACE_shadow_x, press_SPACE_shadow_y))
        screen.blit(press_SPACE, (press_SPACE_x, press_SPACE_y))

        Left = Left_font.render('Left: ' + str(left), True, '#ffecd6')
        Left_shadow = Left_font.render('Left: ' + str(left), True, '#0d2b45')
        screen.blit(Left_shadow, (Left_shadow_x, Left_shadow_y))
        screen.blit(Left, (Left_x, Left_y))

    if roll_phase:
        left_score_board.set()
        right_score_board.set()
        for i in range(5):
            dice[i].roll()

        if pygame.time.get_ticks() - start >= 1500:
            for i in range(5):
                dice[i].set()
            game_prepare_phase = True
            roll_phase = False

        screen.blit(Left_shadow, (Left_shadow_x, Left_shadow_y))
        screen.blit(Left, (Left_x, Left_y))

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if tittle_phase:
                    game_prepare_phase = True
                    tittle_phase = False

                elif game_prepare_phase:
                    if left >= 1:
                        roll_phase = True
                        game_prepare_phase = False
                        start = pygame.time.get_ticks()
                        left -= 1

        if event.type == MOUSEBUTTONDOWN:
            click_x = pygame.mouse.get_pos()[0]
            click_y = pygame.mouse.get_pos()[1]

            if event.button == 1:
                if game_prepare_phase:
                    if 0 < left <= 2:
                        for i in range(5):
                            if dice[i].x <= click_x <= dice[i].x + dice[i].dice_image[dice[i].num - 1].get_width() and \
                                    dice[i].y <= click_y <= dice[i].y + dice[i].dice_image[dice[i].num - 1].get_height():
                                if not dice[i].fixed:
                                    dice[i].up()
                                else:
                                    dice[i].down()

    pygame.display.update()
    mainClock.tick(60)

# pygame 종료
pygame.quit()
