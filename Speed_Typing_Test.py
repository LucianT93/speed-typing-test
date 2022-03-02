import sys
import random
from functions import *

# creates a sprite to animate the countdown
class Countdown (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        count1 = pygame.font.Font('Fonts/Calibri.ttf', 80).render('1',True,'#0008ad')
        count2 = pygame.font.Font('Fonts/Calibri.ttf', 80).render('2',True,'#0008ad')
        count3 = pygame.font.Font('Fonts/Calibri.ttf', 80).render('3', True, '#0008ad')
        self.count_change = [count3, count2, count1]
        self.count_index = 0
        self.image = self.count_change[self.count_index]
        self.rect = self.image.get_rect(center=(400, 130))
    def animation(self):
        global state, start_time
        self.count_index += 0.015
        if self.count_index >= len(self.count_change):
            start_time = time.time()
            state = 'play'
            self.count_index = 0
        else:
            self.image = self.count_change[int(self.count_index)]

    def update(self):
        self.animation()

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 400))
background_surf = pygame.image.load('Background.png')

# create the instance of countdown sprite
countdown = pygame.sprite.GroupSingle()
countdown.add(Countdown())

# Input text
text = ''

# states are the variables that controls the state of the game,
# we need multiple states for the start screen, countdown, play and results screens
state = 'non active'
end_time = 0
start_time = 0

while True:
    screen.blit(background_surf, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if state == 'non active':
            if event.type == pygame.MOUSEBUTTONDOWN and start_rec.collidepoint(event.pos) and event.button == 1:
                state = 'countdown'
                sentence = random.choice(get_text())

        elif state == 'play':
            # get the key inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    text = ''
                    state = 'results'
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    continue
                else:
                    text += event.unicode

        elif state == 'results':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = 'non active'

# calls all the functions, depending on the state of the game
    if state == 'non active':
        title_screen(screen)
        start_surf, start_rec = start_screen()
        screen.blit(start_surf, start_rec)
    elif state == 'countdown':
        countdown.draw(screen)
        countdown.update()
        start_time = time.time()
    elif state == 'play':
        text_input(text,screen)
        get_sentence(screen, sentence)
        acc, cps = results(text,sentence,start_time)
        typing_title(screen)
    elif state == 'results':
        text_input(text,screen)
        get_sentence(screen, sentence)
        show_results(acc,cps,screen)

    pygame.display.update()
    clock.tick(60)
