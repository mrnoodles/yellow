__author__ = 'New'

import time
import pygame
pygame.init()
pygame.mixer.init()
import sound.sound_bank

sound.sound_bank.initialize()

#print sound.sound_bank.real_cries

window = pygame.display.set_mode((100, 100))

for cry in range(1, 151):
    sound.sound_bank.real_cries[cry].play()
    time.sleep(3)
