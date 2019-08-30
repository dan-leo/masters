import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import plotter as p
import jupyter as j
import importlib

cc = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:blue', 'tab:brown', 'tab:cyan']

def plot(mdb, kx, ky, scale=[1,1], invert=[True,False], colour=cc):
    global hytest, hyuenw, hyatt, hxtest, hxuenw, hxatt, kkx, kky
    hytest, hyuenw, hyatt = [], [], []
    hxtest, hxuenw, hxatt = [], [], []
    kkx, kky = kx, ky
    importlib.reload(p)
    importlib.reload(j)
    fig = plt.figure(figsize=(14, 4))
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    fig = plt.figure(figsize=(14, 2))
    ax4 = fig.add_subplot(131)
    ax5 = fig.add_subplot(132)
    ax6 = fig.add_subplot(133)
    for ti, test in enumerate(mdb):
        hytest.append([])
        hxtest.append([])
        for ui, uenw in enumerate(test):
            if not ti:
                hyuenw.append([])
                hxuenw.append([])
            for ai, att in enumerate(uenw):
                if not ti:
                    hyatt.append([])
                    hxatt.append([])
                for atd in [uenw[att]]:
                    try:
                        try:
                            # main
                            rx = j.threshold(atd, kx)
                            ry = j.threshold(atd, ky)
                            r = rx * ry
                            x = np.array(atd[kx][r])/scale[0]
                            y = np.array(atd[ky][r])/scale[1]
                            ax1.scatter(x, y, color=cc[ai])
                            ax2.scatter(x, y, color=cc[ui])
                            ax3.scatter(x, y, color=cc[ti])
                            if y.size:
                                hy = np.mean(y)
                                hytest[ti].append(hy)
                                hyuenw[ui].append(hy)
                                hyatt[ai].append(hy)
                            if x.size:
                                hx = np.mean(x)
                                hxtest[ti].append(hx)
                                hxuenw[ui].append(hx)
                                hxatt[ai].append(hx)
                            
                            # outliers
                            rx = np.invert(rx) if invert[0] else rx
                            ry = np.invert(ry) if invert[1] else ry
                            r = rx * ry
                            x = np.array(atd[kx][r])/scale[0]
                            y = np.array(atd[ky][r])/scale[1]
                            ms=80
                            ax4.scatter(x, y, color=cc[ai], s=ms)
                            ax5.scatter(x, y, color=cc[ui], s=ms)
                            ax6.scatter(x, y, color=cc[ti], s=ms)
                        except TypeError as e:
                            print(e, atd[kx])
                    except (KeyError, TypeError) as e:
                        pass
    plt.show()
    print(ti+1, ui+1, ai+1)

def hist(plotx=False, kx='A', ky='B'):
    print('ky', kky)
    fig = plt.figure(figsize=(14, 4))
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    ax1.hist(hyatt, stacked=True)
    ax2.hist(hyuenw, stacked=True)
    ax3.hist(hytest, stacked=True)
    plt.show()
    if plotx:
        print('kx', kkx)
        fig = plt.figure(figsize=(14, 4))
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)
        ax1.hist(hxatt, stacked=True)
        ax2.hist(hxuenw, stacked=True)
        ax3.hist(hxtest, stacked=True)
        plt.show()