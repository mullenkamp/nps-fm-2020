#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:53:36 2024

@author: mike
"""
import pandas as pd
import os
import pathlib
import pytest

from npsfm import NPSFM

########################################################3
### Parameters

script_path = pathlib.Path(os.path.realpath(os.path.dirname(__file__)))
data_path = script_path.parent.parent.joinpath('data')

nzsegment = 3076139
parameter = 'Nitrate'
feature = 'river'
version = 'v202401'
hopeful_state = 'A'

########################################################
### Test

ts_data = pd.read_csv(script_path.joinpath('test_data1.csv.zip'), index_col=0, parse_dates=True)['value']


self = NPSFM(data_path)


def test_add_limits():
    limits = self.add_limits(parameter, feature, nzsegment)

    assert len(limits) == 4


limits = self.add_limits(parameter, feature, nzsegment)


def test_add_stats():
    stats = self.add_stats(ts_data)

    assert len(stats) == 2


stats = self.add_stats(ts_data)


def test_calc_state():
    attr_state = self.calc_state(only_median=True)
    attr_state = self.calc_state(only_median=False)

    assert attr_state == 'C'


def test_calc_improvement_to_state():
    improve_ratio1 = self.calc_improvement_to_state(hopeful_state)
    improve_ratio2 = self.calc_improvement_to_bottom_line()

    assert (len(improve_ratio1) == 2) and len(improve_ratio2) == 2































































