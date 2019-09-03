import numpy as np
import matplotlib.pyplot as plt
import glob

print('custom jupyter @DanielRobinson')

dirr = ""
debug = False

def adjust(key, val):
#     if key == 'Total power':
#         return max(-1400, val)
    # if key == 'Signal power':
    #     return max(-1640, val)
    if key == 'ECL':
        return min(3, val)
#     if key == 'SNR':
#         return max(-200, val)
# #     if key == 'txTime':
# #         if val > 200000:
# #             return 20000
# #     if key == 'energy':
# #         return min(100000, val)
    # if key == 'TX power':
    #     return max(-1000, val)
#     if key == 'EARFCN':
#         return min(10000, val)
#     if key == 'PCI':
#         if val > 1000:
#             return 0
#     if key == 'RSRQ':
#         if val < -1000:
#             return 0
    return val

def exclude(key, vals):
    a = np.array(vals)
    r = a == a
    if key == 'Signal power':
        r *= a > -1450
    if key == 'Total power':
        r *= a > -1450
    if key == 'TX power':
        r *= a > -2000
    if key == 'SNR':
        r *= a > -1000
    if key == 'RSRQ':
        r *= a > -1000
    if key == 'txBytes':
        r *= a > 0
    if key == 'rxBytes':
        r *= a > 0
    if key == 'txTimeNW':
        r *= a > 0
    if key == 'rxTimeNW':
        r *= a > 0
    if key == 'EARFCN':
        r *= a > 0
    if key == 'PCI':
        r *= a > 0
    return r

def threshold(a, key):
    # print('a[key]', a[key], key)
    a = np.array(a[key])
    r = a == a
    lim = [None, None]
    if key == 'Signal power':
        r *= a > -1450
    if key == 'txTime':
        r *= a < 25000
    if key == 'TX power':
        r *= a > -1000
    if key == 'Total power':
        r *= a > -1400
    if key == 'SNR':
        r *= a > -200
    if key == 'energy':
        r *= a > 0
        r *= a < 50000
    if key == 'txBytes':
        r *= a < 1100
    if key == 'rxBytes':
        r *= a < 1100
    if key == 'txTimeNW':
        r *= a < 20000
    if key == 'rxTimeNW':
        r *= a < 20000
    if key == 'Total ACK NACK RX':
        r *= a > 0
    # if key == 'EARFCN':
    #     r *= a < 100000
    if key == 'PCI':
        r *= a < 200
    # if key == 'Total TX bytes':
    #     r *= a > 0
    # if key == 'Total RX bytes':
    #     r *= a > 0

    # if key == 'rxBytes':
    #     r *= a > 0

    # if key == 'TX time':

    # if key == 'RX time':


    return r

def thresh(a, key, split):
    # print('a[key]', a[key], key)
    a = np.array(a[key])
    r = a == a
    lim = [None, None]
    if key == 'Signal power':
        r *= a > -1450
        lim = [-1350, -700]
    if key == 'TX power':
        r *= a > -1400
    if key == 'Total power':
        r *= a > -1400
    if key == 'SNR':
        r *= a > -200
        # lim = [-200, 200]
    if key == 'energy':
        r *= a > 0
        lim = [1, 800000]
    if key == 'Total TX bytes':
        r *= a > 0
        lim = [None, 100000]
    if key == 'Total RX bytes':
        r *= a > 0
        lim = [None, 50000]
    if key == 'txBytes':
        r *= a > 0
        limits = [10000, 500, 200, 50]
        r, lim = splitter(r, a, limits, split, True)
    if key == 'rxBytes':
        r *= a > 0
        limits = [10000, 500, 200, 50]
        r, lim = splitter(r, a, limits, split, True)
    if key == 'TX time':
        limits = [120000, 50]
        r, lim = splitter(r, a, limits, split, True)
    if key == 'RX time':
        limits = [500000, 50]
        r, lim = splitter(r, a, limits, split, True)
    if key == 'txTimeNW':
        limits = [120000, 50]
        r, lim = splitter(r, a, limits, split, True)
    if key == 'rxTimeNW':
        limits = [120000, 50]
        r, lim = splitter(r, a, limits, split, True)
    return r, lim

