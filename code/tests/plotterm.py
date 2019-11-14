import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
import plotter as p
import jupyterlib as j
import importlib
import matplotlib.colors as mc
import colorsys
from sklearn.cluster import KMeans
from matplotlib.offsetbox import AnchoredText
from tabulate import tabulate

cc_compare = [(237/255, 189/255, 0), 'red']
ccui = ['tab:cyan', 'tab:grey', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:red']
cc = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:blue', 'tab:brown', 'tab:cyan']
testl = ['1-16 B', '64-128 B', '256-512 B', 'Echo', 'COPS', 'eDRX', 'PTAU']
uenwl = ['Ublox-MTN', 'Quectel-MTN', 'Ublox-Vodacom', 'Quectel-Vodacom']
nwl = ['MTN-ZTE', 'Vodacom-Nokia']
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


def plot(mdb, kx, ky, xlabel='', ylabel='', scale=[1,1], invert=[True,False], colour=cc, folder='', K=0, loc='upper right', bbox=(1.05, 1.12)):
    global hytest, hyuenw, hyatt, hxtest, hxuenw, hxatt, kkx, kky, xxlabel, yylabel, ffolder, outcounts, ally
    outcounts = acounts = oiutcounts = 0
    hytest, hyuenw, hyatt = [], [], []
    hxtest, hxuenw, hxatt = [], [], []
    hytw = []
    hecl = [[], [], [], []]
    ecl_list = []
    ecl_listo = []
    ally = []
    folder = folder + '/' if len(folder) else 'plotter3/'
    ffolder = folder
    kkx, kky = kx, ky
    xxlabel, yylabel = xlabel, ylabel
    for oi in range(2):
        for ti, test in enumerate(mdb):
            if oi:
                hytw.append([])
                for i in range(4):
                    hecl[i].append([])
                hytest.append([])
                hxtest.append([])
            for ui, uenw in enumerate(test):
                if oi:
                    hytw[ti].append([])
                    for i in range(4):
                        hecl[i][ti].append([])
                    if not ti:
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
                                rex = j.exclude(kx, atd[kx])
                                rey = j.exclude(ky, atd[ky])
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
                                    K_len = min(K, len(atdky))
                                    kmeans = KMeans(n_clusters=K_len)
                                    kmeans.fit(data.T)
                                    atk[kx], atk[ky] = kmeans.cluster_centers_.T
                                    # print(kmeans.labels_, atk[kx], atk[ky])
                                    # labels_   
                                    a = [[] for i in range(K_len)]
                                    for e, k in zip(atd['ECL'], kmeans.labels_):
                                        a[k].append(e)
                                    for i in range(K_len):
                                        a[i] = int(round(np.mean(a[i]))) if a[i] else a[i]
                                    for e, vy in zip(a, atk[ky]):
                                        # vy = vy / 1000 if ui >= 4 else vy
                                        hecl[e][ti][ui].append(vy/scale[1])
                                    # print(hecl)

                                else:
                                    atk[kx], atk[ky] = atd[kx], atd[ky]
                                    atk['ECL'] = atd['ECL']

                                if oi:
                                    x = atk[kx]/scale[0]
                                    y = atk[ky]/scale[1]
                                    if y.size:
                                        for hy in y:
                                            if not ti in [99]:
                                                # hy = hy / 1000 if ui >= 4 else hy
                                                ally[ui].append(hy)
                                                hytw[ti][ui].append(hy)
                            except TypeError as e:
                                print(e, atd[kx])
                        except (KeyError, TypeError) as e:
                            pass
    # mean = [np.mean(m) for m in ally]
    # # f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey='row')
    # fig = plt.figure(figsize=(7,4))
    # # ax1 = plt.subplot(121)
    # # ax2 = plt.subplot(133)
    # ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=2)
    # ax2 = plt.subplot2grid((1, 3), (0, 2))
    # ax1.bar(['Ublox-ZTE','Quectel-ZTE','Ublox-Nokia','Quectel-Nokia'], mean[:4])
    # ax2.bar(['MTN', 'Vodacom'], [np.mean(mean[:2]), np.mean(mean[2:4])], color=cc_compare)
    # _, _, g1, g2 = ax1.axis()
    # ax2.set_ylim(g1, g2)
    # plt.tight_layout()
    # print(tabulate([np.insert([str(np.mean(m)) for m in ally], 0, ylabel)], uenwl, tablefmt="github"))
    # print(tabulate([np.insert([str(np.mean(m)) for m in [mean[:2], mean[2:4]]], 0, ylabel)], ['MTN', 'Vodacom'], tablefmt="github"))
    # print(xlabel)
    print([str(np.mean(m))[:4] for m in ally])
    return ally, hytw, hecl
    # for si in range(2):
    #     ax = axo if si else axp
    #     ax[1][2].boxplot(ally)
    #     f1, f2, g1, g2 = ax[0][2].axis()
    #     ax[1][2].set_ylim(g1, g2)
    #     ax[1][2].set_xticklabels(('U-M', 'Q-M', 'U-V', 'Q-V'))

    #     ax[0][1].set_yticklabels([])
    #     # ax[0][2].set_yticklabels([])
    #     ax[1][1].set_yticklabels([])
    #     # ax[1][2].set_yticklabels([])
    #     ax[2][1].set_yticklabels([])
    #     # ax[2][2].set_yticklabels([])

    #     ax[0][0].set_xlim(f1, f2)
    #     ax[0][0].set_ylim(g1, g2)
    #     ax[0][1].set_xlim(f1, f2)
    #     ax[0][1].set_ylim(g1, g2)
    #     ax[1][0].set_xlim(f1, f2)
    #     ax[1][0].set_ylim(g1, g2)
    #     ax[1][1].set_xlim(f1, f2)
    #     ax[1][1].set_ylim(g1, g2)
    #     ax[2][0].set_xlim(f1, f2)
    #     ax[2][0].set_ylim(g1, g2)
    #     ax[2][1].set_xlim(f1, f2)
    #     ax[2][1].set_ylim(g1, g2)

    #     Afont = {
    #         #'family': 'serif',
    #         # 'facecolor': 'blue',
    #         # 'color':  'white',
    #         # 'weight': 'normal',
    #         # 'size': 14,
    #     }
    #     ax[0][0].set_ylabel(ylabel)
    #     ax[1][0].set_ylabel(ylabel)
    #     ax[2][0].set_ylabel(ylabel)
    #     ax[2][0].set_xlabel(xlabel)
    #     ax[2][1].set_xlabel(xlabel)
    #     ax[2][2].set_xlabel(xlabel)
    #     ax[0][0].legend(loc=loc, bbox_to_anchor=bbox) # 'best' (1.05, 1.12)
    #     ax[0][1].legend(loc=loc, bbox_to_anchor=bbox) # 'best'
    #     ax[0][2].legend(loc=loc, bbox_to_anchor=bbox) # 'best'
    #     ax[1][0].set_zorder(1)
    #     ax[2][0].set_zorder(1)
    #     ax[1][0].legend(loc=loc, bbox_to_anchor=(1.35, 1.12) if not si else (1.35, 1.04)) # 'best'
    #     ax[2][0].legend(loc=loc, bbox_to_anchor=(1.35, 1.12) if not si else (1.35, 1.04)) # 'best'
    #     ax[2][2].legend(loc=loc, bbox_to_anchor=bbox if not si else (bbox[0], 1.04)) # 'best'

    # axp[0][0].add_artist(AnchoredText(str(sum([len(a) for a in hytest])) + '/' + str(acounts) + '\nK=' + str(K), loc=2))
    # axo[0][0].add_artist(AnchoredText(str(outcounts) + '/' + str(oiutcounts) + '\nK=' + str(K), loc=2))
    # # f1, f2, g1, g2 = axp[0][2].axis()
    # y2 = axp[0][2].get_yticks()[-1]
    # for i, (ax1, ax2, alph) in enumerate(zip([ax for row in axp for ax in row], [ax for row in axo for ax in row], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])):
    #     ax2.set_ylim(y2 - 0.4*np.abs(y2), None)
    #     ax1.add_artist(AnchoredText(alph, loc='lower right' if i in [1,4,7] else 'lower left'))
    #     ax2.add_artist(AnchoredText(alph, loc='lower right' if i in [1,4,7] else 'lower left'))

    # kx = '_'.join(kx.split())
    # ky = '_'.join(ky.split())
    # # plt.tight_layout()
    # plt.show()
    # fig.savefig(folder + kx + '_' + ky + '_plot.png', bbox_inches='tight')
    # fig.savefig(folder + kx + '_' + ky + '_plot.pdf', bbox_inches='tight')
    # fig2.savefig(folder + kx + '_' + ky + '_outliers.png', bbox_inches='tight')
    # fig2.savefig(folder + kx + '_' + ky + '_outliers.pdf', bbox_inches='tight')
    # print(ti+1, ui+1, ai+1)

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