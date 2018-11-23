import wave
import math
import struct


class SFX:

    @staticmethod
    def read_wav(filename):

        """Function from Michael's slack message"""

        noise_in = wave.open(filename, 'rb')

        channels = noise_in.getnchannels()
        sample_rate = noise_in.getframerate()
        sample_width = noise_in.getsampwidth()
        frame_count = noise_in.getnframes()

        raw_audio = noise_in.readframes(frame_count)
        noise_in.close()

        total_samples = frame_count * channels

        if sample_width == 1:
            fmt = "%ib" % total_samples
        elif sample_width == 2:
            fmt = "%ih" % total_samples
        else:
            raise ValueError("Not 8 or 16 bit")

        audio_data = struct.unpack(fmt, raw_audio)
        del raw_audio

        return list(audio_data)

    # Will be loaded from helper.py
    compressionType = "NONE"
    compressionName = "No compression"
    maxValue = 32767.0
    channels = 1  # number of channels
    sample_width = 2
    sample_rate = 44100

    def __init__(self, mode, frequency=300):

        self.length = 6  # in seconds
        self.file_name = 'output.wav'  # whoosh sourced from: http://soundbible.com
        self.samples = SFX.sample_rate * self.length
        self.frequency = float(frequency)
        self.volume = 1
        self.sound_file = wave.open(self.file_name, mode)
        if mode == 'w':
            self.sound_file.setparams((SFX.channels,
                                       self.sample_width,
                                       self.sample_rate,
                                       self.samples,
                                       SFX.compressionType,
                                       self.compressionName))

    @staticmethod
    def generate_sin_wave(position, frequency, amplitude):
        """generates simple sine wave"""
        return math.sin(
                2.0 * math.pi
                * frequency
                * float((position / SFX.sample_rate)))\
                * SFX.maxValue * amplitude

    @staticmethod
    def package(tone_list):
        """packages values using struct.pack"""
        values = []
        for i in range(0, len(tone_list)):
            packed_value = struct.pack('h', int(tone_list[i]))
            values.append(packed_value)

        print('Finished packaging')

        return b''.join(values)

    def generate_sound(self):
        """generates the sound to be played"""
        values = []
        for i in range(0, self.samples):
            value = SFX.generate_sin_wave(i, self.frequency, 0.5)

            values.append(value)

        return values


class MoveSFX(SFX):
    """
    Sound effects for player move. Extends SFX class purely for gen_sin_wave()
    and package()
    """

    def generate_echo(self, delay=1000):
        length = self.sound_file.getnframes()
        self.sound_file.close()
        for i in range(0, length):
            print(i)


class AttackSFX(SFX):
    """
    Sound effects for player/enemy attack - not yet implemented
    """

    def generate_sound(self):
        pass

    def play_sound(self):
        pass

