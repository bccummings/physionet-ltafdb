import sys
import argparse
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def argument_parser(argv):
    '''
    Parse input from the command line
    '''

    parser = argparse.ArgumentParser( description = "Script to visualize data from the Physionet Long Term Atrial Fibrilation Database")

    parser.add_argument('--recordname',
                        help='name of record, with path included if necessary',
                        type=str,
                        required=True)

    parser.add_argument('--samplerate',
                        help='sampling rate as an integer in Hz',
                        type=int,
                        required=False,
                        default=128)

    parser.add_argument('--markertype',
                        help='which markers to plot. N, |, and/or T.',
                        type=str,
                        nargs='*',
                        required=False,
                        default=None)

    return parser.parse_args()

def read_data(args):
    '''
    Read input datafile
    '''
    data = pd.read_csv(args.recordname+'.data', sep='\t', header=None)
    t = [i/args.samplerate for i in range(len(data))]

    return (data, t)

def read_annotations(args):
    '''
    Read input annotations file
    '''
    anns = pd.read_csv(args.recordname+'.ann',
                        delim_whitespace=True,
                        header=None,
                        usecols=[2,3],
                        names=['sample', 'marker'])

    return anns


def plot_waveforms(data, anns, t):
    [fig, ax] = plt.subplots(nrows=2, ncols=1, sharex=True)

    ax[0].plot(t, data[1])
    ax[1].plot(t, data[2])

    if args.markertype:
        for m in args.markertype:
            anns_extracted = anns.loc[anns.marker==m]

            marker_t = [i/args.samplerate for i in anns_extracted['sample']]

            ax[0].plot(marker_t, data[1][anns_extracted['sample']], 'o')
            ax[1].plot(marker_t, data[2][anns_extracted['sample']], 'o')

    plt.show()

if __name__ == '__main__':
    args = argument_parser(sys.argv[1:])
    (data, t) = read_data(args)
    anns = read_annotations(args)
    plot_waveforms(data, anns, t)
