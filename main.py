import pygame
import sound_effects

pygame.init()
pygame.display.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                from sys import exit
                exit()

                # generates tone to be played back with D
            elif event.key == pygame.K_a:
                sound_effect = sound_effects.MoveSFX('w')
                sound_effect.sound_file.writeframes(
                    sound_effect.package(sound_effect.generate_sound()))
                sound_effect.sound_file.close()

                # plays currently loaded tone
            elif event.key == pygame.K_d:
                sound_effect = sound_effects.MoveSFX('r')
                pygame.mixer.music.load(sound_effect.file_name)
                pygame.mixer.music.play(1, 0.0)

                # generate echo (not working)
            elif event.key == pygame.K_e:
                sound_effect = sound_effects.MoveSFX('r')
                sound_effect.generate_echo()
                sound_effect.sound_file.close()

                # allows entering manual frequency (using terminal)
            elif event.key == pygame.K_f:
                freq = input('Please enter a frequency:')
                sound_effect = sound_effects.MoveSFX('w', freq)
                sound_effect.sound_file.writeframes(
                    sound_effect.package(sound_effect.generate_sound()))
                sound_effect.sound_file.close()
