#!/usr/bin/env python3

'''
This script is written by @jniimi_as_jack, 
with intended that it will be run on Google Colab Pro+.
'''

from time import sleep
import pandas as pd
from datetime import datetime as dt
from requests import get
from json import dumps
from random import randint
from tqdm import tqdm

DIR  = '/content/drive/MyDrive/data/investment/'
BASE = 'https://api.bitflyer.com/v1/'
URL = BASE + 'getticker'

def get_price(i):
    r = get(URL, params={'product_code':'ETH_JPY'}).json()
    r = pd.DataFrame(r, index=[i+1])
    return r

def get_Tsec_data(T, wait_sec):
    for i in tqdm(range(T)):
        r = get_price(i = i)
        d = r if i==0 else d = pd.concat([d, r], axis = 0)
        sleep(wait_sec)
    fname = DIR+'rawSequence_'+str(randint(100000000,999999999))+'.pkl'
    print('Saved:',fname)
    d.to_pickle(fname)
