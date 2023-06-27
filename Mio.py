import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init() 
pygame.display.set_caption("Rodro Jogo")
BG_color = (250, 250, 250)
WIDTH, HEIGHT = 1000 , 800
FPS = 144
Player_velocity = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))



def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    #get_rect? and x,y?
    _,_, width, height = image.get_rect()
    #why a list?
    tiles = []
    
    #When i highligth the word width in lowercase this highligth the word in uppercase toooooooooooo
    #range??
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)
                        
    return tiles, image


    
# def siempre lleva el self pero solo cuando es una clase
def main(window):
    
    clock = pygame.time.Clock()
    run = True 
    
    #Why 2 variables
    background, bg_image = get_background("Blue.png")
    
    while run:
        #clock.tick para controlar FPS!
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                run = False
                break
            
    pygame.quit()
    quit()
    

            
if __name__ == "__main__":
     main(window)
            