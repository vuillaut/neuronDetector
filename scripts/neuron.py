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


def print_stats(df):
    """
    Print stats from a DataFrame and create a summary DataFrame that is returned
    """
    print("{} different experiments".format(len(set(df.experiment))))
    print("{} detected neurons in total".format(len(df)))
    print("{:.2f} neurons per experiment on average".format(len(df)/len(set(df.experiment))))

    stat_df = pd.DataFrame()

    print("")
    exps = set(df.experiment)
    divs = []
    for exp in exps:
        div = exp[exp.lower().find("div"):exp.lower().find("div")+5]
        div = div.replace('_', '')
        if div not in divs:
            divs.append(div)

    stats_df = pd.DataFrame(np.zeros((len(divs), 3)),
                            columns=['nb_exp', 'nb_neur','nb_neur/nb_exp'],
                            index=np.sort(divs))

    for d in np.sort(divs):
        nexp = len([exp for exp in exps if d in exp])
        nneur = len(df[df['experiment'].str.contains(d)])
        print("{}:".format(d))
        print("{} experiments\n{} neurons\n{:.2f} neurons per exp\n".format(nexp, nneur, nneur/nexp))
        stats_df['nb_exp'][d] = nexp
        stats_df['nb_neur'][d] = nneur
        stats_df['nb_neur/nb_exp'][d] = nneur/nexp

    return stats_df



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
    m = video.sum(axis=(1,2)).mean()
    for ii, image in enumerate(video):
        if image.sum()/m > limit and current_strike is False :
            args.append(ii)
            n += 1
            current_strike = True
        elif image.sum()/m > limit and current_strike:
            current_strike = True
        else:
            current_strike = False
    return n, np.array(args)


def get_peak_hist(df, exp=None):
    if exp is None:
        mask = np.ones(len(df), dtype=bool)
    else:
        mask = df.experiment==exp
    return np.histogram(df[mask].Z, bins=np.linspace(10,305,30))[0]
