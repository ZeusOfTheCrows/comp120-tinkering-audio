import wave
import math
import struct


def generate_sin_wave(position, frequency, amplitude):
    """
    ___________________________________________________________________________
    Generates the nth number of a simple sine wave.
    :param position: current frame of sound list
    :param frequency: the frequency of the sound
    :param amplitude: the amplitude of the sound
    :return: sin(current frame of sound list)
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    """

    return math.sin(
            2.0 * math.pi
            * frequency
            * float((position / SFX.sample_rate)))\
            * SFX.maxValue * amplitude


def package(tone_list):
    """
    ___________________________________________________________________________
    Packages values using struct.pack.
    :param tone_list: list of values in pure_tone
    :return: packaged tone list

    """

    values = []
    for i in range(0, len(tone_list)):
        packed_value = struct.pack('h', int(tone_list[i]))
        values.append(packed_value)

    print('Finished packaging')

    return b''.join(values)


def read_wav(filename):
    """
    ___________________________________________________________________________
    Function from Michael's slack message:
    Reads wav file and converts to list of manipulatable values.
    :param filename: file to be loaded
    :return: list of audio values
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    """

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


class SFX:

    """
    ___________________________________________________________________________
    Class containing assorted sound effects
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    """

    # Will be loaded from helper.py
    compressionType = "NONE"
    compressionName = "No compression"
    maxValue = 32767.0
    channels = 1  # number of channels
    sample_width = 2
    sample_rate = 44100

    def __init__(self, filename, mode='w', frequency=300):
        """
        _______________________________________________________________________
        Sets necessary variables for sound generation
        :param filename: name of output file
        :param mode: read or write mode (must be r, w, rb or wb - w by default)
        :param frequency: frequency for the generated tone (300 by default)
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """

        self.length = 6  # in seconds
        self.file_name = filename + '.wav'
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

    def generate_sound(self):
        """
        _______________________________________________________________________
        Generates the sound to be played
        :return: packaged pure tone
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """

        values = []
        for i in range(0, self.samples):
            value = generate_sin_wave(i, self.frequency, 0.5)
            values.append(value)

        return package(values)


class MoveSFX:

    """
    ___________________________________________________________________________
    Sound effects for player move. Needs a little extra code to work.
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    """

    def __init__(self, filename):
        """
        _______________________________________________________________________
        Reads the specified file for editing - not completed
        :param filename: name of input file
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """
        read_wav(filename)

        self.length = 6  # in seconds
        self.file_name = filename + '.wav'
        self.samples = SFX.sample_rate * self.length
        self.frequency = 300
        self.volume = 1
        self.sound_file = wave.open(self.file_name, r)

    def generate_echo(self, delay=1000):
        """
        _______________________________________________________________________
        :param delay:
        :return:
        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """

        length = self.sound_file.getnframes()
        self.sound_file.close()
        for i in range(0, length):
            print(i)


class AttackSFX(SFX):

    """
    ___________________________________________________________________________
    Sound effects for player/enemy attack - not yet implemented.
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    """

    def generate_sound(self):
        pass

    def play_sound(self):
        pass

