import wave
import math
import struct


class SFX:

    compressionType = "NONE"
    compressionName = "No compression"
    maxValue = 32767.0
    channels = 1  # number of channels
    sample_width = 2
    sample_rate = 44100

    def __init__(self, mode):

        self.length = 6  # in seconds
        self.file_name = 'Whoosh.wav'  # source: http://soundbible.com
        self.samples = SFX.sample_rate * self.length
        self.frequency = 350
        self.volume = 1
        self.sound_file = wave.open(self.file_name, mode)
        if mode == 'w':
            self.sound_file.setparams((SFX.channels, self.sample_width, self.sample_rate, self.samples, SFX.compressionType, self.compressionName))

    @staticmethod
    def generate_sin_wave(position, frequency, amplitude):

        return math.sin(
                2.0 * math.pi
                * frequency
                * float((position / SFX.sample_rate)))\
                * SFX.maxValue * amplitude

    @staticmethod
    def package(tone_list):
        values = []

        for i in range(0, len(tone_list)):
            packed_value = struct.pack('h', int(tone_list[i]))
            values.append(packed_value)

        print('Finished packaging')

        return b''.join(values)

    def generate_sound(self):

        values = []
        for i in range(0, self.samples):
            value = SFX.generate_sin_wave(i, self.frequency, 0.5)

            values.append(value)

        return values

    def play_sound(self):
        pass


class MoveSFX(SFX):
    """
    def generate_sound(self):
        pass

    def play_sound(self):
        pass
    """

    def generate_echo(self, delay=1000):
        length = self.sound_file.getnframes()
        self.sound_file.close()
        for i in range(0, length):
            print(i)


class AttackSFX(SFX):

    def generate_sound(self):
        pass

    def play_sound(self):
        pass

