import numpy as np

datepath = "AllResults.txt"
referencepath = 'tempfile.txt'
datafile = open(datepath, 'rb')
referencefile = open(referencepath, 'rb')
datafile = datafile.readlines()
datafile = [x.strip() for x in datafile]
datafile = [x.split(',') for x in datafile]
numtotal = len(datafile)
ids = []
start = []
for i in range(numtotal):
    tmpid = datafile[i][0]
    if tmpid not in ids:
        ids.append(tmpid)  # ids
        start.append(i)  # start indexes
    else:
        pass
runlen = len(start)
for i in range(len(ids)):
    if i != runlen-1:
        numobs = int(start[i+1]) - int(start[i])
    else:
        numobs = len(datafile) - int(start[i])
    print numobs
    tmpflux = []
    for j in range(numobs):
        tmpflux.append(float(datafile[start[i]+j][2]))
    fluxstd = np.std(tmpflux)
referencefile = referencefile.readlines()
referencefile = [x.strip() for x in referencefile]
referencefile = [x.split(' ') for x in referencefile]
