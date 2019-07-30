import numpy as np
import matplotlib.pyplot as plt
import glob

print('custom jupyter library imported')

dirr = ""
debug = False

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
            if k == 'ECL':
                if v > 2:
                    dt[k][i] = -1
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
    # print('files', files)
    dt = []
    file_list = []
    if str(type(files)) == "<class 'str'>":
        file_list = glob.glob(dirr + files)
    else:
        for fl in files:
            file_list.append(dirr + fl)
    # print('files2', files)
    for f in file_list:
        # print('filefff', f)
        c = csvToDict(f)
        # print('c', len(c))
        dt.append(dataProcess(c))
    return dt

def adjust(key, val):
    if key == 'Signal power':
        return max(-1300, val)
    if key == 'ECL':
        return min(3, val)
    if key == 'SNR':
        return max(-200, val)
    if key == 'txTime':
        if val > 200000:
            return 20000
    return val

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