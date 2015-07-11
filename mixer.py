__author__ = 'user'

import pygame
pygame.init()
from sound import sound_bank
sound_bank.initialize()

#Variables
background_playback = False
vol_adj = 0


#Variables
background_playback = False
vol_adj = 0

#Constants
BEEP_VOLUME = 0.5
VOL_ADJUSTER = 0.20


#Manual Channels
BACKGROUND = pygame.mixer.find_channel()

#Manual Adjustments
#BEEP.set_volume(BEEP_VOLUME)


def play_bgm(id):
    bgm = pygame.mixer.Sound(sound_bank.bgm_filename(id))
    BACKGROUND.play(bgm, -1)


def change_volume(Dir, Target=BACKGROUND):
    """For sound adjustment"""
    volume = Target.get_volume()

    if Dir == "UP":
        if (volume+VOL_ADJUSTER)<=1:
            Target.set_volume(volume+VOL_ADJUSTER)
    if Dir == "DOWN":
        if (volume-VOL_ADJUSTER)>=0:
            Target.set_volume(volume-VOL_ADJUSTER)


def increase_volume(Target=BACKGROUND):
    change_volume("UP")


def decrease_volume(Target=BACKGROUND):
    change_volume("DOWN")


def switch_background_music():
    """Switch background music on or off"""
    global background_playback
    if background_playback:
        BACKGROUND.pause()
        background_playback = False
    else:
        BACKGROUND.unpause()
        background_playback = True
