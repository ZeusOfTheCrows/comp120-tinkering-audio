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

            elif event.key == pygame.K_a:
                sound_effect = sound_effects.MoveSFX('w')
                sound_effect.sound_file.writeframes(
                    sound_effect.package(sound_effect.generate_sound()))
                sound_effect.sound_file.close()

            elif event.key == pygame.K_d:
                sound_effect = sound_effects.MoveSFX('r')
                pygame.mixer.music.load(sound_effect.file_name)
                pygame.mixer.music.play(5, 0.0)

            elif event.key == pygame.K_e:
                sound_effect = sound_effects.MoveSFX('r')
                sound_effect.generate_echo()
                sound_effect.sound_file.close()
