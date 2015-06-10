__author__ = 'New'

import os
import pygame

pygame.init()

real_cries = [None]

def filename_getter(id):
    kipcrin = str(id)

    if len(kipcrin) == 1:
        kipcrin = "00" + kipcrin

    if len(kipcrin) == 2:
        kipcrin = "0" + kipcrin

    return os.path.abspath("cries/" + kipcrin + ".mp3")


def initialize():

    for cry in range(1, 151):

        kipcrin = filename_getter(cry)
        icrievrtim = pygame.mixer.Sound(kipcrin)

        real_cries.append(icrievrtim)