def compare(files, thresh, text, ylabel, xlabel, ky, kx, ry, rx, overlays=['ublox', 'quectel'], graphs=['zte', 'nokia'], split=1, hist=False, bins=20, log=True, weighted=True):
    global dirr
    sy = len(graphs)
    fx = 7 * sy
    fy = 4 * split
    sx = split
    debug = False
    alpha = 1.0
    dev = ['ublox', 'quectel']
    nwv = ['zte_mtn/rf_shield/', 'nokia_vodacom/centurycity/']
    loc = ['MTN ZTE', 'Vodacom Nokia']
    colours = [['g*', 'k*'], ['b*', 'r*']]
    # colours = [['g*', 'k*'], ['g*', 'k*']]
    
    fig = plt.figure(figsize=(fx, fy))
    plt.suptitle(text + (" histogram" if hist else " plot"), y=0.92)
    axlist = []
    if hist:
        xlabel = ylabel
        ylabel = 'Count'
    
    for i in range(split):
        ax = [None, None]
        lens = []
        # hyys = []
        # lys = []
        # spcolours = []
        # print('i', i)
        for s in range(sy):
            # print('s', s)
            hyy = []
            pcolours = []
            ax[s] = fig.add_subplot(sx, sy, s + 1 + i * sy)
            axlist.append(ax[s])
            if i == np.floor(split/2):
                plt.ylabel(ylabel)
            for j in range(len(overlays)):
                # print('j', j)
                b = [overlays[j] in a for a in nwv]
                nwi = b.index(True) if True in b else [graphs[s] in a for a in nwv].index(True)
                uei = dev.index(overlays[j]) if overlays[j] in dev else dev.index(graphs[s])
                dirr = 'logs/' + nwv[nwi] + dev[uei] + '/'
                if hist:
                    pcolours.append(colours[nwi][uei][0])
                else:
                    pcolours.append(colours[nwi][uei])
                # print(i, s, j, dirr, nwi, uei)
                hy, ly = plot(ax[0], ax[1], kx, ky, rx, ry, files, colours[nwi][uei], alpha, (i, split), hist, thresh, [[s, len(graphs)], [j, len(overlays)]], bins, log, dev[uei])
                if hist and str(type(hy)) != "<class 'NoneType'>":
                    lens.append(len(hy))
                    hyy.append(hy)
                    # print('lens', lens)
                    # hyys.append(hyy)
                    # spcolours.append(pcolours)
                    # lys.append(lys)
                # if i == split - 1:
                #     print('dirr', dirr)
            if hist:
                b = [len(a) for a in hyy]
                m = max(lens)
                w = [[1 * m / c] * c for c in b]
                # print(lens, m, b)
                # print(hyy, bins)
                try:
                    data = np.concatenate(np.ravel(hyy))
                except ValueError:
                    data = np.ravel(hyy)
                finally:
                    _, lbins = np.histogram(data, bins=bins)
                    logbins = np.logspace(np.log10(lbins[0]), np.log10(lbins[-1]), len(lbins))
                    n, rbins, _ = ax[s].hist(hyy, color=pcolours[:len(hyy)], alpha=alpha, range=ly, bins= logbins if log else bins, log=log, stacked=False, label=overlays, weights=w if weighted else None)
                    plt.xscale('log')
                    # ax[s].legend(prop={'size': 10})
                    np.set_printoptions(precision=0, suppress=True)
                    print(rbins)
                    # print(ly)
                    ax[s].set_xlim(ly) # x
            if i == split - 1:
                if overlays[j] in dev:
                    plt.xlabel(loc[nwi] + ' ' + xlabel)
                else:
                    plt.xlabel(dev[uei][0].upper() + dev[uei][1:] + ' ' + xlabel)
        
        # y alignment of dual plot graphs
        if s >= 1:# and j >= (1 if len(overlays) > 0 else 0):
            f1, f2, g1, g2 = ax[1].axis()
            h1, h2, u1, u2 = ax[0].axis()
            ax[0].set_ylim([min(u1, g1), max(u2, g2)])
            ax[1].set_ylim([min(u1, g1), max(u2, g2)])
            ax[0].set_xlim([min(f1, h1), max(f2, h2)])
            ax[1].set_xlim([min(f1, h1), max(f2, h2)])
            # print(f1, f2, g1, g2)
            # print(min(u1, g1), max(u2, g2))
        # for s in range(len(hyys)):
        #     if s >= 1:
        #         lens = np.array(lens).T
        #         # b = [len(a) for a in a]
        #         # [[1 * b[-1] / c] * c for c in b]
        #     ax[s].hist(hyys[s], color=spcolours[s], alpha=alpha, range=lys[s], bins=bins, log=log, )
        #     ax[s].set_xlim(ly) # x alignment of dual hist graphs

    import matplotlib.ticker as ticker
    # make hist have same y axis
    ymin = ymax = 0.8
    for ax in axlist:
        h1, h2, u1, u2 = ax.axis()
        # ymin = min(ymin, u1) # None if log else ymin
        ymax = max(ymax, u2)
    for ax in axlist:
        ax.legend(prop={'size': 10})
        if hist:
            ax.set_ylim([ymin, ymax])
        # ax.legend(prop={'size': 10}, labels=overlays)
        # print(ymin, ymax)
        if log:
            for axis in [ax.xaxis, ax.yaxis]:
                axis.set_major_formatter(ticker.FuncFormatter(lambda y,pos: ('{{:.{:1d}f}}'.format(int(np.maximum(-np.log10(max(y, 0.01)),0)))).format(y)))
    
    log = "_log_" if log else "_"
    hist = "_hist_" if hist else "_"
    pic = 'img/Vodacom_vs_MTN_' + "_".join(caps(graphs)) + "_" + "_".join(caps(overlays)) + log + str(split) + hist + "_".join(text.split())
    plt.savefig(pic + '.png')
    plt.savefig(pic + '.pdf')
    plt.show()

