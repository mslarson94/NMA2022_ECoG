## Grabbing data & initializing plotting parameters 
# @title Data retrieval
import os, requests
from matplotlib import rcParams
from matplotlib import pyplot as plt
import numpy as np

def grabData():
    fname = 'memory_nback.npz'
    url = "https://osf.io/xfc7e/download"
    if not os.path.isfile(fname):
        try:
            r = requests.get(url)
        except requests.ConnectionError:
            print("!!! Failed to download data !!!")
        else:
            if r.status_code != requests.codes.ok:
                print("!!! Failed to download data !!!")
            else:
                with open(fname, "wb") as fid:
                    fid.write(r.content)
    rcParams['figure.figsize'] = [20, 4]
    rcParams['font.size'] = 15
    rcParams['axes.spines.top'] = False
    rcParams['axes.spines.right'] = False
    rcParams['figure.autolayout'] = True
    
    alldat = np.load(fname, allow_pickle=True)['dat']
    
    return alldat, rcParams

