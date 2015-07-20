__author__ = 'New'

import time
import pygame

#pygame.mixer.pre_init(44100,-16,2, 1024 * 3)
pygame.init()
from sound import sound_bank


window = pygame.display.set_mode((100, 100))


sound_bank.initialize()

for cry in range(1, 151):
    sound_bank.real_cries[cry].play()

    pygame.time.Clock().tick(1)
    #time.sleep(3)