def caps(a):
    for i in range(len(a)):
        if 'zte' in a[i]:
            a[i] = 'ZTE'
        else:
            a[i] = a[i][0].upper() + a[i][1:]
    return a
        
def plot(ax1, ax2, x, y, xr, yr, files, colour, alpha, split, hist, thresh, indexes, bins, log, overlay):
    # print(ax1, ax2, x, y, xr, yr, colour, alpha, split, hist, indexes, bins, log)
    # print('plot(x, y, xr, yr, files, colour, alpha, split, hist)', x, y)
    hy = []
    ax = ax2 if ax2 else ax1
    right = indexes[0][0] >= 1
    ci = 0
    for fi, f in enumerate(files):
        # print('zu_mg')
        zu_mg = merge(mk(f))
        # print('len zu_mg', len(zu_mg))
        # print('zu_mg', zu_mg)
        if zu_mg:
            p, q, limits = dict_filt(zu_mg, x, y, split, thresh)
            # print('p, q', p, q, 'limits', limits)
            try:
                if len(p) and len(q):
                    if hist:
                        # print('hist q/yr', q/yr)
                        if len(q):
                            hy.append(q/yr)
                        continue
                    # print('plot q/yr', q/yr)
                    if log:
                        ax.semilogy(p/xr, q/yr, colour, label=overlay if not ci else None, alpha=alpha)
                    else:
                        ax.plot(p/xr, q/yr, colour, label=overlay if not ci else None, alpha=alpha)
                        
                    ci += 1
            except TypeError:
                pass

    # y and x limit alignment of dual plot graphs
    lx = limits[0]
    ly = limits[1]
    # print('type(lx)', str(type(lx)))
    if str(type(lx)) != "<class 'NoneType'>":
        if lx[0]:
            lx[0] /= xr
        if lx[1]:
            lx[1] /= xr
        if not hist:
            ax.set_xlim(lx)
    if str(type(ly)) != "<class 'NoneType'>":
        if ly[0]:
            ly[0] /= yr
        if ly[1]:
            ly[1] /= yr
        if not hist:
            ax.set_ylim(ly)


    if hist and hy:
        # remember that ravel passes by reference, unlike flatten which passes a copy of the array
        try:
            hy = np.concatenate(np.ravel(hy))
        except ValueError:
            hy = np.ravel(hy)
        finally:
            if len(hy):
                # print(len(hy))
                if not ly[0] and not ly[1]:
                    ly = None
                # print('ly', ly)
                # print(len(hy), ly)
                return hy, ly 
                
    # # y alignment of dual plot graphs
    # if right and indexes[1][0] >= (1 if indexes[1][1] > 0 else 0):
    #     f1, f2, g1, g2 = ax2.axis()
    #     h1, h2, u1, u2 = ax1.axis()
    #     ax1.set_ylim([min(u1, g1), max(u2, g2)])
    #     ax2.set_ylim([min(u1, g1), max(u2, g2)])
    #     ax1.set_xlim([min(f1, h1), max(f2, h2)])
    #     ax2.set_xlim([min(f1, h1), max(f2, h2)])
    #     # print(f1, f2, g1, g2)
    #     # print(min(u1, g1), max(u2, g2))
    
    return None, None
    
