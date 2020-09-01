import numpy as np
from scipy import fft
import matplotlib.pyplot as plt
from pydub import AudioSegment

SAMPLE_RATE = 44100 # standard mp3 sample rate, Hz
PLOT_XLIM = (0, 5)
PLOT_YLIM = (-2*10**8, 2*10**8)

def read_as_array(fname, ftype="mp3", mono=False):
    track = AudioSegment.from_file(fname, ftype)

    if mono:
        track = track.setChannels(1)

    return np.array(track.get_array_of_samples())

def fastFourier(samples, srate=SAMPLE_RATE):
    yf = np.abs(fft(samples))
    freq = fft.fftfreq(samples.shape[-1]) * srate

    return np.vstack((freq, yf))

def plot_track(samples, outFunct=plt.show):
    fourier = fastFourier(samples)

    #plt.xlim(*PLOT_XLIM)
    #plt.ylim(*PLOT_YLIM)
    xs = fourier[0,:]
    ys = fourier[1,:]

    plt.plot(xs, ys)
    outFunct()
    #plt.savefig("fft.png")
