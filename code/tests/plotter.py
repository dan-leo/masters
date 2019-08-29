import numpy as np
import matplotlib.pyplot as plt
import jupyter as j
import importlib
import pandas as pd
import seaborn as sns
# importlib.reload(j)
from mpl_toolkits import mplot3d
import copy

import matplotlib.ticker as ticker
import glob

cc = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:blue', 'tab:brown', 'tab:cyan']

def attdt():
    atf = {}
    atten = np.arange(0, 40, 10)
    for at in atten:
        atf[str(at) + ' dB'] = []
    atf['40-110 dB'] = []
    return atf

# manual flatten of array
def flatten(hist):
    flat = []
    for i in range(len(hist)):
        merge = []
        for h in hist[i][0]:
            for v in h:
                merge.append(v)
        flat.append(merge)
    return np.array(flat)

# def db(dirrs, files):
def scatternuator(name, kx, ky, thresh, plotlim, scale, limited, dirrs, files, kz=None, atd=None, scaled=False, log=True, overlay=False, \
    labels=['Ublox', 'Quectel'], legend=True, title='metric', ttype='fade', fig=None, offset=0, colour='tab:blue', fx=5, fy=3, \
    print_outliers=True, bbox=(1.03, 0.97)):
    savefig = fig == None
    attenuator_db = []

    np.set_printoptions(precision=3, suppress=True)
    for di, dirr in enumerate(dirrs):
        ####################### file prep #######################
        atf = attdt()
        atten = np.arange(110, -1, -10)
        # starfolder = 'release/release128/*'
        print(dirr + str(files))
        for starfolder in files:
            subfiles = glob.glob(dirr + starfolder)
            for file in subfiles:
                f = file.split('\\')[-1]
                for atn in atten:
                    if str(atn) in f:
                        # print(atn, file)
                        if atn >= 40:
                            atf['40-110 dB'].append(file)
                        else:
                            atf[str(atn) + ' dB'].append(file)
                        break
                else:
                    print('else', file)
                    atf['40-110 dB'].append(file)

        ####################### database {} prep #######################

        atd = atd if atd else attdt()
        for k in atd:
            if str(type(atd[k])) == "<class 'dict'>":
                # print('len(atd[', k, '])', len(atd[k]), type(atd[k]))
                atd[k] = [atd[k]]
        for k in atf:
            # print(k, atf[k])
            for f in atf[k]:
                try:
                    c = j.csvToDict(f)
                    dp = j.dataProcess(c)
                    atd[k].append(dp)
                except AttributeError as e:
                    print('AttributeError', e, k, type(atd[k]))
                    pass
            atd[k] = j.merge(atd[k])
            # print('atd[k]', len(atd[k]))
        
        atdc = copy.deepcopy(atd)
        attenuator_db.append(atdc)

    if ttype == 'return':
        return atd
