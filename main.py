import random
import pygame

def load_dict(file_name):
    file = open(file_name)
    words = file.readlines()
    file.close()
    return [word[:5].upper() for word in words ]

DICT_GUESSING = load_dict("en.txt")
DICT_ANSWERS = load_dict("wo.txt")
ANSWER = random.choice(DICT_ANSWERS)


WIDTH = 600
HEIGHT = 700
MARGIN = 10
T_MARGIN =  100
B_MARGIN = 100
LR_MARGIN = 100

GREY = (70,70,80)
GREEN = (6, 214, 160)
YELLOW = (255, 209, 102)

INPUT = ""
GUESSES = []
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
UNGUESSED = ALPHABET
GAME_OVER = False

pygame.init()
pygame.font.init()
pygame.display.set_caption("Wordle")

SQ_SIZE = (WIDTH - 4*MARGIN - 2*LR_MARGIN) // 5
FONT = pygame.font.SysFont("free sans bold" , SQ_SIZE)
FONT_SMALL = pygame.font.SysFont("free sans bold" , SQ_SIZE//2)

def determine_unguessed_letters(guesses):
    guessed_letters = "".join(guesses)
    unguessed_letters = ""
    for letter in ALPHABET :
        if letter not in guessed_letters:
            unguessed_letters += letter
    return unguessed_letters

def determine_color(guess, j):
    letter = guess[j]
    if letter == ANSWER[j]:
        return GREEN
    elif letter in ANSWER :
        n_target = ANSWER.count(letter)
        n_correct = 0
        n_occurence = 0
        for i in range(5):
            if guess[i] == letter:
                if i <= j:
                    n_occurence += 1
                if letter == ANSWER[i]:
                    n_correct +=1
        if n_target - n_correct - n_occurence >= 0:
            return YELLOW
    return GREY
    
        
#créer une interface
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#animation loop
animating = True
while animating:
    #background
    screen.fill("white")
    
    determine_unguessed_letters(GUESSES)
    
    #draw uunguessed letters
    letters = FONT_SMALL.render(UNGUESSED, False, GREY)
    surface = letters.get_rect(center = (WIDTH//2, T_MARGIN//2) )
    screen.blit(letters, surface)
    
    #draw guesses
    y = T_MARGIN
    for i in range(6):
        x = LR_MARGIN
        for j in range(5):
            #square
            square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
            pygame.draw.rect(screen, GREY, square, width =2, border_radius = 3)
            
            #letters/words that have already been guessed
            if i < len(GUESSES):
                color = determine_color(GUESSES[i], j)
                pygame.draw.rect(screen, color, square, border_radius = 3)
                letter = FONT.render(GUESSES[i][j], False, (255,255,255) )
                surface = letter.get_rect(center = (x + SQ_SIZE//2, y + SQ_SIZE//2) )
                screen.blit(letter, surface)
                
            #user text input (next guess)
            if i == len(GUESSES) and j < len(INPUT):
                letter = FONT.render(INPUT[j], False, GREY)
                surface = letter.get_rect(center = (x + SQ_SIZE//2, y + SQ_SIZE//2) )
                screen.blit(letter, surface)
            
            
            
            x += SQ_SIZE + MARGIN
        y += SQ_SIZE + MARGIN
            
    #show the correct answer after a gameover 
    if len (GUESSES) == 6 and GUESSES[5] != ANSWER:
        GAME_OVER = True
        letters = FONT.render(ANSWER, False, GREEN)
        surface = letters.get_rect(center = (WIDTH//2, HEIGHT-B_MARGIN//2 - MARGIN) )
        screen.blit(letters, surface)
            
            
    #updating screen
    pygame.display.flip()
    
    #track user interaction 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        #user presses a key    
        elif event.type == pygame.KEYDOWN:
            #escape key to quit the animation
            if event.key == pygame.K_ESCAPE :
                animating = False
                
            #backspace to delete a carachter
            if event.key == pygame.K_BACKSPACE:
                if len(INPUT) > 0:
                    INPUT = INPUT[:len(INPUT)-1]
                    
            
            #return key to submit a guesse
            elif event.key == pygame.K_RETURN:
                if len(INPUT) ==5 and INPUT in DICT_GUESSING:
                    GUESSES.append(INPUT)
                    UNGUESSED = determine_unguessed_letters(GUESSES)
                    GAME_OVER = True if INPUT == ANSWER else False
                    INPUT = ""
                    
            #space bar to restart the game
            elif event.key == pygame.K_SPACE :
                ANSWER = random.choice(DICT_ANSWERS)
                GAME_OVER = False
                INPUT = ""
                GUESSES = []
                UNGUESSED = ALPHABET


                
                    
            #regular text input 
            elif len(INPUT) < 5 and not GAME_OVER :
                INPUT = INPUT + event.unicode.upper()