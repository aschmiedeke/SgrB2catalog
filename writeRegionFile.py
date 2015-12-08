#!/usr/bin/env python
from __future__ import print_function

import createDictionary
import astropy.coordinates as coord
import astropy.units as u
import pyregion
from pyregion.parser_helper import Shape


#--------------------------------------------------
def search(dictionary_list, searchFor):
    """
    Obtain the position of an entry for a given searchString in a keyword. (TypeErrors will be ignored).

    Keywords:
        dictionary -- name of the dictionary to be searched
        searchFor -- a string or integer that should be searched

    Returns:
        result -- list of indices of matches.

    """

    str_keys = [k for k in dictionary_list[0] if hasattr(dictionary_list[0][k], 'find')]
    return [row for row in dictionary_list
            if any([searchFor in val
                    for val in
                    [row[k] for k in str_keys]])]

    #for keyword in dictionary:
    #    try:
    #        for e, entry in enumerate(dictionary[keyword]):
    #            if searchFor in entry:
    #                result.append(e)

    #    except TypeError:
    #        #print "TypeError (\"%s\") --> continue with next keyword" % keyword
    #        continue

    #return result


#---------------------------------------------------------

def writeRegionFile(outname, catalog, matches, color='blue', width=2,
                    fonttype='helvetica', fontsize=10, fontweight='normal',
                    fontfamily='roman'):
    '''
    Writes the region file.

    Keywords:
        outname -- A string containing the name of the output file.
        gParam -- A dictionary of global setup parameters.
        catalog -- A dictionary containing the different region.
        matches -- A list containing the indices matching the search keyword(s).

    '''

    fontpars = dict(fontweight=fontweight, fonttype=fonttype,
                    fontfamily=fontfamily, fontsize=fontsize)

    shapeList = []

    for row in matches:

        name = row['name']
        stype = row['stype']
        coords = row['coord']
        epoch = row['epoch']
        shape = row['shape']
        sunit = row['sunit']
        text = row['text']

 
        #
        # do some coordinate system conversion, if necessary

        if 'equatorial' in row['ctype']:
            if epoch == 1950:
                frame = coord.FK4
                pos = coord.SkyCoord(coords, frame=frame, unit=(u.hourangle, u.deg))
                pos_fk5 = pos.fk5

            elif epoch == 2000:
                frame = coord.FK5
                pos_fk5 = coord.SkyCoord(coords, frame=frame, unit=(u.hourangle, u.deg))

            else:
                print("Cannot read epoch and/or ctype. Skipping index %i" % index)
                continue


        if 'ellipse' in stype:

            shape_list = shape.split(',')

            rmaj = u.Quantity(float(shape_list[0].strip()), sunit)
            rmin = u.Quantity(float(shape_list[1].strip()), sunit)
            rpa = shape_list[2].strip()

            shape = Shape(stype,
                          (pyregion.region_numbers.SimpleNumber(pos_fk5.ra.deg),
                           pyregion.region_numbers.SimpleNumber(pos_fk5.dec.deg),
                           pyregion.region_numbers.AngularDistance('{0}"'.format(rmaj.to(u.arcsec).value)),
                           pyregion.region_numbers.AngularDistance('{0}"'.format(rmin.to(u.arcsec).value)),
                           pyregion.region_numbers.AngularDistance(rpa),))
            shape.coord_format = 'fk5'
            shape.attr = ([],{})
            shape.attr[1].update({'color': color,
                                  'text': "{0}{2}{1}".format(name,text, ", " if text else ""),
                                  'width': str(width),
                                  'font': "{fonttype} {fontsize} {fontweight} {fontfamily}".format(**fontpars),
                                 })
            shape.coord_list = [pos_fk5.ra.deg, pos_fk5.dec.deg,
                                rmaj.to(u.deg).value, rmin.to(u.deg).value,
                                float(rpa)]
            shape.comment = "text={{{text}}}".format(**shape.attr[1])
            print(shape, shape.attr)





        shapeList.append(shape)

    SL = pyregion.ShapeList(shapeList)
    SL.write(outname)

    return SL


#---------------------------------------------------------
if __name__ == '__main__':

    #
    # create the dictionary

    catalog = createDictionary.createDictionary()

    #
    # search the dictionary; obtain a list of the position of the matches in the dictionary
    # TODO: Make this a keyword.

    searchString = 'Benson'

    matches = search(catalog, searchString)
    print(matches)
    print("Found %i / %i matches." % (len(matches), len(catalog)))

    #
    # provide some general parameters for the regions file setup
    # TODO: Make this keywords.

    outname = 'sample.reg'

    gParam = {'color': 'blue',
              'width': 2,
              'fonttype': 'helvetica',
              'fontsize': 10}

    sl = writeRegionFile(outname, catalog, matches, **gParam)
