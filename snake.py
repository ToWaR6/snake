import pygame
from pygame import *
import random

from constants import *

def new_apple(snake):
    apple = (random.randint(0,max_x-1), random.randint(0,max_y-1))
    while apple in snake:
        apple = (random.randint(0,max_x-1), random.randint(0,max_y-1))
    return apple

def print_again(screen):
    screen.fill(0)
    for pixel in text_again + text_YN:
        screen.fill(-1, (pixel[1]*case_size,pixel[0]*case_size,case_size,case_size))
    display.flip()

def game():
    game = True
    while game:
        snake = [(0,0), (0,1), (0,2)]
        head = snake[-1]
        direction = (0,1)

        apple = new_apple(snake)

        while (0 <= head[0] < max_x) and (0 <= head[1] < max_y) and (snake.count(head) == 1):
            # get keydown / set direction
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN: 
                    if event.key == K_LEFT and direction != (1,0):
                        direction = (-1,0)
                        break
                    elif event.key == K_RIGHT and direction != (-1,0):
                        direction = (1,0)
                        break
                    elif event.key == K_UP and direction != (0,1):
                        direction = (0,-1)
                        break
                    elif event.key == K_DOWN and direction != (0,-1):
                        direction = (0,1)
                        break

            snake += [(head[0]+direction[0],head[1]+direction[1])]

            if head != apple:
                del snake[0]
            else:
                apple = new_apple(snake)

            screen.fill(0)
            for i in snake+[apple]:
                screen.fill(-1, (i[0]*case_size,i[1]*case_size,case_size,case_size))
            display.flip()

            head = snake[-1]
            
            events.clear()
            time.wait(100)
        
        print_again(screen)
        answer = False
        while not answer:
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == K_y:
                        answer = True
                        game = True
                        break
                    if event.key == K_n:
                        answer = True
                        game = False
                        print("Bye !")
                        break

pygame.init()

max_x, max_y = 25, 25
case_size = 20

screen = display.set_mode((max_x*case_size,max_y*case_size))

game()

pygame.quit()