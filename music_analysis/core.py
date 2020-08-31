import numpy as np
from pydub import AudioSegment

SAMPLE_RATE = 44100 # standard mp3 sample rate, Hz

def read_as_array(fname, ftype="mp3", mono=False):
    track = AudioSegment.from_file(fname, ftype)

    if mono:
        track = track.setChannels(1)

    return np.array(track.get_array_of_samples())
