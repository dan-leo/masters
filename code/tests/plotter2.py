def pan4(name, dirrs, files, kx, ky, thresh, plotlim, distlim, histlim, scale, limited, bins=20):
    plot_hist = False
    plot_dist = False

    np.set_printoptions(precision=3, suppress=True)
    cc = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:blue', 'tab:brown']
    # 4x4 plotter
    paxis = []
    daxis = []
    haxis = []
    hist = []
    aka = []
    fy = 8
    fx = 12
    fig = plt.figure(figsize=(fx, fy))
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
                        if atn >= 50:
                            atf['50-110 dB'].append(file)
                        else:
                            atf[str(atn) + ' dB'].append(file)
                        break
                else:
                    print('else', file)
                    atf['50-110 dB'].append(file)

        ####################### database {} prep #######################

        atd = attdt()
        for k in atf:
            # print(k, atf[k])
            for f in atf[k]:
                c = j.csvToDict(f)
                dp = j.dataProcess(c)
                atd[k].append(dp)
            atd[k] = j.merge(atd[k])
            # print('atd[k]', len(atd[k]))

        ####################### scatter #######################
        # fig = plt.figure()
        ax = fig.add_subplot(2, 2, di + 1)
        y = []
        x = []
        ka = []

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
                # print(yy)
                xx = xx / scale[0]
                yy = yy / scale[1]
                ax.scatter(xx[r], yy[r], linestyle='dotted', color=cc[i], label=k)
                x.append(xx[r])
                y.append(yy[r])
                ka.append(k)
            except (KeyError, IndexError) as e:
                print(e)
        hist.append([x, y])
        aka.append(ka)
        # ax = plt.gca()
        paxis.append(ax)
        ax.set_yscale('log')
        ax.set_xlim(plotlim[:2])
        ax.set_ylim(plotlim[2:])
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
        ax.legend()#bbox_to_anchor=(0.97, 1.15))

    pic = 'plotter/' + name + '_plot'
    plt.savefig(pic + '.png')
    plt.savefig(pic + '.pdf')
