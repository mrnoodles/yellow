__author__ = 'New'

import os
import pygame

pygame.init()

real_cries = [None]

bgm = [
    "101-opening.wav",
    "102-palette-town-theme.wav",
    "103-professor-oak.wav",
    "104-oak-research-lab.wav",
    "105-rival-appears.wav",
    "106-the-road-to-viridian-city-from-palette.wav",
    "107-battle-vs-wild-pokemon-.wav",
    "108-victory-vs-wild-pokemon-.wav",
    "109-pewter-city-s-theme.wav",
    "110-pokemon-center.wav",
    "111-pokemon-recovery.wav",
    "112-viridian-forest.wav",
    "113-guidepost.wav",
    "114-trainer-appears-girl-chapter-.wav",
    "115-battle-vs-trainer-.wav",
    "116-victory-vs-trainer-.wav",
    "117-mt.-moon-cave.wav",
    "118-the-road-to-cerulean-from-mt.-moon.wav",
    "119-cerulean-city-s-theme.wav",
    "120-pokemon-gym.wav",
    "121-to-bill-s-lighthouse-from-cerulean.wav",
    "122-jigglypuff-s-song.wav",
    "123-vermillion-city-s-theme.wav",
    "124-codename-st.-anne.wav",
    "125-the-road-to-lavender-town-from-vermillion.wav",
    "126-pokemon-whistle.wav",
    "127-trainer-appears-boy-chapter-.wav",
    "128-battle-vs-gym-leader-.wav",
    "129-victory-vs-gym-leader-.wav",
    "130-cycling.wav",
    "131-lavender-town-s-theme.wav",
    "132-pokemon-tower.wav",
    "133-celadon-city.wav",
    "134-casino.wav",
    "135-trainer-appears-bad-guy-chapter-.wav",
    "136-team-rocket-hideout.wav",
    "137-sylph-company.wav",
    "138-ocean.wav",
    "139-cinnabar-islands-theme.wav",
    "140-pokemon-mansion.wav",
    "141-evolution.wav",
    "142-the-final-road.wav",
    "143-last-battle-vs-rival-.wav",
    "144-into-the-palace.wav",
    "145-ending.wav"
]


def cry_filename(id):
    kipcrin = str(id)

    if len(kipcrin) == 1:
        kipcrin = "00" + kipcrin

    if len(kipcrin) == 2:
        kipcrin = "0" + kipcrin

    #return os.path.abspath("cries\\" + kipcrin + ".ogg")

    return "sound/cries/" + kipcrin + ".wav"


def bgm_filename(id):
    print "playing:", os.path.abspath("../sound/bgm/" + bgm[id][:-3] + "ogg")
    return "../sound/bgm/" + bgm[id][:-3] + "ogg"


def initialize():

    for cry in range(1, 151):

        kipcrin = cry_filename(cry)
        icrievrtim = pygame.mixer.Sound(kipcrin)

        real_cries.append(icrievrtim)
