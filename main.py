import pygame, random
from pygame.locals import *

# init ----------------------------------------------------
mainClock = pygame.time.Clock()

pygame.init()  # init
pygame.mixer.init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)
pygame.mixer.music.load('data/music/background_music.mp3')
pygame.mixer.music.play(-1)

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
turn_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)
score_font = pygame.font.Font("BlackHanSans-Regular.ttf", 20)
subtotal_font = pygame.font.Font("BlackHanSans-Regular.ttf", 17)
bonus_font = pygame.font.Font("BlackHanSans-Regular.ttf", 17)
total_font = pygame.font.Font("BlackHanSans-Regular.ttf", 30)


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

        self.turn = 0
        self.aces = None
        self.deuces = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.subtotal = 0
        self.bonus = 0
        self.choice = None
        self.four_of_a_kind = None
        self.full_house = None
        self.s_straight = None
        self.l_straight = None
        self.yacht = None
        self.total = 0

    def set(self):
        screen.blit(self.image, (self.x, self.y))

    def render(self):
        if not self.aces:
            sum = 0
            for i in range(5):
                if dice[i].num == 1: sum += 1

            self.aces_temp = sum
            aces = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(aces, (153, 120))
            else:
                screen.blit(aces, (820, 120))

        if not self.deuces:
            sum = 0
            for i in range(5):
                if dice[i].num == 2: sum += 2

            self.deuces_temp = sum
            deuces = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(deuces, (153, 145))
            else:
                screen.blit(deuces, (820, 145))

        if not self.threes:
            sum = 0
            for i in range(5):
                if dice[i].num == 3: sum += 3

            self.threes_temp = sum
            threes = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(threes, (153, 170))
            else:
                screen.blit(threes, (820, 170))

        if not self.fours:
            sum = 0
            for i in range(5):
                if dice[i].num == 4: sum += 4

            self.fours_temp = sum
            fours = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(fours, (153, 195))
            else:
                screen.blit(fours, (820, 195))

        if not self.fives:
            sum = 0
            for i in range(5):
                if dice[i].num == 5: sum += 5

            self.fives_temp = sum
            fives = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(fives, (153, 220))
            else:
                screen.blit(fives, (820, 220))

        if not self.sixes:
            sum = 0
            for i in range(5):
                if dice[i].num == 6: sum += 6

            self.sixes_temp = sum
            sixes = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(sixes, (153, 245))
            else:
                screen.blit(sixes, (820, 245))

        if not self.choice:
            sum = 0
            for i in range(5):
                sum += dice[i].num

            self.choice_temp = sum
            choice = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(choice, (153, 330))
            else:
                screen.blit(choice, (820, 330))

        if not self.four_of_a_kind:
            kind = []
            cnt = 0
            sum = 0

            for i in range(5):
                kind.append(dice[i].num)

            if len(list(set(kind))) == 2:
                for i in range(5):
                    if kind[0] == dice[i].num:
                        cnt += 1
                    sum += dice[i].num

                if not (cnt == 1 or cnt == 4):
                    sum = 0

            self.four_of_a_kind_temp = sum
            four_of_a_kind = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(four_of_a_kind, (153, 363))
            else:
                screen.blit(four_of_a_kind, (820, 363))

        if not self.full_house:
            kind = []
            cnt = 0
            sum = 0

            for i in range(5):
                kind.append(dice[i].num)

            if len(list(set(kind))) == 2:
                for i in range(5):
                    if kind[0] == dice[i].num:
                        cnt += 1
                    sum += dice[i].num

                if not (cnt == 2 or cnt == 3):
                    sum = 0

            self.full_house_temp = sum
            full_house = score_font.render(str(sum), True, '#d08159')
            if self.type == 'Left':
                screen.blit(full_house, (153, 388))
            else:
                screen.blit(full_house, (820, 388))

        if not self.s_straight:
            kind = []

            for i in range(5):
                kind.append(dice[i].num)

            kind = list(set(kind))
            kind.sort()
            if kind == [1, 2, 3, 4] or kind == [2, 3, 4, 5] or kind == [3, 4, 5, 6] or kind == [1, 2, 3, 4,
                                                                                                5] or kind == [2, 3, 4,
                                                                                                               5,
                                                                                                               6] or kind == [
                1, 2, 3, 4, 6] or kind == [1, 3, 4, 5, 6]:
                self.s_straight_temp = 15
                s_straight = score_font.render('15', True, '#d08159')
            else:
                self.s_straight_temp = 0
                s_straight = score_font.render('0', True, '#d08159')
            if self.type == 'Left':
                screen.blit(s_straight, (153, 413))
            else:
                screen.blit(s_straight, (820, 413))

        if not self.l_straight:
            kind = []

            for i in range(5):
                kind.append(dice[i].num)

            kind.sort()
            if kind == [1, 2, 3, 4, 5] or kind == [2, 3, 4, 5, 6]:
                self.l_straight_temp = 30
                l_straight = score_font.render('30', True, '#d08159')
            else:
                self.l_straight_temp = 0
                l_straight = score_font.render('0', True, '#d08159')
            if self.type == 'Left':
                screen.blit(l_straight, (153, 438))
            else:
                screen.blit(l_straight, (820, 438))

        if not self.yacht:
            kind = []

            for i in range(5):
                kind.append(dice[i].num)

            if len(list(set(kind))) == 1:
                self.yacht_temp = 50
                yacht = score_font.render('50', True, '#d08159')
            else:
                self.yacht_temp = 0
                yacht = score_font.render('0', True, '#d08159')
            if self.type == 'Left':
                screen.blit(yacht, (153, 463))
            else:
                screen.blit(yacht, (820, 463))

    def render_all(self):
        turn = turn_font.render(str(self.turn), True, '#0d2b45')
        if self.type == 'Left':
            screen.blit(turn, (33, 55))
        else:
            screen.blit(turn, (700, 55))

        if self.aces is not None:
            aces = score_font.render(str(self.aces), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(aces, (153, 120))
            else:
                screen.blit(aces, (820, 120))

        if self.deuces is not None:
            deuces = score_font.render(str(self.deuces), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(deuces, (153, 145))
            else:
                screen.blit(deuces, (820, 145))

        if self.threes is not None:
            threes = score_font.render(str(self.threes), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(threes, (153, 170))
            else:
                screen.blit(threes, (820, 170))

        if self.fours is not None:
            fours = score_font.render(str(self.fours), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(fours, (153, 195))
            else:
                screen.blit(fours, (820, 195))

        if self.fives is not None:
            fives = score_font.render(str(self.fives), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(fives, (153, 220))
            else:
                screen.blit(fives, (820, 220))

        if self.sixes is not None:
            sixes = score_font.render(str(self.sixes), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(sixes, (153, 245))
            else:
                screen.blit(sixes, (820, 245))

        subtotal = subtotal_font.render(str(self.subtotal), True, '#0d2b45')
        if self.type == 'Left':
            screen.blit(subtotal, (149, 268))
        else:
            screen.blit(subtotal, (816, 268))

        bonus = bonus_font.render(str(self.bonus), True, '#0d2b45')
        if self.type == 'Left':
            screen.blit(bonus, (153, 290))
        else:
            screen.blit(bonus, (820, 290))

        if self.choice is not None:
            choice = score_font.render(str(self.choice), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(choice, (153, 330))
            else:
                screen.blit(choice, (820, 330))

        if self.four_of_a_kind is not None:
            four_of_a_kind = score_font.render(str(self.four_of_a_kind), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(four_of_a_kind, (153, 363))
            else:
                screen.blit(four_of_a_kind, (820, 363))

        if self.full_house is not None:
            full_house = score_font.render(str(self.full_house), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(full_house, (153, 388))
            else:
                screen.blit(full_house, (820, 388))

        if self.s_straight is not None:
            s_straight = score_font.render(str(self.s_straight), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(s_straight, (153, 413))
            else:
                screen.blit(s_straight, (820, 413))

        if self.l_straight is not None:
            l_straight = score_font.render(str(self.l_straight), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(l_straight, (153, 438))
            else:
                screen.blit(l_straight, (820, 438))

        if self.yacht is not None:
            yacht = score_font.render(str(self.yacht), True, '#0d2b45')
            if self.type == 'Left':
                screen.blit(yacht, (153, 463))
            else:
                screen.blit(yacht, (820, 463))

        total = total_font.render(str(self.total), True, '#0d2b45')
        if self.type == 'Left':
            screen.blit(total, (153, 496))
        else:
            screen.blit(total, (820, 496))


left_score_board = score_board('Left')
right_score_board = score_board('Right')


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


# end ----------------------------------------------------
end_font = pygame.font.Font("BlackHanSans-Regular.ttf", 100)

# running ----------------------------------------------------
running = True
while running:
    screen.blit(background, (0, 0))

    if right_score_board.turn == 12:
        game_prepare_phase = False
        end = end_font.render(str(left_score_board.total)+ ' : ' + str(right_score_board.total), True, '#ffecd6')
        end_shadow = end_font.render(str(left_score_board.total)+ ' : ' + str(right_score_board.total), True, '#0d2b45')
        screen.blit(end_shadow, (tittle_shadow_x, tittle_shadow_y))
        screen.blit(end, (tittle_x, tittle_y))

    if tittle_phase:
        screen.blit(tittle_shadow, (tittle_shadow_x, tittle_shadow_y))
        screen.blit(tittle, (tittle_x, tittle_y))
        screen.blit(press_SPACE_shadow, (press_SPACE_shadow_x, press_SPACE_shadow_y))
        screen.blit(press_SPACE, (press_SPACE_x, press_SPACE_y))

    if game_prepare_phase:
        left_score_board.set()
        right_score_board.set()

        if right_score_board.bonus == 0 and right_score_board.subtotal >= 63:
            right_score_board.bonus = 35
            right_score_board.total += 35

        if left_score_board.bonus == 0 and left_score_board.subtotal >= 63:
            left_score_board.bonus = 35
            left_score_board.total += 35

        if left <= 2:
            if player1:
                left_score_board.render()
            else:
                right_score_board.render()

        left_score_board.render_all()
        right_score_board.render_all()

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

        left_score_board.render_all()
        right_score_board.render_all()

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

            if game_prepare_phase and left <= 2:
                if event.key == K_1:
                    if player1 and left_score_board.aces is None:
                        left_score_board.aces = left_score_board.aces_temp
                        left_score_board.subtotal += left_score_board.aces
                        left_score_board.total += left_score_board.aces
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.aces is None:
                        right_score_board.aces = right_score_board.aces_temp
                        right_score_board.subtotal += right_score_board.aces
                        right_score_board.total += right_score_board.aces
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_2:
                    if player1 and left_score_board.deuces is None:
                        left_score_board.deuces = left_score_board.deuces_temp
                        left_score_board.subtotal += left_score_board.deuces
                        left_score_board.total += left_score_board.deuces
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.deuces is None:
                        right_score_board.deuces = right_score_board.deuces_temp
                        right_score_board.subtotal += right_score_board.deuces
                        right_score_board.total += right_score_board.deuces
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_3:
                    if player1 and left_score_board.threes is None:
                        left_score_board.threes = left_score_board.threes_temp
                        left_score_board.subtotal += left_score_board.threes
                        left_score_board.total += left_score_board.threes
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.threes is None:
                        right_score_board.threes = right_score_board.threes_temp
                        right_score_board.subtotal += right_score_board.threes
                        right_score_board.total += right_score_board.threes
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_4:
                    if player1 and left_score_board.fours is None:
                        left_score_board.fours = left_score_board.fours_temp
                        left_score_board.subtotal += left_score_board.fours
                        left_score_board.total += left_score_board.fours
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.fours is None:
                        right_score_board.fours = right_score_board.fours_temp
                        right_score_board.subtotal += right_score_board.fours
                        right_score_board.total += right_score_board.fours
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_5:
                    if player1 and left_score_board.fives is None:
                        left_score_board.fives = left_score_board.fives_temp
                        left_score_board.subtotal += left_score_board.fives
                        left_score_board.total += left_score_board.fives
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.fives is None:
                        right_score_board.fives = right_score_board.fives_temp
                        right_score_board.subtotal += right_score_board.fives
                        right_score_board.total += right_score_board.fives
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_6:
                    if player1 and left_score_board.sixes is None:
                        left_score_board.sixes = left_score_board.sixes_temp
                        left_score_board.subtotal += left_score_board.sixes
                        left_score_board.total += left_score_board.sixes
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.sixes is None:
                        right_score_board.sixes = right_score_board.sixes_temp
                        right_score_board.subtotal += right_score_board.sixes
                        right_score_board.total += right_score_board.sixes
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_7:
                    if player1 and left_score_board.choice is None:
                        left_score_board.choice = left_score_board.choice_temp
                        left_score_board.total += left_score_board.choice
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.choice is None:
                        right_score_board.choice = right_score_board.choice_temp
                        right_score_board.total += right_score_board.choice
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_8:
                    if player1 and left_score_board.four_of_a_kind is None:
                        left_score_board.four_of_a_kind = left_score_board.four_of_a_kind_temp
                        left_score_board.total += left_score_board.four_of_a_kind
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.four_of_a_kind is None:
                        right_score_board.four_of_a_kind = right_score_board.four_of_a_kind_temp
                        right_score_board.total += right_score_board.four_of_a_kind
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_9:
                    if player1 and left_score_board.full_house is None:
                        left_score_board.full_house = left_score_board.full_house_temp
                        left_score_board.total += left_score_board.full_house
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.full_house is None:
                        right_score_board.full_house = right_score_board.full_house_temp
                        right_score_board.total += right_score_board.full_house
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_0:
                    if player1 and left_score_board.s_straight is None:
                        left_score_board.s_straight = left_score_board.s_straight_temp
                        left_score_board.total += left_score_board.s_straight
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.s_straight is None:
                        right_score_board.s_straight = right_score_board.s_straight_temp
                        right_score_board.total += right_score_board.s_straight
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_q:
                    if player1 and left_score_board.l_straight is None:
                        left_score_board.l_straight = left_score_board.l_straight_temp
                        left_score_board.total += left_score_board.l_straight
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.l_straight is None:
                        right_score_board.l_straight = right_score_board.l_straight_temp
                        right_score_board.total += right_score_board.l_straight
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

                if event.key == K_w:
                    if player1 and left_score_board.yacht is None:
                        left_score_board.yacht = left_score_board.yacht_temp
                        left_score_board.total += left_score_board.yacht
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        left_score_board.turn += 1
                        player1 = False
                        left = 3
                    elif not player1 and right_score_board.yacht is None:
                        right_score_board.yacht = right_score_board.yacht_temp
                        right_score_board.total += right_score_board.yacht
                        for i in range(5):
                            if dice[i].fixed:
                                dice[i].down()
                        right_score_board.turn += 1
                        player1 = True
                        left = 3

        if event.type == MOUSEBUTTONDOWN:
            click_x = pygame.mouse.get_pos()[0]
            click_y = pygame.mouse.get_pos()[1]

            if event.button == 1:
                if game_prepare_phase:
                    if 0 < left <= 2:
                        for i in range(5):
                            if dice[i].x <= click_x <= dice[i].x + dice[i].dice_image[dice[i].num - 1].get_width() and \
                                    dice[i].y <= click_y <= dice[i].y + dice[i].dice_image[
                                dice[i].num - 1].get_height():
                                if not dice[i].fixed:
                                    dice[i].up()
                                else:
                                    dice[i].down()

    pygame.display.update()
    mainClock.tick(60)

# pygame 종료
pygame.quit()