#     plt.show()
    
    ####################### seaborn distribution #######################
    if plot_dist:
        fy = 8
        fx = 12
        fig = plt.figure(figsize=(fx, fy))
        legend = ['1', '2', '3', '4']
        
        ##############################
        
        ax = fig.add_subplot(2, 2, 1)
        for hi, h in enumerate(hist):
            df = pd.DataFrame(h[1])
            data = df.T.dropna().values.ravel()
            # print('data', data)
            sns.distplot(data, hist=False, kde=True,
                        ax=ax,
                        norm_hist=True,
                        hist_kws={'edgecolor':'black'})
        if limited:
            ax.set_xlim(distlim[:2][0], distlim[:2][1]/4)
            ax.set_ylim(distlim[2:])
    #     plt.xscale('log')
    #     plt.yscale('log')
    #     ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
    #     if limited:
    #         ax.set_yticklabels(['{:,.1%}'.format(x) for x in ax.get_yticks()]) 
        fig.legend(labels=legend)
        daxis.append(ax)
        
        
        ##############################
        
        
        ax = fig.add_subplot(2, 2, 2)
        for hi, h in enumerate(hist):
    #         s = pd.Series(h[1])
    #         print(s)
            df = pd.DataFrame(h[1])
            # df.index = pd.Index(legend)
            sns.distplot(df.T.dropna().values.ravel(), hist=False, kde=True, 
    #                      bins=logbins,
                        ax=ax,
                        norm_hist=True,
    #                      color = cc[:1],
    #                      color = ('blue', 'black'),
    #                      norm_hist=True,
    #                      kde_kws={'weight':[[100]*len(data)]},
                        hist_kws={'edgecolor':'black'})
        if limited:
            ax.set_xlim(distlim[:2])
        plt.xscale('log')
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
        daxis.append(ax)
        
        ##############################
        
        ax = fig.add_subplot(2, 2, 3)
        for hi, h in enumerate(hist):
            df = pd.DataFrame(h[1])
            data = df.T.dropna().values.ravel()
            sns.distplot(data, hist=False, kde=True,
                        ax=ax,
                        norm_hist=True,
                        hist_kws={'edgecolor':'black'})
        if limited:
            ax.set_xlim(distlim[:2])
            ax.set_ylim(distlim[2:])
    #     plt.xscale('log')
        plt.yscale('log')
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
        if limited:
            ax.set_yticklabels(['{:,.1%}'.format(x) for x in ax.get_yticks()])
        fig.legend(labels=legend)
        daxis.append(ax)
        
        ##############################

        ax = fig.add_subplot(2, 2, 4)
        for hi, h in enumerate(hist):
            df = pd.DataFrame(h[1])
            data = df.T.dropna().values.ravel()
            sns.distplot(data, hist=False, kde=True,
                        ax=ax,
                        norm_hist=True,
                        hist_kws={'edgecolor':'black'})
        if limited:
            ax.set_xlim(distlim[:2])
            ax.set_ylim(distlim[2:])
        plt.xscale('log')
        plt.yscale('log')
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
        if limited:
            ax.set_yticklabels(['{:,.1%}'.format(x) for x in ax.get_yticks()])
        fig.legend(labels=legend)
        daxis.append(ax)

        pic = 'plotter/' + name + '_logkde'
        plt.savefig(pic + '.png')
        plt.savefig(pic + '.pdf')

    ####################### histogram #######################
    
    if plot_hist:
        fy = 8
        fx = 12
        fig = plt.figure(figsize=(fx, fy))
        
        lens = []
        lllbins = []
        for hi, h in enumerate(hist):
            y = h[1]
            try:
                data = np.concatenate(np.ravel(y))
            except ValueError:
                data = np.flatten(y)
            finally:
                _, lbins = np.histogram(data, bins=bins)
                lens.append(len(data))
                lllbins.append(lbins)
                
        m = max(lens)
        print('len(data)', lens, m/np.array(lens))
        for hi, h in enumerate(hist):
            y = h[1]
            lbins = lllbins[hi]
            ratio = m / lens[hi]
            w = [[ratio for b in a] for a in y]
            w = [ratio] * 6
            # print(w)
            ax = fig.add_subplot(2, 2, hi + 1)
            if limited:
                logbins = np.logspace(np.log10(histlim[0]), np.log10(histlim[1]), len(lbins))
            else:
                # print(lbins[0], lbins[-1])
                logbins = np.logspace(np.log10(lbins[0]), np.log10(lbins[-1]), len(lbins))
            haxis.append(ax)
            # print('logbins', logbins)
            # ax = plt.gca()
            
            
            # ax.hist(y, bins=logbins, log=True, range=hlimy, stacked=True)
    #         print('len(y)', len(y), 'len(aka[hi])', len(aka[hi]))
    #         for t in y:
    #            print(len(t))
    #         for v in w:
    #            print(len(v))
    #         print(np.repeat(y, ratio).shape)

            # pseudo weights
    #         for u in range(len(y)):
    #             y[u] = np.repeat(y[u], np.ceil(ratio))
            df = pd.DataFrame(y)#, columns=k)
            df.index = pd.Index(aka[hi])
            
            df.T.plot.hist(stacked=True, ax=ax, bins=logbins, density=True, )#, weights=w)
            
            # https://randyzwitch.com/creating-stacked-bar-chart-seaborn/
            # https://stackoverflow.com/questions/47138271/how-to-create-a-stacked-bar-chart-for-my-dataframe-using-seaborn
    #         sns.distplot(df.T.dropna(), hist=True, kde=False,
    #                      norm_hist=True,
    #                      ax=ax,
    #                      color=cc[:len(y)],
    #                      hist_kws={'edgecolor':'black'})
            
            data = df.T.dropna().values.ravel()
            sns.distplot(data, hist=False, kde=True,
                        ax=ax,
    #                      kde_kws={'weight':[[100]*len(data)]},
                        hist_kws={'edgecolor':'black'})
            
            plt.xscale('log')
            plt.yscale('log')

            if limited:
                ax.set_xlim(histlim[:2])
                ax.set_ylim(histlim[2:])
                ax.set_yticklabels(['{:,.1%}'.format(x) for x in ax.get_yticks()])
            
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))

    ####################### limits #######################
    if not limited:
        # pxmin = pymin = pxmax = pymax = 1
        # hxmin = hymin = hxmax = hymax = 1
        plim = [v for v in paxis[0].axis()]
        hlim = [v for v in haxis[0].axis()]
        print(plim)
        print(hlim)
        # hlim = [1000, -1000]*2
        for pax, hax in zip(paxis, haxis):
            for i, p in enumerate(pax.axis()):
                plim[i] = min(plim[i], p) if i in [0, 2] else max(plim[i], p)
            for i, h in enumerate(hax.axis()):
                hlim[i] = min(hlim[i], h) if i in [0, 2] else max(hlim[i], h)
        for pax, hax in zip(paxis, haxis):
            pax.set_xlim(plim[:2])
            pax.set_ylim(plim[2:])
            hax.set_xlim(hlim[:2])
            hax.set_ylim(hlim[2:])
#             for axis in [pax.yaxis, hax.yaxis]:
#                 axis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
        np.set_printoptions(precision=5, suppress=True)     
        print('plotlim=', np.array(plim))
        print('distlim=', np.array(daxis[0].axis()))
        print('distlim=', np.array(daxis[1].axis()))
        print('histlim=', np.array(hlim))

    pic = 'plotter/' + name + '_hist'
    plt.savefig(pic + '.png')
    plt.savefig(pic + '.pdf')

    plt.show()
    # plt.xscale('log')