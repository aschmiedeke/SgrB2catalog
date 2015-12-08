#!/usr/bin/env python
from __future__ import print_function

from collections import defaultdict


class Region(object):

    """
    Definition of a region

    Attributes:
        name: A string representing the name of th region.
        otype: A string specifying the type of source, e.g. 'hii'.
        coord: A string giving the center coordinates in sexagesimal format.
        ctype: A string representing the type of the coordinate system.
        epoch: A float giving the epoch of the observation.
        stype: A string representing the shape of the region.
        shape: A string containing comma separated floats. Depending on the stype provides e.g. width and height.
        sunit: A string giving the unit of the floats specified in shape.
        ref: A string representing the paper reference.
        freq: A float giving the frequency of the observation.
        funit: A string representing the frequency unit.
        text: A string providing additional text to be given in the label. Defaults to empty string.

    """

    def __init__(self, name, otype, coord, ctype, epoch, stype, shape, sunit, ref, freq, funit, text=''):

        self.name = name
        self.otype = otype
        self.coord = coord
        self.ctype = ctype
        self.epoch = epoch
        self.stype = stype
        self.shape = shape
        self.sunit = sunit
        self.ref = ref
        self.freq = freq
        self.funit = funit
        self.text = text



def createDictionary():
    #
    #   stype           shape
    #----------------------------------------------
    #   'circle'        'radius'
    #   'ellipse'       'radius, radius, angle'
    #   'box'           'width, height, angle'
    #   'polygon'       'x2, y2, x3, y3, ...'           Note: center coordinate defines here: x1, y1
    #

    regions = []
    regions.append(Region('A', 'hii', '17:44:09.697 -28:21:57.60', 'equatorial', 1950, 'ellipse', '1.70, 1.10, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('B', 'hii', '17:44:10.094 -28:22:00.71', 'equatorial', 1950, 'ellipse', '0.60, 0.54, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('C', 'hii', '17:44:10.207 -28:22:16.00', 'equatorial', 1950, 'ellipse', '1.00, 1.00, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz', 'not detected'))
    regions.append(Region('D', 'hii', '17:44:10.244 -28:22:10.53', 'equatorial', 1950, 'ellipse', '0.80, 0.58, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('E', 'hii', '17:44:10.289 -28:22:06.52', 'equatorial', 1950, 'ellipse', '1.10, 0.61, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('F', 'hii', '17:44:10.358 -28:22:02.50', 'equatorial', 1950, 'ellipse', '1.90, 1.10, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('G', 'hii', '17:44:10.467 -28:22:00.95', 'equatorial', 1950, 'ellipse', '1.10, 0.48, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('H', 'hii', '17:44:10.606 -28:22:42.81', 'equatorial', 1950, 'ellipse', '1.10, 0.80, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('I', 'hii', '17:44:10.608 -28:22:02.90', 'equatorial', 1950, 'ellipse', '4.30, 3.30, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz'))
    regions.append(Region('J', 'hii', '17:44:10.662 -28:21:53.80', 'equatorial', 1950, 'ellipse', '1.00, 1.00, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz', 'not detected'))
    regions.append(Region('K', 'hii', '17:44:10.281 -28:21:11.80', 'equatorial', 1950, 'ellipse', '1.00, 1.00, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz', 'not detected'))
    regions.append(Region('L', 'hii', '17:44:12.960 -28:20:54.40', 'equatorial', 1950, 'ellipse', '1.00, 1.00, 0.0', 'arcsec', 'Benson, 1984', 15.0, 'GHz', 'not detected'))

    regions.append(Region('A', 'hii', '17:44:09.697 -28:21:57.60', 'equatorial', 1950, 'ellipse', '1.0, 1.0, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz', 'not clear'))
    regions.append(Region('B', 'hii', '17:44:10.094 -28:22:00.71', 'equatorial', 1950, 'ellipse', '2.7, 1.6, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('C', 'hii', '17:44:10.207 -28:22:16.00', 'equatorial', 1950, 'ellipse', '1.9, 1.1, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('D', 'hii', '17:44:10.244 -28:22:10.53', 'equatorial', 1950, 'ellipse', '2.4, 0.7, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('E', 'hii', '17:44:10.289 -28:22:06.52', 'equatorial', 1950, 'ellipse', '2.6, 1.6, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('F', 'hii', '17:44:10.358 -28:22:02.50', 'equatorial', 1950, 'ellipse', '2.6, 2.1, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('G', 'hii', '17:44:10.467 -28:22:00.95', 'equatorial', 1950, 'ellipse', '1.0, 1.0, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz', 'not resolved'))
    regions.append(Region('H', 'hii', '17:44:10.606 -28:22:42.81', 'equatorial', 1950, 'ellipse', '2.5, 1.7, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('I', 'hii', '17:44:10.608 -28:22:02.90', 'equatorial', 1950, 'ellipse', '4.5, 3.6, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('J', 'hii', '17:44:10.662 -28:21:53.80', 'equatorial', 1950, 'ellipse', '4.0, 6.0, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('K', 'hii', '17:44:10.281 -28:21:11.80', 'equatorial', 1950, 'ellipse', '13.0, 16.0, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))
    regions.append(Region('L', 'hii', '17:44:12.960 -28:20:54.40', 'equatorial', 1950, 'ellipse', '6.0, 9.0, 0.0', 'arcsec', 'Benson, 1984', 5.0, 'GHz'))

    regions.append(Region('F1a', 'hii', '17:44:10.3150 -28:22:01.274', 'equatorial', 1950, 'ellipse', '0.130, 0.090, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F1b', 'hii', '17:44:10.3032 -28:22:01.613', 'equatorial', 1950, 'ellipse', '0.190, 0.070, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F1c', 'hii', '17:44:10.3226 -28:22:01.586', 'equatorial', 1950, 'ellipse', '0.170, 0.130, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F1d', 'hii', '17:44:10.3305 -28:22:01.707', 'equatorial', 1950, 'ellipse', '0.180, 0.100, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F1e', 'hii', '17:44:10.3261 -28:22:01.929', 'equatorial', 1950, 'ellipse', '0.040, 0.020, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F1f', 'hii', '17:44:10.3453 -28:22:01.579', 'equatorial', 1950, 'ellipse', '0.130, 0.090, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F1g', 'hii', '17:44:10.3638 -28:22:01.579', 'equatorial', 1950, 'ellipse', '0.150, 0.070, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F2a', 'hii', '17:44:10.3468 -28:22:01.287', 'equatorial', 1950, 'ellipse', '0.090, 0.050, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F2b', 'hii', '17:44:10.3531 -28:22:01.399', 'equatorial', 1950, 'ellipse', '0.090, 0.060, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F2c', 'hii', '17:44:10.3599 -28:22:01.421', 'equatorial', 1950, 'ellipse', '0.150, 0.110, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F2d', 'hii', '17:44:10.3590 -28:22:01.303', 'equatorial', 1950, 'ellipse', '0.160, 0.080, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F3a', 'hii', '17:44:10.3555 -28:22:02.581', 'equatorial', 1950, 'ellipse', '0.100, 0.060, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F3b', 'hii', '17:44:10.3590 -28:22:02.482', 'equatorial', 1950, 'ellipse', '0.240, 0.090, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F3c', 'hii', '17:44:10.3619 -28:22:02.112', 'equatorial', 1950, 'ellipse', '0.080, 0.060, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F3e', 'hii', '17:44:10.4152 -28:22:02.370', 'equatorial', 1950, 'ellipse', '0.080, 0.040, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F4a', 'hii', '17:44:10.3943 -28:22:01.688', 'equatorial', 1950, 'ellipse', '0.130, 0.080, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F4b', 'hii', '17:44:10.4040 -28:22:02.070', 'equatorial', 1950, 'ellipse', '0.100, 0.100, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz', 'not clear'))
    regions.append(Region('F4c', 'hii', '17:44:10.4285 -28:22:01.364', 'equatorial', 1950, 'ellipse', '0.110, 0.080, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F10.37', 'hii', '17:44:10.3693 -28:22:03.694', 'equatorial', 1950, 'ellipse', '0.095, 0.062, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('F10,38', 'hii', '17:44:10.3837 -28:22:04.288', 'equatorial', 1950, 'ellipse', '0.079, 0.065, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))
    regions.append(Region('G', 'hii', '17:44:10.4812 -28:22:00.790', 'equatorial', 1950, 'ellipse', '0.100, 0.111, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz', 'not clear'))
    regions.append(Region('G10.47', 'hii', '17:44:10.4782 -28:22:00.070', 'equatorial', 1950, 'ellipse', '0.100, 0.100, 0.0', 'arcsec', 'dePree, 1998', 42.8, 'GHz', 'not clear'))

    #regions.append(Region('', 'hii', '', 'equatorial', 1950, 'ellipse', '', 'arcsec', 'dePree, 1998', 42.8, 'GHz'))

    #
    # store information in list containing sub-dictionaries

    regiondicts=[]
    for r in regions:
        regiondicts.append({'name': r.name, 'otype': r.otype, 'coord': r.coord, 'ctype': r.ctype, 'epoch': r.epoch,
                        'stype': r.stype, 'shape': r.shape, 'sunit': r.sunit, 'text': r.text,
                        'ref': r.ref, 'freq': r.freq, 'funit': r.funit})
    return regiondicts
