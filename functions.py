import pygame
import time

# shows the title on the start screen
def title_screen(screen):
    font_title = pygame.font.Font('Fonts/Calibri.ttf',50)
    title_surf = font_title.render('Speed Typing Test', True, '#0008ad')
    title_rec = title_surf.get_rect(center=(400, 150))
    screen.blit(title_surf, title_rec)

# shows the start screen
def start_screen():
    font_start = pygame.font.Font('Fonts/Calibri.ttf',25)
    start_surf = font_start.render('Clicks here to begin', True, '#0008ad')
    start_rec = start_surf.get_rect(center=(400, 200))
    return start_surf, start_rec

# shows the input text
def text_input(text,screen):
    font_text = pygame.font.Font('Fonts/Calibri.ttf', 25)
    input_box = pygame.Rect(50, 220, 700, 35)
    text_surf = font_text.render(text, True, '#0008ad')
    text_rect = text_surf.get_rect(center=(400, 238))
    screen.blit(text_surf, text_rect)
    pygame.draw.rect(screen, "#000566", input_box, 2, 20)

# shows the sentence
def get_sentence(screen, sentence):
    font_sentence = pygame.font.Font('Fonts/Calibri.ttf', 25)
    sentence_surf = font_sentence.render(sentence, True, '#000000')
    sentence_rect = sentence_surf.get_rect(center=(400, 200))
    screen.blit(sentence_surf, sentence_rect)

def typing_title(screen):
    typing = pygame.font.Font('Fonts/Calibri.ttf', 35).render('TYPE! When finished, press Enter to show results!'
                                                              , True, '#0008ad')
    typing_rect = typing.get_rect(center=(400, 130))
    screen.blit(typing, typing_rect)

# get the sentence
def get_text():
    with open('sentences.txt','r') as file:
        f = file.read().splitlines()
    return f

# calculate accuracy by comparing each letter from input text to its corespondent index in the sentence
def accuracy(text, sentence):
    count = 0
    for index, character in enumerate(sentence):
        try:
            if text[index] == character:
                count += 1
        except:
            pass
    accuracy = count * 100 / len(sentence)
    return "{:.2f}".format(accuracy), count

# calculates the type speed of the correct characters
def results(text,sentence,start_time):
    end_time = time.time()
    time_elapsed = end_time - start_time
    acc, chs = accuracy(text, sentence)
    cps = "{:.2f}".format(chs / time_elapsed)
    return acc, cps

# show the results on the screen
def show_results(acc,cps,screen):
    results_title = pygame.font.Font('Fonts/Calibri.ttf', 35).render('RESULTS! Press Enter to restart', True, '#0008ad')
    results_title_rect = results_title.get_rect(center=(400, 130))
    screen.blit(results_title, results_title_rect)

    results_surf = pygame.font.Font('Fonts/Calibri.ttf', 25).render(f'Accuracy: {acc} %, '
                                                                    f'Characters per second: {cps}', True,
                                                                    '#0008ad')
    results_rect = results_surf.get_rect(center=(400, 280))
    screen.blit(results_surf,results_rect)
