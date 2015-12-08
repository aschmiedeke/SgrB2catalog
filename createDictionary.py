#!/usr/bin/env python
from __future__ import print_function

import numpy as np
from collections import defaultdict
from astropy.table import Table
import json

def createDictionary():
    with open('catalog.json','r') as f:
        regiondicts = json.load(f)

    return regiondicts

def makeTable(regiondicts, default={int: 0, str: "", float: 0.0, np.float64: 0.0, np.float:0.0, np.int: 0}):

    colnames = [k for k in regiondicts[0]]
    dtypes = {k: dtype(regiondicts[0][k]) for k in regiondicts[0]}
    complete = False

    while not complete:
        complete=True
        for row in regiondicts:
            for cn in colnames:
                if cn not in row:
                    row[cn] = default[dtypes[cn]]
            for cn in row:
                if cn not in colnames:
                    colnames.append(cn)
                    dtypes[cn] = dtype(row[cn])
                    complete = False

    tbl = Table(regiondicts)

    return tbl

def dtype(x):
    return x.dtype.type if hasattr(x, 'dtype') else type(x)
