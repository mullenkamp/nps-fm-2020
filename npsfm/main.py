#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:00:43 2023

@author: mike
"""
import os
import pathlib
import pandas as pd
import numpy as np
from copy import copy
import booklet

from . import v202401, utils
# import v202401, utils


pd.options.display.max_columns = 10

######################################################
### Parameters

# features = set([limits[0] for limits in v202401.parameter_limits_dict])
# indicators = set([limits[1] for limits in v202401.parameter_limits_dict])



#######################################################
### Functions







###################################################
### Classes


# class ImportData:
#     """

#     """
#     def __init__(self, ts_data=None, indicator=None, nzsegment=None):
#         """

#         """



#     def add_data(self, ts_data, indicator, feature):
#         """

#         """
#         ## Checks
#         if not isinstance(ts_data, pd.Series):
#             raise TypeError('ts_data must be a pandas Series with a datetime index.')
#         if not isinstance(ts_data.index, pd.DatetimeIndex):
#             raise TypeError('ts_data must be a pandas Series with a datetime index.')
#         if indicator not in indicators:
#             raise ValueError(f'indicator must be one of {indicators}')
#         if feature not in features:
#             raise ValueError(f'feature must be one of {features}')




#     def add_nzsegment(self, nzsegment):
#         """

#         """





class NPSFM:
    """

    """
    def __init__(self, package_data_path, download_files=False, only_missing=True):
        """

        """
        ## File check
        missing_files = utils.check_files(package_data_path)
        if missing_files:
            if download_files:
                utils.download_files(package_data_path, only_missing=only_missing)
            else:
                raise ValueError('There are missing data files. Files would have been downloaded if download_files=True (but it is not). Othersize if this was a mistake, please check/change the data_path: {}'.format(', '.join([os.path.split(f)[-1] for f in missing_files])))

        self.data_path = pathlib.Path(package_data_path)

        ## Run checks to see what parameters are available to calc grades


    def add_data(self, ts_data, parameter, feature, nzsegment):
        """

        """
        ## Checks
        if not isinstance(ts_data, pd.Series):
            raise TypeError('ts_data must be a pandas Series with a datetime index.')
        if not isinstance(ts_data.index, pd.DatetimeIndex):
            raise TypeError('ts_data must be a pandas Series with a datetime index.')
        feature_parameter = (feature, parameter)
        if feature_parameter not in v202401.parameter_limits_dict:
            raise ValueError(f'The combo of {feature_parameter} must be one of {list(v202401.parameter_limits_dict.keys())}')
        with booklet.open(self.data_path.joinpath('rec_classes.blt')) as f:
            if nzsegment not in f:
                raise ValueError(f'{nzsegment} not a valid nzsegment.')
            else:
                tags = f[nzsegment]

        ## Determine the associated limits for the site and parameter
        limits = utils.get_limits(feature_parameter, tags)

        bl_limit_state = v202401.bottom_line_limits[feature_parameter]
        bl_limit = limits[bl_limit_state]

        ## Save data
        self.ts_data = ts_data
        self.parameter = parameter
        self.feature = feature
        self.feature_parameter = feature_parameter
        self.nzsegment = nzsegment
        self.class_tags = tags
        self.bottom_line_limit_state = bl_limit_state
        self.bottom_line_limit = bl_limit
        self.limits = limits
        self.stats = utils.calc_stats(ts_data, limits)

        return copy(self)


    def calc_state(self):
        """

        """
        result = utils.calc_state_from_limit(self.stats, self.limits)

        return result


    def calc_improvement_to_state(self, state):
        """

        """
        if state not in self.limits:
            raise ValueError(f'{state} not in the available states: {list(self.limits.keys())}')

        results = utils.calc_improvement_to_state(self.stats, self.limits, state)

        return results


    def calc_improvement_to_bottom_line(self):
        """

        """
        results = utils.calc_improvement_to_state(self.stats, self.limits, self.bottom_line_limit_state)

        return results




####################################################
### Testing























