def splitter(r, a, limits, split, ends=True):
    split, slen = split
    if ends:
        if slen == 1:
            limits = [limits[0], limits[-1]]
        lim = [limits[split+1], limits[split]]
        r *= a < limits[split]
        r *= a >= limits[split+1]
    else:
        # limits = limits[1:1]
        if split == 0:
            lim = [limits[split], None]
            r *= a >= limits[split]
        elif split == slen - 1:
            lim = [None, limits[split-1]]
            r *= a < limits[split-1]
        else:
            lim = [limits[split], limits[split-1]]
            r *= a < limits[split-1]
            r *= a >= limits[split]
    # print('splitter lim', lim)
    return r, lim
    
def dict_filt(dc, x, y, split, thresh):
    _debug = False
    try:
        try:
            # kx = [x, x[1:-1]]
            # kx = kx[[a in dc.keys() for a in kx].index(True)]
            # ky = [y, y[1:-1]]
            # ky = ky[[a in dc.keys() for a in ky].index(True)]
            t, limitx = thresh(dc, x, split)
            t2, limity = thresh(dc, y, split)
            if len(t):
                t *= t2
            if _debug:
                print('dc[x]', x, len(dc[x]), 'dc[y]', y, len(dc[y]), dc[x], dc[y])
            return np.array(dc[x])[t], np.array(dc[y])[t], [limitx, limity]
        except KeyError:
            return None, None, [None, None]
    except IndexError as e:
        print(IndexError, 'len(dc[x]) and len(dc[y])', len(dc[x]) and len(dc[y]), e)
        return np.array(dc[x]), np.array(dc[y]), [None, None]


def clean(arr, val):
    try:
        for i in arr:
            arr.pop(arr.index(val))
    except ValueError:
        pass
    return arr

# csv to {}
def csvToDict(file):
    dt = {}
    data = []
    header = []
    fheader = ['index','idleTime','txTime','totalTime','energy','maxCurrent','Signal power','Total power','TX power','TX time','RX time','Cell ID','ECL','SNR','EARFCN','PCI','RSRQ','RLC UL BLER','RLC DL BLER','MAC UL BLER','MAC DL BLER','Total TX bytes','Total RX bytes','Total TX blocks','Total RX blocks','Total RTX blocks','Total ACK/NACK RX','RLC UL','RLC DL','MAC UL','MAC DL','Current Allocated','Total Free','Max Free','Num Allocs','Num Frees','primary_cell','rsrp','rsrq','rssi','snr']
    ready = False
    
    # test file encoding
    enc = 'utf-16-le'
    try:
        with open(file, 'r', encoding=enc) as f:
            for l in f:
                pass
            if 'CAPTURE' not in f.readlines()[:20]:
                enc = None
    except UnicodeDecodeError as e:
        # print(UnicodeDecodeError)
        enc = None    
    
    with open(file, 'r', encoding=enc) as f:
        for line in f:
            if ',' in line:
                if 'index' in line:
                    header = np.array([v for v in line.strip().split(",")[:-1]])
                    # print(header)
                else:
                    data.append([float(v) for v in line.strip().split(",")[:-1]])
    rows = len(data)
    cols = len(header)
    
    # populate empty values with zeroes.
    nump = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            try:
                nump[i][j] = data[i][j]
            except IndexError:
                pass
            
    # print(nump.shape)
    # print(nump.T)
    for n, d in zip(header, nump.T):
        if n in fheader:
            dt[n] = d
        else:
            for fh in fheader:
                if n in fh:
                    dt[fh] = d
    # dt['name'] = file
    return dt

