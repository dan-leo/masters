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
        print(UnicodeDecodeError)
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

def datasetPlot(dt, length=1000, time=False):
    h = len(dt[0])/2 + 1
    rainbow = ['g-*', 'r-*', 'b-*', 'y-*', 'k*', 'm*', 'c*']
    plt.figure(figsize=(h,h))
    i = 1
    for k in dt[0]:
        
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
                plt.plot(t, d[k][:l], rainbow[j])
            except KeyError:
                pass
        i += 1
    plt.show()