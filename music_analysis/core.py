import numpy as np
from scipy import fft
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from pydub import AudioSegment

SAMPLE_FREQ = 44100 # standard mp3 sample rate, Hz
PLOT_XLIM = (0, 5)
PLOT_YLIM = (0, 3*10**8)

def read_as_array(fname, ftype="mp3", mono=False):
    track = AudioSegment.from_file(fname, ftype)

    if mono:
        track = track.setChannels(1)

    return np.array(track.get_array_of_samples())

def fast_fourier(samples, sfreq=SAMPLE_FREQ):
    num_samples = samples.shape[-1]
    intensities = np.abs(fft(samples)[0:num_samples//2])
    freqs = np.linspace(0.0, sfreq/2.0, num_samples//2)

    return np.vstack((freqs, intensities))

def get_peaks(fourier):
# TODO: implement threshold for peak finding
    intensities = fourier[1,:]
    peaks, _ =  find_peaks(intensities)

    return np.vstack((fourier[0,:][peaks], intensities[peaks]))

def plot_fourier(fourier, peaks=False):

    plt.xlim(*PLOT_XLIM)
    plt.ylim(*PLOT_YLIM)
    xs = fourier[0,:]
    ys = fourier[1,:]
    peaks = get_peaks(fourier)

    plt.plot(xs, ys)
    plt.plot(peaks[0,:], peaks[1,:], 'x')
    plt.show()