# post processing csv {} data
def dataProcess(dt):
    dt['Total ACK NACK RX'] = dt.pop('Total ACK/NACK RX')
    # print('Total ACK NACK RX', dt['Total ACK NACK RX'])
    try:
        kins = ['idleTime', 'Total TX bytes', 'Total RX bytes', 'TX time', 'RX time']
        kouts = ['time', 'txBytes', 'rxBytes', 'txTimeNW', 'rxTimeNW']
        for ko in kouts:
            dt[ko] = [0]
        for k, ko in zip(kins, kouts):
            for i, v in enumerate(dt[k]):
                if k == 'idleTime':
                    if i > 0:
                        dt[ko].append(v + dt['txTime'][i-1] + dt[ko][i-1])
                if k in kins[1:]:
                    if i > 0:
                        # print('dt[k][i] - dt[k][i-1]', dt[k][i] - dt[k][i-1])
                        dt[ko].append(dt[k][i] - dt[k][i-1])
            # if k == 'Total TX bytes':
                # print('dt[k]', dt[k])
                # print("dt['txBytes']", dt['txBytes'])
    except KeyError:
        dt[ko] = [[0] * len(dt['Signal power'])][0]
        # print('KeyError: ', "dt['txBytes']", dt['txBytes'])
    finally:
        for ko in kouts:
            dt[ko] = np.array(dt[ko])
        return dt

def dp(dt, length=1000, time=False):
    datasetPlot(dt, length, time)
    
def datasetPlot(dt, length, time):
    h = len(dt[0])/2 + 1
    rainbow = ['g*', 'r*', 'b*', 'y*', 'k*', 'm*', 'c*']
    plt.figure(figsize=(h,h))
    i = 1
    for k in dt[0]:
        if str(type(dt[0][k])) == "<class 'numpy.ndarray'>":
            try:
                # check for data changes
                if len(dt) > 1:
                    diff = np.mean(dt[0][k])
                    for d in dt:
                        if np.mean(d[k]) != diff:
                            break
                        diff = np.mean(d[k])
                    else:
                        continue
            except KeyError:
                pass

            plt.subplot(h,2,i)
            plt.title(k)  
            for j, d in enumerate(dt):
                try:
                    l = min(len(d[k]), length)
                    if time:
                        t = d['time'][:l]
                    else:
                        t = np.arange(0, l, 1)
                    plt.plot(t, d[k][:l], rainbow[j % len(rainbow)])
                except KeyError:
                    pass
            i += 1
    plt.show()

# join attenuated files together into database
def mk(files):
    global dirr
    # print('files', files, 'dirr', dirr)
    dt = []
    file_list = []
    if str(type(files)) == "<class 'str'>":
        file_list = glob.glob(dirr + files)
    else:
        for fl in files:
            file_list.append(dirr + fl)
    # print('file_list', file_list)
    for f in file_list:
        # print('filefff', f)
        c = csvToDict(f)
        dp = dataProcess(c)
        # print("dp['txBytes']", dp['txBytes'])
        dt.append(dp)
    return dt

def maxHeaders(dt):
    m = 0
    maxH = []
    for d in dt:
        if len(d) > m:
            try:
                m = len(d)
                maxH = []
                for k in d:
                    # if k == 'txBytes':
                    #     print(str(type(d[k])))
                    if str(type(d[k])) == "<class 'numpy.ndarray'>":
                        maxH.append(k)
                    # if str(type(d[k])) == "<class 'list'>":
                    #     # print(k)
            except TypeError as e:
                # print(TypeError, e, d)
                pass
    # print('maxH', maxH)
    return maxH

