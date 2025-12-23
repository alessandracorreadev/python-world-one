import pygame
import time

pygame.init() # intialize pygame
pygame.mixer.init()
pygame.mixer.music.load("only_me_audio_yt_lib.mp3") # load the mp3
pygame.mixer.music.play(-1) # play the mp3
while pygame.mixer.music.get_busy(): # plays the mp3  in infinete loop
    time.sleep(1)