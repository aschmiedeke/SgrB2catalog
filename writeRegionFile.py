#!/usr/bin/env python

import createDictionary
import astropy.coordinates as coord
import astropy.units as u


#--------------------------------------------------
def search(dictionary, searchFor):
    """
    Obtain the position of an entry for a given searchString in a keyword. (TypeErrors will be ignored).

    Keywords:
        dictionary -- name of the dictionary to be searched
        searchFor -- a string or integer that should be searched

    Returns:
        result -- list of indices of matches.

    """

    result = []

    for keyword in dictionary:
        try:
            for e, entry in enumerate(dictionary[keyword]):
                if searchFor in entry:
                    result.append(e)

        except TypeError:
            #print "TypeError (\"%s\") --> continue with next keyword" % keyword
            continue

    return result


#---------------------------------------------------------
def writeRegionFile(outname, gParam, catalog, matches):
    '''
    Writes the region file.

    Keywords:
        outname -- A string containing the name of the output file.
        gParam -- A dictionary of global setup parameters.
        catalog -- A dictionary containing the different region.
        matches -- A list containing the indices matching the search keyword(s).

    '''

    f = open(outname, 'w')

    f.write('# Region file for:at: DS9 version 4.1\n')
    f.write('global color=%s dashlist=8 3 width=%i font=\"%s %.1f normal roman\" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
            % (gParam['color'], gParam['width'], gParam['fonttype'], gParam['fontsize']))
    f.write('fk5\n')

    for index in matches:

        name = catalog['name'][index]
        stype = catalog['stype'][index]
        coords = catalog['coord'][index]
        epoch = catalog['epoch'][index]
        shape = catalog['shape'][index]
        sunit = catalog['sunit'][index]
        text = catalog['text'][index]

        #
        # do some coordinate system conversion, if necessary

        if 'equatorial' in catalog['ctype'][index]:
            if epoch == 1950:
                frame = coord.FK4
                pos = coord.SkyCoord(coords, frame=frame, unit=(u.hourangle, u.deg))
                pos_fk5 = pos.fk5

            elif epoch == 2000:
                frame = coord.FK5
                pos_fk5 = coord.SkyCoord(coords, frame=frame, unit=(u.hourangle, u.deg))

            else:
                print "Cannot read epoch and/or ctype. Skipping index %i" % index
                continue


        #
        # get the size

        if 'ellipse' in stype:

            shape_list = shape.split(',')

            rmaj = shape_list[0]
            rmin = shape_list[1]
            rpa = shape_list[2]

        if 'arcsec' in sunit:
            unit = '"'

        #
        # combine the label

        if text != '':
            label = '%s, %s' % (name, text)
        else:
            label = '%s' % name

        f.write('%s(%.5f, %.5f, %s%s, %s%s, %s) # text={%s}\n' % (stype, pos_fk5.ra.deg, pos_fk5.dec.deg,
                                                                rmaj, unit, rmin, unit, rpa, label))
    f.close()


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
    print "Found %i / %i matches." % (len(matches), len(catalog['name']))

    #
    # provide some general parameters for the regions file setup
    # TODO: Make this keywords.

    outname = 'sample.reg'

    gParam = {'color': 'blue',
              'width': 2,
              'fonttype': 'helvetica',
              'fontsize': 10}

    writeRegionFile(outname, gParam, catalog, matches)