def merge(dt):
    merge = {}
    maxH = maxHeaders(dt)
    if debug: 
        print('dt len:', len(maxH))
    for k in maxH:
        merge[k] = []
        for d in dt:
            try:
                for element in d[k]:
                    merge[k].append(adjust(k, element))
            except (KeyError, IndexError) as e:
                if debug: 
                    print(e, end=",")
    return merge

def mean(dt):
    mean = {}
    # maxH = maxHeaders(dt)
    if debug: 
        print('dt len:', len(dt[0]))
    for k in dt:
        # print(k, type(dt[k]))
        if str(type(dt[k])) == "<class 'list'>":
            vals = np.array(dt[k])[exclude(k, dt[k])]
            try:
                if len(vals):
                    mean[k] = np.mean(vals)
            except TypeError:
                print(e, k, vals)
    return mean


        # if descr in ['zte', 'all_nw']:
        #     ax1 = fig.add_subplot(sx, sy, 1 + i * 2)
        #     if i == split - 1:
        #         plt.xlabel('MTN ZTE ' + xlabel)
        #     if i == np.ceil(split/2):
        #         plt.ylabel(ylabel)
        #     colours = ['g*', 'k*']
        #     num = 2 if overlay == 'all' else 1
        #     for j in range(num):
        #         dirr = 'logs/zte_mtn/rf_shield/' + (dev[j] if num > 1 else overlay) + '/'
        #         plot(ax1, None, kx, ky, rx, ry, files, colours[j if num > 1 else dev.index(overlay)], alpha[j], (i, split), hist, thresh, j)
        # if descr in ['nokia', 'all_nw'] and sy > 1:
        #     ax2 = fig.add_subplot(sx, sy, 2 + i * 2)
        #     if i == split - 1:
        #         plt.xlabel('Vodacom Nokia ' + xlabel)
        #     if overlay in ['ublox', 'all']:
        #         dirr = 'logs/nokia_vodacom/centurycity/ublox/'
        #         plot(ax1, ax2, kx, ky, rx, ry, files, 'b*', alpha[0], (i, split), hist, thresh, 0)
        #     if overlay in ['quectel', 'all']:
        #         dirr = 'logs/nokia_vodacom/centurycity/quectel/'
        #         plot(ax1, ax2, kx, ky, rx, ry, files, 'r*', alpha[1], (i, split), hist, thresh, 1)
        # if descr in ['ublox', 'all_ue']:
        #     ax1 = fig.add_subplot(sx, sy, 1 + i * 2)
        #     if i == split - 1:
        #         plt.xlabel('Ublox ' + xlabel)
        #     plt.ylabel(ylabel)
        #     if overlay in ['zte', 'all']:
        #         dirr = 'logs/zte_mtn/rf_shield/ublox/'
        #         plot(ax1, None, kx, ky, rx, ry, files, 'g*', alpha[0], (i, split), hist, thresh, 0)
        #     if overlay in ['nokia', 'all']:
        #         dirr = 'logs/nokia_vodacom/centurycity/ublox/'
        #         plot(ax1, None, kx, ky, rx, ry, files, 'b*', alpha[1], (i, split), hist, thresh, 1)
        # if descr in ['quectel', 'all_ue'] and sy > 1:
        #     ax2 = fig.add_subplot(sx, sy, 2 + i * 2)
        #     if i == split - 1:
        #         plt.xlabel('Quectel ' + xlabel)
        #     if overlay in ['zte', 'all']:
        #         dirr = 'logs/zte_mtn/rf_shield/quectel/'
        #         plot(ax1, ax2, kx, ky, rx, ry, files, 'k*', alpha[0], (i, split), hist, thresh, 0)
        #     if overlay in ['nokia', 'all']:
        #         dirr = 'logs/nokia_vodacom/centurycity/quectel/'
        #         plot(ax1, ax2, kx, ky, rx, ry, files, 'r*', alpha[1], (i, split), hist, thresh, 1)