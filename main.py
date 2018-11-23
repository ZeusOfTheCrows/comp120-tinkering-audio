
"""
CONTRACT 1 - NOT MUCH RIGHT NOW, IN THE FUTURE, WALKING/ATTACKING SOUND EFFECTS
TAKEN OWNERSHIP BY CYRUS
WITH HELP FROM FELLOW TEAM MEMBERS: ADRIAN< PAUL AND JAKOB
"""

import pygame
import sound_effects

pygame.init()
pygame.display.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))

pureTone = sound_effects.SFX('output', 'w')
whoosh = sound_effects.MoveSFX('whoosh')
# (whoosh sourced from: http://soundbible.com)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                from sys import exit
                exit()

                # generates tone to be played back with D
            elif event.key == pygame.K_a:
                pureTone.sound_file.writeframes(pureTone.generate_sound())
                pureTone.sound_file.close()

                # plays currently loaded tone
            elif event.key == pygame.K_d:
                try:
                    pygame.mixer.music.load(pureTone.file_name)
                    pygame.mixer.music.play(1, 0.0)
                except pygame.error:
                    print('Please generate tone with "A" first')

                # generate echo (not working)
            elif event.key == pygame.K_e:
                whoosh.generate_echo()
                pygame.mixer.music.load('whoosh.wav')

                # allows entering manual frequency (using terminal)
            elif event.key == pygame.K_f:
                freq = input('Please enter a frequency:')
                pureTone.sound_file.writeframes(pureTone.generate_sound())
                pureTone.sound_file.close()
