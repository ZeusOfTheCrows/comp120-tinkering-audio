import pygame
import sound_effects

pygame.init()
pygame.display.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))

sound_effect = sound_effects.SFX()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                from sys import exit
                exit()
            elif event.key == pygame.K_a:
                sound_effect.sound_file.writeframes(
                    sound_effect.package(sound_effect.generate_sound()))
                sound_effect.sound_file.close()
            elif event.key == pygame.K_s:
                sound = pygame.sndarray.make_sound(sound_effect.package(sound_effect.generate_sound()))
                sound.play(1)
                sound.stop()
            elif event.key == pygame.K_d:
                pygame.mixer.music.load('output.wav')
                pygame.mixer.music.play(5, 0.0)


# vv Not mine!! vv

import numpy
import scipy.signal

sample_rate = 44100

def sine_wave(hz, peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    return numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)