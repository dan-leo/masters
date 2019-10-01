import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import plotter as p
import jupyter as j
import importlib
import matplotlib.colors as mc
import colorsys
from sklearn.cluster import KMeans
from matplotlib.offsetbox import AnchoredText
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

cc_compare = [(237/255, 189/255, 0), 'red']
ccui = ['tab:cyan', 'tab:green', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:red']
cc = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:blue', 'tab:brown', 'tab:cyan']
testl = ['1-16 B', '64-128 B', '256-512 B', 'Echo', 'COPS', 'eDRX', 'PTAU']
uenwl = ['Ublox-MTN', 'Quectel-MTN', 'Ublox-Vodacom', 'Quectel-Vodacom']
attl = [a for a in p.attdt()]

def lc(color, amount=0.4):
    return lighten_color(color, amount)

def lighten_color(color, amount):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    # import matplotlib.colors as mc
    # import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


def plot(mdb, kx, ky, xlabel='', ylabel='', scale=[1,1], invert=[True,False], colour=cc, folder='', K=0, numerator=[None, None], testl=testl, 
        joburg=False, log=False, loc='upper right', thresh=None, bbox=(1.05, 1.12)):
    global hytest, hyuenw, hyatt, hxtest, hxuenw, hxatt, kkx, kky, xxlabel, yylabel, ffolder, outcounts, ally
    outcounts = acounts = oiutcounts = 0
    nwl = ['MTN-Ericsson', 'Vodacom-Huawei'] if joburg else ['MTN-ZTE', 'Vodacom-Nokia']
    hytest, hyuenw, hyatt = [], [], []
    hxtest, hxuenw, hxatt = [], [], []
    ecl_list = []
    ecl_listo = []
    ally = []
    folder = folder + '/' if len(folder) else 'plotter3/'
    ffolder = folder
    kkx, kky = kx, ky
    xxlabel, yylabel = xlabel, ylabel
    fig, axp = plt.subplots(3, 3, figsize=(12, 12), sharey=False)
    fig2, axo = plt.subplots(3, 3, figsize=(12, 7), sharey=False)
    for oi in range(2):
        for ti, test in enumerate(mdb):
            if oi:
                hytest.append([])
                hxtest.append([])
            for ui, uenw in enumerate(test):
                if not ti and oi:
                    ally.append([])
                    hyuenw.append([])
                    hxuenw.append([])
                for ai, att in enumerate(uenw):
                    if not ti and oi:
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
                                atd['ECL'] = np.array(atd['ECL'])[re]
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
                                    atk['ECL'] = atd['ECL']

                                # main
                                rx = j.threshold(atk, kx)
                                ry = j.threshold(atk, ky, thresh)
                                sirange = 1 if log else 2
                                for si in range(sirange):
                                    if si:
                                        ax = axo
                                        rx = np.invert(rx) if invert[0] else rx==rx
                                        ry = np.invert(ry) if invert[1] else ry==ry
                                    else:
                                        ax = axp
                                    if log:
                                        r = atk[kx] == atk[kx]
                                    else:
                                        r = rx * ry
                                    x = atk[kx][r]/scale[0]
                                    y = atk[ky][r]/scale[1]
                                    if numerator[0]:
                                        x = numerator[0]/x
                                    if numerator[1]:
                                        y = numerator[1]/y
                                    # axp[0][0].scatter(x, y, color=cc[ui] if oi else lc(cc[ui]), label=uenwl[ui] if not ti and not ai and oi else None)
                                    # axp[1][0].scatter(x, y, color=cc[ai] if oi else lc(cc[ai]), label=attl[ai] if not ti and not ui and oi else None)
                                    # axp[2][0].scatter(x, y, color=cc[ti] if oi else lc(cc[ti]), label=testl[ti] if not ui and not ai and oi else None)

                                    if ui < 2:
                                        ax[0][0].scatter(x, y, color=ccui[ui] if oi else lc(ccui[ui]), label=uenwl[ui] if not ti and not ai and oi else None)
                                        ax[1][0].scatter(x, y, color=cc[ai % len(cc)] if oi else lc(cc[ai % len(cc)]), label=attl[ai] if not ti and not ui and oi else None)
                                        ax[2][0].scatter(x, y, color=cc[ti % len(testl)] if oi else lc(cc[ti % len(testl)]), label=testl[ti % len(testl)] if not ui and not ai and oi else None)
                                        # if not oi:
                                        #     ax[0][0].scatter(x, y, color=lc(cc[ui]))
                                        # else:
                                        #     ax[0][0].scatter(x, y, color=cc[ui], label=uenwl[ui] if not ti and not ai else None)
                                    else:
                                        ax[0][1].scatter(x, y, color=ccui[ui] if oi else lc(ccui[ui]), label=uenwl[ui] if not ti and not ai and oi else None)
                                        ax[1][1].scatter(x, y, color=cc[ai % len(cc)] if oi else lc(cc[ai % len(cc)]), label=attl[ai] if not ti and ui == 2 and oi else None)
                                        ax[2][1].scatter(x, y, color=cc[ti] if oi else lc(cc[ti]), label=testl[ti] if ui == 2 and not ai and oi else None)
                                        # if not oi:
                                        #     ax[0][1].scatter(x, y, color=lc(cc[ui]))
                                        # else:
                                        #     ax[0][1].scatter(x, y, color=cc[ui], label=uenwl[ui] if not ti and not ai else None)
                                    i3 = int(ui/2)
                                    if not oi:
                                        ax[0][2].scatter(x, y, color=lc(cc_compare[i3]))
                                    else:
                                        ax[0][2].scatter(x, y, color=cc_compare[i3], label=nwl[i3] if not ti and not ai and not ui % 2 else None)

                                    if not oi:
                                        ecl = atk['ECL'][r]
                                        ecll = ecl_list if not si else ecl_listo
                                        for xp, yp, e in zip(x, y, ecl):
                                            ax[2][2].scatter(xp, yp, color=cc[int(e)], label=('N/A' if e == 3 else 'ECL ' + str(int(e))) if not e in ecll else None, alpha=0.8)
                                            ecll.append(e)
                                        acounts += len(y)
                                        if si:
                                            oiutcounts += len(y)
                                    else:
                                        if y.size:
                                            # hy = np.mean(y)
                                            for hy in y:
                                                ally[ui].append(hy)
                                                if not si:
                                                    hytest[ti].append(hy)
                                                    hyuenw[ui].append(hy)
                                                    hyatt[ai].append(hy)
                                        if not si:
                                            if x.size:
                                                # hx = np.mean(x)
                                                for hx in x:
                                                    hxtest[ti].append(hx)
                                                    hxuenw[ui].append(hx)
                                                    hxatt[ai].append(hx)
                                        else:
                                            outcounts += len(y)

                                # # outliers
                                # rx = np.invert(rx) if invert[0] else rx==rx
                                # ry = np.invert(ry) if invert[1] else ry==ry
                                # r = rx * ry
                                # x = np.array(atk[kx])[r]/scale[0]
                                # y = np.array(atk[ky])[r]/scale[1]
                                # if oi:
                                #     outcounts += len(y)
                                #     if y.size:
                                #         for hoy in y:
                                #             ally[ui].append(hoy)
                                # else:
                                #     oiutcounts += len(y)
                                # ms=80
                                # axo[1][0].scatter(x, y, color=cc[ai] if oi else lc(cc[ai]), s=ms)
                                # axo[0][2].scatter(x, y, color=cc[ui] if oi else lc(cc[ui]), s=ms)
                                # axo[2][0].scatter(x, y, color=cc[ti] if oi else lc(cc[ti]), s=ms)
                                # if not oi:
                                #     ecl = atk['ECL'][r]
                                #     for xp, yp, e in zip(x, y, ecl):
                                #         axo[2][2].scatter(xp, yp, color=cc[int(e)], s=ms, alpha=0.8)
                                    

                            except TypeError as e:
                            # except KeyboardInterrupt as e:
                                print(e, atd[kx])
                        except (KeyError, TypeError) as e:
                            # print(e, kx, ky)
                        # except KeyboardInterrupt as e:
                            pass

    for i, ax in enumerate([ax for row in axp for ax in row]):
        if log:
            ax.set_yscale('log')

    for si in range(2):
        ax = axo if si else axp
        ax[1][2].boxplot(ally)
        f1, f2, g1, g2 = ax[0][2].axis()
        ax[1][2].set_ylim(g1, g2)
        ax[1][2].set_xticklabels(('U-M', 'Q-M', 'U-V', 'Q-V'))

        ax[0][1].set_yticklabels([])
        # ax[0][2].set_yticklabels([])
        ax[1][1].set_yticklabels([])
        # ax[1][2].set_yticklabels([])
        ax[2][1].set_yticklabels([])
        # ax[2][2].set_yticklabels([])

        ax[0][0].set_xlim(f1, f2)
        ax[0][0].set_ylim(g1, g2)
        ax[0][1].set_xlim(f1, f2)
        ax[0][1].set_ylim(g1, g2)
        ax[1][0].set_xlim(f1, f2)
        ax[1][0].set_ylim(g1, g2)
        ax[1][1].set_xlim(f1, f2)
        ax[1][1].set_ylim(g1, g2)
        ax[2][0].set_xlim(f1, f2)
        ax[2][0].set_ylim(g1, g2)
        ax[2][1].set_xlim(f1, f2)
        ax[2][1].set_ylim(g1, g2)

        Afont = {
            #'family': 'serif',
            # 'facecolor': 'blue',
            # 'color':  'white',
            # 'weight': 'normal',
            # 'size': 14,
        }
        ax[0][0].set_ylabel(ylabel)
        ax[1][0].set_ylabel(ylabel)
        ax[2][0].set_ylabel(ylabel)
        ax[2][0].set_xlabel(xlabel)
        ax[2][1].set_xlabel(xlabel)
        ax[2][2].set_xlabel(xlabel)
        if (log and not si) or (not log):
            ax[0][0].legend(loc=loc, bbox_to_anchor=bbox) # 'best' (1.05, 1.12)
            ax[0][1].legend(loc=loc, bbox_to_anchor=bbox) # 'best'
            ax[0][2].legend(loc=loc, bbox_to_anchor=bbox) # 'best'
            ax[1][0].set_zorder(1)
            ax[2][0].set_zorder(1)
            if joburg:
                ax[1][1].legend(loc=loc) #, bbox_to_anchor=(1.35, 1.12) if not si else (1.35, 1.04)) # 'best'
                ax[2][1].legend(loc=loc) #, bbox_to_anchor=(1.35, 1.12) if not si else (1.35, 1.04)) # 'best'
            else:
                ax[1][0].legend(loc=loc, bbox_to_anchor=(1.35, 1.12) if not si else (1.35, 1.04)) # 'best'
                ax[2][0].legend(loc=loc, bbox_to_anchor=(1.35, 1.12) if not si else (1.35, 1.04)) # 'best'
            ax[2][2].legend(loc=loc, bbox_to_anchor=bbox if not si else (bbox[0], 1.04)) # 'best'

    axp[0][0].add_artist(AnchoredText(str(sum([len(a) for a in hytest])) + '/' + str(acounts) + '\nK=' + str(K), loc=2))
    axo[0][0].add_artist(AnchoredText(str(outcounts) + '/' + str(oiutcounts) + '\nK=' + str(K), loc=2))
    # f1, f2, g1, g2 = axp[0][2].axis()
    y2 = axp[0][2].get_yticks()[-1]
    for i, (ax1, ax2, alph) in enumerate(zip([ax for row in axp for ax in row], [ax for row in axo for ax in row], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])):
        ax2.set_ylim(y2 - 0.1*np.abs(y2), None)
        ax1.add_artist(AnchoredText(alph, loc='lower right' if i in [1,4,7] else 'lower left'))
        ax2.add_artist(AnchoredText(alph, loc='lower right' if i in [1,4,7] else 'lower left'))
        if log:
            ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
        if i != 5:
            # if log:
            #     ax1.set_yscale('log')
            if joburg:
                ax1.xaxis.set_major_locator(MultipleLocator(20))
            else:
                ax1.xaxis.set_major_locator(MultipleLocator(10))

    kx = '_'.join(kx.split())
    ky = '_'.join(ky.split())
    # plt.tight_layout()
    plt.show()
    fig.savefig(folder + kx + '_' + ky + '_plot.png', bbox_inches='tight')
    fig.savefig(folder + kx + '_' + ky + '_plot.pdf', bbox_inches='tight')
    fig2.savefig(folder + kx + '_' + ky + '_outliers.png', bbox_inches='tight')
    fig2.savefig(folder + kx + '_' + ky + '_outliers.pdf', bbox_inches='tight')
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
    ax1.legend(loc='upper right', bbox_to_anchor=(1.07, 1.15))
    ax2.legend(loc='upper right', bbox_to_anchor=(1.07, 1.15))
    ax3.legend(loc='upper right', bbox_to_anchor=(1.07, 1.15))
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
        ax1.legend(loc='upper right', bbox_to_anchor=(1.07, 1.15))
        ax2.legend(loc='upper right', bbox_to_anchor=(1.07, 1.15))
        ax3.legend(loc='upper right', bbox_to_anchor=(1.07, 1.15))
        kkx = '_'.join(kkx.split())
        fig2.savefig(ffolder + kkx + '_histogram.png')
        fig2.savefig(ffolder + kkx + '_histogram.pdf')
        plt.show()
    return hcounts, outcounts, hyuenw


    # fig = plt.figure(figsize=(9, 8))
    # ax1 = fig.add_subplot(221)
    # ax2 = fig.add_subplot(222)
    # ax3 = fig.add_subplot(223)
    # axo[1][0] = fig.add_subplot(224)