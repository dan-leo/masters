import numpy as np
import matplotlib.pyplot as plt
import glob

print('custom jupyter @DanielRobinson')

dirr = ""
debug = False

def compare(files, thresh, text, ylabel, xlabel, ky, kx, ry, rx, overlays=['ublox', 'quectel'], graphs=['zte', 'nokia'], split=1, hist=False):
    # print(files, text, ylabel, xlabel, ky, kx, ry, rx, descr, overlay, split, hist)
    global dirr
    _debug = False
    sy = len(graphs)
    fx = 7 * sy
    fy = 4 * split + 2
    sx = 1 + split
    debug = False
    alpha = [1, 0.7]
    dev = ['ublox', 'quectel']
    nwv = ['zte_mtn/rf_shield/', 'nokia_vodacom/centurycity/']
    loc = ['MTN ZTE', 'Vodacom Nokia']
    colours = [['g*', 'k*'], ['b*', 'r*']]
    if _debug: 
        print(fx, fy, sx, sy,)    
    
    fig = plt.figure(figsize=(fx, fy))
    plt.suptitle(text)

    for i in range(split):
        ax = [None, None]
        for s in range(sy):
            ax[s] = fig.add_subplot(sx, sy, s + 1 + i * 2)
            if i == split - 1:
                plt.xlabel(loc[s] + ' ' + xlabel)
            if i == np.floor(split/2):
                plt.ylabel(ylabel)
            num = 2 if overlay == 'all' else 1
            for j in range(num):
                if num > 1:
                    if 'nw' in descr:
                        nwvi = s
                        devv = dev[j]
                        colourx = s
                        coloury = j
                    else:
                        nwvi = j
                        devv = dev[s]
                        colourx = j
                        coloury = s
                else:
                    nwvi = nwv.index(descr)
                    devv = overlay
                    coloury = dev.index(overlay)
                dirr = 'logs/' + nwv[nwvi] + devv + '/'
                print(i, s, j, dirr)
                plot(ax[0], ax[1], kx, ky, rx, ry, files, colours[colourx][coloury], alpha[j], (i, split), hist, thresh, j)


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
        
    plt.savefig('img/vodacom_vs_mtn_' + descr + "_" + overlay + "_" + "_".join(text.split()) + '.png')
    plt.show()
    
def splitter(r, a, limits, split):
    split, slen = split
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
    return r, lim
    
def dict_filt(dc, x, y, split, thresh):
    _debug = False
    try:
        t, limitx = thresh(dc, x, split) 
        t2, limity = thresh(dc, y, split)
        if len(t):
            t *= t2
        if _debug:
            print('dc[x]', x, len(dc[x]), 'dc[y]', y, len(dc[y]), dc[x], dc[y])
        return np.array(dc[x])[t], np.array(dc[y])[t], [limitx, limity]
    except IndexError:
        print(IndexError, 'len(dc[x]) and len(dc[y])', len(dc[x]) and len(dc[y]))
        return np.array(dc[x]), np.array(dc[y]), [None, None]

def plot(ax1, ax2, x, y, xr, yr, files, colour, alpha, split, hist, thresh, overlay_index):
    # print('plot(x, y, xr, yr, files, colour, alpha, split, hist)', x, y)
    hy = []
    ax = ax2 if ax2 else ax1
    right = True if ax2 else False
    for f in files:
        zu_mg = merge(mk(f))
        # print('zu_mg', zu_mg)
        if zu_mg:
            p, q, limits = dict_filt(zu_mg, x, y, split, thresh)
            # print('p, q', p, q)
            if len(p) and len(q):
                if hist:
                    # print('hist q/yr', q/yr)
                    if len(q):
                        hy.append(q/yr)
                    continue
                # print('plot q/yr', q/yr)
                ax.plot(p/xr, q/yr, colour, alpha=alpha)

    if hist and hy:
        # remember that ravel passes by reference, unlike flatten which passes a copy of the array
        
        # print(np.ravel(hy), len(np.ravel(hy)), type(np.ravel(hy)))
        try:
            hy = np.concatenate(np.ravel(hy))
        except ValueError:
            hy = np.ravel(hy)
        finally:
            if len(hy):
                ax.hist(hy, color=colour[0], alpha=alpha)
                if right and overlay_index == 1:
                    f1, f2, g1, g2 = plt.axis()
                    print(f1, f2, g1, g2)
                    h1, h2, u1, u2 = ax1.axis()
                    ax1.set_ylim([min(u1, g1), max(u2, g2)])
                    ax2.set_ylim([min(u1, g1), max(u2, g2)])
                axes = plt.gca()
                ly = limits[1]
                if ly[0]:
                    ly[0] /= yr
                if ly[1]:
                    ly[1] /= yr
                axes.set_xlim(ly)
                return
    axes = plt.gca()
    lx = limits[0]
    ly = limits[1]
    if lx[0]:
        lx[0] /= xr
    if lx[1]:
        lx[1] /= xr
    if ly[0]:
        ly[0] -= 1
        ly[0] /= yr
    if ly[1]:
        ly[1] /= yr
    axes.set_xlim(lx)
    axes.set_ylim(ly)
    # plt.show()

def adjust(key, val):
#     if key == 'Total power':
#         return max(-1400, val)
#     if key == 'Signal power':
#         return max(-1400, val)
#     if key == 'ECL':
#         return min(3, val)
#     if key == 'SNR':
#         return max(-200, val)
# #     if key == 'txTime':
# #         if val > 200000:
# #             return 20000
# #     if key == 'energy':
# #         return min(100000, val)
#     if key == 'TX power':
#         if val < -1000:
#             return -140
#     if key == 'EARFCN':
#         return min(10000, val)
#     if key == 'PCI':
#         if val > 1000:
#             return 0
#     if key == 'RSRQ':
#         if val < -1000:
#             return 0
    return val

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
        dt[n] = d
    dt['name'] = file
    return dt

# post processing csv {} data
def dataProcess(dt):
    dt['time'] = [0]
    for k in dt:
        for i, v in enumerate(dt[k]):
            if k == 'idleTime':
                if i > 0:
                    dt['time'].append(v + dt['txTime'][i-1] + dt['time'][i-1])
            else:
                break
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
        # print('c', len(c))
        dt.append(dataProcess(c))
    return dt

def maxHeaders(dt):
    m = 0
    maxH = []
    for d in dt:
        if len(d) > m:
            m = len(d)
            maxH = []
            for k in d:
                if str(type(d[k])) == "<class 'numpy.ndarray'>":
                    maxH.append(k)
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
                if debug: print(e, end=",")
    return merge

def mean(dt):
    mean = {}
    if debug: 
        print('dt len:', len(dt[0]))
    for k in dt[0]:
        if str(type(dt[0][k])) == "<class 'numpy.ndarray'>":
            mean[k] = []
            for d in dt:
                mean[k].append(adjust(k, np.mean(d[k])))
    return mean