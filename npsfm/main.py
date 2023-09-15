#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:00:43 2023

@author: mike
"""
import pandas as pd
import numpy as np

import v20230223



pd.options.display.max_columns = 10

######################################################
### Parameters




#######################################################
### Functions



def get_required_cols(limits):
    """

    """
    cols = set(['nzsegment'])
    for band, limit in limits.items():
        cols.update(set(list(limit.keys())))

    return list(cols)


def assign_bands_normal(feature, parameter, data, limits):
    """

    """
    b0 = data[['nzsegment']].copy()
    b0[parameter] = 'NA'
    bool_series = b0.set_index(['nzsegment'])[parameter]

    for band, limit in reversed(limits.items()):
        bool_list = []
        for col, minmax in limit.items():
            min1, max1 = minmax
            bool0 = (data[col] > min1) & (data[col] <= max1)
            bool_list.append(bool0)

        bool1 = pd.concat(bool_list, axis=1)
        bool_series[bool1.all(axis=1).values] = band

    return bool_series


def assign_bands_for_parameter(feature, parameter, data):
    """

    """
    key = (feature, parameter)

    ## Get the limits
    limits = v20230223.parameter_limits_dict[key]

    ## Check that the data has the required cols
    if parameter in v20230223.parameter_special_cols_dict:
        cols = v20230223.parameter_special_cols_dict[parameter].copy()
    else:
        cols = get_required_cols(limits)

    if not all(np.in1d(cols, data.columns)):
        raise ValueError('Not all required columns are in the data.')

    ## Run the calcs
    if key in v20230223.parameter_special_cols_dict:
        b0 = data[cols[:2]].copy()
        b0[parameter] = 'NA'
        bool_series = b0.set_index(cols[:2])[parameter].sort_index()
        for band, limit in reversed(limits.items()):
            bool_list = []
            for col, minmax in limit.items():
                min1, max1 = minmax
                bool0 = (data[cols[-1]] >= min1) & (data[cols[-1]] < max1)
                bool0.name = col
                bool_list.append(bool0)

            bool1 = pd.concat(bool_list, axis=1)
            bool1['nzsegment'] = data['nzsegment']
            bool2 = bool1.set_index('nzsegment').stack().sort_index()
            bool2.index.names = cols[:2]

            bool_series.loc[bool_series.index.isin(bool2.loc[bool2].index)] = band

        data0 = pd.merge(data[cols[:2]], bool_series.reset_index(), on=cols[:2], how='left').drop(cols[1], axis=1).set_index('nzsegment')
    else:
        data0 = assign_bands_normal(parameter, data, limits)

    return data0




###################################################
### Class


class NPSFM:
    """

    """
    def __init__(self, data):
        """

        """
        ## Run checks to see what parameters are available to calc grades

























































