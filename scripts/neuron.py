### All functions for neuron detector analysis

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from skimage import io
import os
import pandas as pd
import seaborn as sns


def get_signal(filename):
    """
    return the images intensity as a function of time from a file
    """
    image = io.imread(filename)
    return image
    # return image.sum(axis=(1,2))



def plot_signal(signal, filename=None, ax=None, **kwargs):
    ax = plt.gca() if ax is None else ax

    if (filename is not None) and ('label' not in kwargs):
        kwargs['label'] = os.path.basename(filename.split('.')[0])

    ax.plot(signal, **kwargs)
    ax.set_xlabel('image')
    ax.set_ylabel('signal')
    ax.legend()
    return ax


def plot_relative_signal(signal, filename=None, ax=None, **kwargs):
    ax = plt.gca() if ax is None else ax

    if (filename is not None) and ('label' not in kwargs):
        kwargs['label'] = os.path.basename(filename.split('.')[0])

    ax.plot(signal/signal.mean(), **kwargs)
    ax.set_xlabel('image')
    ax.set_ylabel('Intensité relative')
    ax.legend()
    return ax


def plot_signal_from_file(filename, list_synchro=[], synchro_limit=1.1, ax=None, **kwargs):
    """
    Just make a plot of the images intensity as a function of time from a file
    """
    signal = get_signal(filename)
    if (signal[10:]/signal[10:].mean()>synchro_limit).any():
        list_synchro.append(filename)

    plot_signal_from_file(filename, ax=ax, **kwargs)
    return ax


def find_events(video, limit=1.1):
    """
    return the number of events above limit and their starting time (image index)
    """
    n = 0
    current_strike = False
    args = []
    m = signal.sum(axis=(1,2)).mean()
    for ii, image in enumerate(signal):
        if image.sum()/m > limit and current_strike is False :
            args.append(ii)
            n += 1
            current_strike = True
        elif image.sum()/m > limit and current_strike:
            current_strike = True
        else:
            current_strike = False
    return n, np.array(args)
