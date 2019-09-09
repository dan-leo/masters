import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import plotter as p
import jupyter as j
import importlib
from sklearn.cluster import KMeans

cc = ['tab:blue', 'tab:green', 'tab:cyan', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:red']
cc_compare = ['tab:orange', 'red']
testl = ['1-16 B', '64-128 B', '256-512 B', 'Echo', 'COPS', 'eDRX', 'PTAU']
uenwl = ['Ublox-MTN', 'Quectel-MTN', 'Ublox-Vodacom', 'Quectel-Vodacom']
nwl = ['MTN', 'Vodacom']
attl = [a for a in p.attdt()]

def lighten_color(color, amount=0.3):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

def plot(mdb, kx, ky, xlabel='', ylabel='', scale=[1,1], invert=[True,False], colour=cc, folder='', K=0):
    global hytest, hyuenw, hyatt, hxtest, hxuenw, hxatt, kkx, kky, xxlabel, yylabel, ffolder, outcounts
    outcounts = 0
    hytest, hyuenw, hyatt = [], [], []
    hxtest, hxuenw, hxatt = [], [], []
    folder = folder + '/' if len(folder) else 'plotter3/'
    ffolder = folder
    kkx, kky = kx, ky
    xxlabel, yylabel = xlabel, ylabel
    # importlib.reload(p)
    # importlib.reload(j)
    fig = plt.figure(figsize=(14, 4))
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    fig2 = plt.figure(figsize=(14, 2))
    ax4 = fig2.add_subplot(131)
    ax5 = fig2.add_subplot(132)
    ax6 = fig2.add_subplot(133)
    for oi in range(2):
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
                                # exclude
                                # print(kx, ky)
                                # print(atd[kx])
                                rex = j.exclude(kx, atd[kx])
                                rey = j.exclude(ky, atd[ky])
                                # print('rex, rey', rex, rey)
                                re = rex * rey
                                atd[kx] = np.array(atd[kx])[re]
                                atd[ky] = np.array(atd[ky])[re]
                                atk = {}
                                if K and len(atd[kx]) and len(atd[ky]) and oi:
                                    # remove duplicates
                                    _, idx = np.unique(atd[ky], return_index=True)
                                    atdkx = atd[kx][np.sort(idx)]
                                    atdky = atd[ky][np.sort(idx)]
                                    data = np.array([atdkx, atdky])
                                    # k-means
                                    kmeans = KMeans(n_clusters=min(K, len(atdky)))
                                    kmeans.fit(data.T)
                                    atk[kx], atk[ky] = kmeans.cluster_centers_.T
                                else:
                                    atk[kx], atk[ky] = atd[kx], atd[ky]

                                # main
                                rx = j.threshold(atk, kx)
                                ry = j.threshold(atk, ky)
                                r = rx * ry
                                x = atk[kx][r]/scale[0]
                                y = atk[ky][r]/scale[1]
                                if ui < 2:
                                    if not oi:
                                        ax1.scatter(x, y, color=lighten_color(cc[ui]))
                                    else:
                                        ax1.scatter(x, y, color=cc[ui], label=uenwl[ui] if not ti and not ai else None)
                                else:
                                    if not oi:
                                        ax2.scatter(x, y, color=lighten_color(cc[ui]))
                                    else:
                                        ax2.scatter(x, y, color=cc[ui], label=uenwl[ui] if not ti and not ai else None)
                                i3 = int(ui/2)
                                if not oi:
                                    ax3.scatter(x, y, color=lighten_color(cc_compare[i3]))
                                else:
                                    ax3.scatter(x, y, color=cc_compare[i3], label=nwl[i3] if not ti and not ai and not ui % 2 else None)
                                # ax1.scatter(x, y, color=cc[ai], label=attl[ai] if not ti and not ui else None)
                                # ax2.scatter(x, y, color=cc[ui], label=uenwl[ui] if not ti and not ai else None)
                                # ax3.scatter(x, y, color=cc[ti], label=testl[ti] if not ui and not ai else None)
                                if y.size:
                                    # hy = np.mean(y)
                                    for hy in y:
                                        hytest[ti].append(hy)
                                        hyuenw[ui].append(hy)
                                        hyatt[ai].append(hy)
                                if x.size:
                                    # hx = np.mean(x)
                                    for hx in x:
                                        hxtest[ti].append(hx)
                                        hxuenw[ui].append(hx)
                                        hxatt[ai].append(hx)
                                
                                # outliers
                                rx = np.invert(rx) if invert[0] else rx==rx
                                ry = np.invert(ry) if invert[1] else ry==ry
                                r = rx * ry
                                x = np.array(atk[kx])[r]/scale[0]
                                y = np.array(atk[ky])[r]/scale[1]
                                outcounts += len(y)
                                ms=80
                                if ui < 2:
                                    ax4.scatter(x, y, color=cc[ui] if oi else lighten_color(cc[ui]), s=ms)
                                else:
                                    ax5.scatter(x, y, color=cc[ui] if oi else lighten_color(cc[ui]), s=ms)
                                ax6.scatter(x, y, color=cc_compare[int(ui/2)] if oi else lighten_color(cc_compare[int(ui/2)]), s=ms)
                                # ax4.scatter(x, y, color=cc[ai], s=ms, alpha=1.0 if oi else 0.15)
                                # ax5.scatter(x, y, color=cc[ui], s=ms, alpha=1.0 if oi else 0.15)
                                # ax6.scatter(x, y, color=cc[ti], s=ms, alpha=1.0 if oi else 0.15)
                            except TypeError as e:
                            # except KeyboardInterrupt as e:
                                print(e, atd[kx])
                        except (KeyError, TypeError) as e:
                            # print(e, kx, ky)
                        # except KeyboardInterrupt as e:
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
    fig.savefig(folder + kx + '_' + ky + '_plot.png')
    fig.savefig(folder + kx + '_' + ky + '_plot.pdf')
    fig2.savefig(folder + kx + '_' + ky + '_outliers.png')
    fig2.savefig(folder + kx + '_' + ky + '_outliers.pdf')
    plt.show()
    print(ti+1, ui+1, ai+1)

def hist(plotx=False, kx='A', ky='B', bins=20):
    global kkx, kky
    hcounts = sum([len(a) for a in hytest])
    print('ky', kky, hcounts, '+', outcounts, '=', hcounts + outcounts)
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
    fig.savefig(ffolder + kky + '_histogram.png')
    fig.savefig(ffolder + kky + '_histogram.pdf')
    plt.show()
    if plotx:
        print('kx', kkx)
        fig2 = plt.figure(figsize=(14, 4))
        ax1 = fig2.add_subplot(131)
        ax2 = fig2.add_subplot(132)
        ax3 = fig2.add_subplot(133)
        ax1.hist(hxatt, stacked=True, bins=bins, label=attl, color=[*cc[:5]*4])
        ax2.hist(hxuenw, stacked=True, bins=bins, label=uenwl, color=cc[:4])
        ax3.hist(hxtest, stacked=True, bins=bins, label=testl, color=cc)
        ax1.set_ylabel('Count')
        ax2.set_xlabel(xxlabel)
        ax1.legend(loc='best')
        ax2.legend(loc='best')
        ax3.legend(loc='best')
        kkx = '_'.join(kkx.split())
        fig2.savefig(ffolder + kkx + '_histogram.png')
        fig2.savefig(ffolder + kkx + '_histogram.pdf')
        plt.show()
    return hcounts, outcounts