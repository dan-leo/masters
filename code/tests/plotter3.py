import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import plotter as p
import jupyter as j
import importlib

cc = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:blue', 'tab:brown', 'tab:cyan']
testl = ['1-16 B', '64-128 B', '256-512 B', 'Echo', 'COPS', 'eDRX', 'PTAU']
uenwl = ['Ublox ZTE', 'Quectel ZTE', 'Ublox Nokia', 'Quectel Nokia']
attl = [a for a in p.attdt()]

def plot(mdb, kx, ky, xlabel='', ylabel='', scale=[1,1], invert=[True,False], colour=cc):
    global hytest, hyuenw, hyatt, hxtest, hxuenw, hxatt, kkx, kky, xxlabel, yylabel
    hytest, hyuenw, hyatt = [], [], []
    hxtest, hxuenw, hxatt = [], [], []
    kkx, kky = kx, ky
    xxlabel, yylabel = xlabel, ylabel
    importlib.reload(p)
    importlib.reload(j)
    fig = plt.figure(figsize=(14, 4))
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    fig2 = plt.figure(figsize=(14, 2))
    ax4 = fig2.add_subplot(131)
    ax5 = fig2.add_subplot(132)
    ax6 = fig2.add_subplot(133)
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
                            ax1.scatter(x, y, color=cc[ai], label=attl[ai] if not ti and not ui else None)
                            ax2.scatter(x, y, color=cc[ui], label=uenwl[ui] if not ti and not ai else None)
                            ax3.scatter(x, y, color=cc[ti], label=testl[ti] if not ui and not ai else None)
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
    ax1.set_ylabel(ylabel)
    ax2.set_xlabel(xlabel)
    ax4.set_ylabel(ylabel)
    ax5.set_xlabel(xlabel)
    ax1.legend(loc='best')
    ax2.legend(loc='best')
    ax3.legend(loc='best')
    kx = '_'.join(kx.split())
    ky = '_'.join(ky.split())
    fig.savefig('plotter3/' + kx + '_' + ky + '_plot.png')
    fig.savefig('plotter3/' + kx + '_' + ky + '_plot.pdf')
    fig2.savefig('plotter3/' + kx + '_' + ky + '_outliers.png')
    fig2.savefig('plotter3/' + kx + '_' + ky + '_outliers.pdf')
    plt.show()
    print(ti+1, ui+1, ai+1)

def hist(plotx=False, kx='A', ky='B', bins=20):
    global kkx, kky
    print('ky', kky)
    fig = plt.figure(figsize=(14, 4))
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    ax1.hist(hyatt, stacked=True, bins=bins, label=attl, color=[*cc[:5]*4])
    ax2.hist(hyuenw, stacked=True, bins=bins, label=uenwl, color=cc[:4])
    ax3.hist(hytest, stacked=True, bins=bins, label=testl, color=cc)
    ax1.set_ylabel('Count')
    ax2.set_xlabel(yylabel)
    ax1.legend(loc='best')
    ax2.legend(loc='best')
    ax3.legend(loc='best')
    kky = '_'.join(kky.split())
    plt.savefig('plotter3/' + kky + '_histogram.png')
    plt.savefig('plotter3/' + kky + '_histogram.pdf')
    plt.show()
    if plotx:
        print('kx', kkx)
        fig = plt.figure(figsize=(14, 4))
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)
        ax1.hist(hxatt, stacked=True, bins=bins, label=attl, color=[*cc[:5]*4])
        ax2.hist(hxuenw, stacked=True, bins=bins, label=uenwl, color=cc[:4])
        ax3.hist(hxtest, stacked=True, bins=bins, label=testl, color=cc)
        ax1.set_ylabel('Count')
        ax2.set_xlabel(xxlabel)
        ax1.legend(loc='best')
        ax2.legend(loc='best')
        ax3.legend(loc='best')
        kkx = '_'.join(kkx.split())
        plt.savefig('plotter3/' + kkx + '_histogram.png')
        plt.savefig('plotter3/' + kkx + '_histogram.pdf')
        plt.show()