# def scatternuator(name, kx, ky, thresh, plotlim, scale, limited, attenuator_db):

    # 4x4 plotter
    fy = fy if overlay else 2*fy
    fx = fx if overlay else 2*fx
    npoints = 0
    # fx = 1
    aka = []
    histy = []
    histx = []
    paxis = []
    z_list = []
    outliers = []
    ecl_list = []
    if not fig:
        fig = plt.figure(figsize=(fx, fy))
    plt.title(title + ' plot')
    cc = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:blue', 'tab:brown']
    cd = ['tab:blue', 'tab:red']
    alphas = [1.0, 0.8, 0.6, 0.5, 0.4, 0.3]
    if overlay:
        if '3d' in ttype:
            ax = fig.add_subplot(111, projection = '3d')
        else:
            # ax = fig.add_subplot(111)
            ax = plt.gca()
    for di, atd in enumerate(attenuator_db):
        # print('attenuator_db', di, [len(a) for a in attenuator_db[di]], [len(attenuator_db[di][k][d]) for k in attenuator_db[di] for d in attenuator_db[di][k]])
        ####################### scatter #######################
        x = []
        y = []
        ka = []
        outlier = []
        if overlay:
            # ax = fig.add_subplot(111, label=labels[di])   
            ax.set_label(labels[di])    
        else:
            ax = fig.add_subplot(2, 2, di + 1)

        # try:
        #     print([len(atd[a][ky]) for a in atd], sum([len(atd[a][b]) for a in atd for b in atd[a]]))
        # except KeyError:
        #     pass
        for i, k in enumerate(atd):
            try:
                xx = np.array(atd[k][kx])
                yy = np.array(atd[k][ky])
                r = xx == xx
                if thresh[0]:
                    r *= xx > thresh[0]
                if thresh[1]:
                    r *= xx < thresh[1]
                r2 = yy == yy
                if thresh[2]:
                    r2 *= yy > thresh[2]
                if thresh[3]:
                    r2 *= yy < thresh[3]
                r *= r2
                if kz:
                    zz = np.array(atd[k][kz])
                    r3 = zz == zz
                    if thresh[4]:
                        r3 *= zz > thresh[4]
                    if thresh[5]:
                        r3 *= zz < thresh[5]
                    r *= r3
                # print(yy)
                if scaled:
                    xx = xx / scale[0]
                xx += offset
                if scaled:
                    yy = yy / scale[1]
                npoints += len(xx[r])
                if ttype == 'fade':
                    ax.scatter(xx[r], yy[r], marker='o', color=cd[di], label=k, alpha=alphas[len(atd)-1-i])
                elif ttype == 'colour':
                    ax.scatter(xx[r], yy[r], marker='o', color=cc[i], label=k, alpha=0.8)
                elif ttype == 'label':
                    ax.scatter(xx[r], yy[r], marker='o', color=colour[di], label=labels[di] if not i else None, alpha=[1.0, 0.8, 0.6, 0.5][di])
                elif ttype == 'single':
                    ax.scatter(xx[r], yy[r], marker='o', color=colour, label=labels[0] if not i else None, alpha=0.8)
                elif ttype == 'ecl':
                    ecl = np.array(atd[k]['ECL'])
                    for xp, yp, e in zip(xx[r], yy[r], ecl[r]):
                        ax.scatter(xp, yp, marker='o', color=cc[int(e)], label=(255 if e == 3 else e) if not e in ecl_list else None, alpha=0.8)
                        ecl_list.append(e)
                elif ttype == 'ecl3d':
                    ecl = np.array(atd[k]['ECL'])
                    for xp, yp, e in zip(xx[r], yy[r], ecl[r]):
                        ax.scatter(xp, yp, e, marker='o', color=cc[int(e)], label=e if not e in ecl_list else None, alpha=0.8)
                        ecl_list.append(e)
                elif ttype == 'plot3d':
                    for xp, yp, zp in zip(xx[r], yy[r], zz[r]):
                        ax.scatter(xp, yp, zp, marker='o', color=colour, label=labels[0] if not labels[0] in z_list else None, alpha=0.8)
                        z_list.append(labels[0])
                    # ax.scatter(xx[r], yy[r], zz[r], marker='o', color=colour, label=labels[0] if not i else None, alpha=0.8)
                x.append(xx[r])
                y.append(yy[r])
                if False in r:
                    o = [xx[np.invert(r)], yy[np.invert(r)]]
                    if print_outliers:
                        print('r', o)
                    outliers.append(o)
                    # print('outliers', outliers)
                ka.append(k)
            except (KeyError, IndexError) as e:
                print('KeyError, IndexError', e, k, atd[k])
        # hist.append([x, y])
        # print('x', len(x))
        # x = sum(x, [])
        # y = sum(y, [])
        histx.append(x)
        histy.append(y)
        # print('outliers', outliers)
        # outliers.append(outlier)
        aka.append(ka)
        # ax = plt.gca()
        paxis.append(ax)
        if log:
            ax.set_yscale('log')
        if limited:
            ax.set_xlim(plotlim[:2])
            ax.set_ylim(plotlim[2:])
        if log:
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
        # ax.legend(bbox_to_anchor=(0.97, 1.15))
        if overlay and legend:
            if bbox:
                ax.legend(bbox_to_anchor=bbox)
            else:
                ax.legend()

    sumx = [len(h) for h in histx[0]]
    sumy = [len(h) for h in histy[0]]
    # print('points', npoints, sum(sumx), sum(sumy), sumx, sumy, len(histx), len(histy))
    if savefig:
        pic = 'plotter/' + name + '_plot'
        plt.savefig(pic + '.png')
        plt.savefig(pic + '.pdf')
    return histx, histy, outliers

def histernator(hist_points, title, labels=None, fy=4, fx=6, bins=20, colour=cc):
    fig = plt.figure(figsize=(fx, fy))
    plt.title(title + ' histogram')
    # ax = fig.add_subplot(111)
    ax = plt.gca()
    print('hist points', hist_points.shape, [len(a) for a in hist_points], 'bins', bins)

    # df.index = pd.Index(aka[hi])
    plt.hist(hist_points, bins=bins, label=labels, stacked=True, color=colour)
    if labels:
        plt.legend()
    # plt.show()
    return hist_points