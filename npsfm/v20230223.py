#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:36:04 2023

@author: mike
"""

#######################################################
### Parameters

## Base nps-fm from the 2023-02-23 version

# Rivers
river_ammonia_limits = {
    'A': {'Ammoniacal nitrogen median': (-1, 0.03),
          'Ammoniacal nitrogen Q95': (-1, 0.05)},
    'B': {'Ammoniacal nitrogen median': (-1, 0.24),
          'Ammoniacal nitrogen Q95': (-1, 0.40)},
    'C': {'Ammoniacal nitrogen median': (-1, 1.3),
          'Ammoniacal nitrogen Q95': (-1, 2.2)},
    'D': {'Ammoniacal nitrogen median': (-1, 100000),
          'Ammoniacal nitrogen Q95': (-1, 100000)}
    }

river_nitrate_limits = {'A': {'Nitrate + nitrite median': (-1, 1),
                        'Nitrate + nitrite Q95': (-1, 1.5)},
                  'B': {'Nitrate + nitrite median': (-1, 2.4),
                        'Nitrate + nitrite Q95': (-1, 3.5)},
                  'C': {'Nitrate + nitrite median': (-1, 6.9),
                        'Nitrate + nitrite Q95': (-1, 9.8)},
                  'D': {'Nitrate + nitrite median': (-1, 100000),
                        'Nitrate + nitrite Q95': (-1, 100000)}
                  }

river_ecoli_limits = {'A': {'E. coli G540': (-1, 0.05),
                      'E. coli G260': (-1, 0.2),
                      'E. coli median': (-1, 130),
                      'E. coli Q95': (-1, 540)},
                  'B': {'E. coli G540': (-1, 0.1),
                        'E. coli G260': (-1, 0.3),
                        'E. coli median': (-1, 130),
                        'E. coli Q95': (-1, 1000)},
                  'C': {'E. coli G540': (-1, 0.2),
                        'E. coli G260': (-1, 0.34),
                        'E. coli median': (-1, 130),
                        'E. coli Q95': (-1, 1200)},
                  'D': {'E. coli G540': (-1, 0.3),
                        'E. coli G260': (-1, 1.01),
                        'E. coli median': (-1, 1000000),
                        'E. coli Q95': (-1, 1000000)},
                  'E': {'E. coli G540': (-1, 1.01),
                        'E. coli G260': (-1, 1.01),
                        'E. coli median': (-1, 1000000),
                        'E. coli Q95': (-1, 1000000)}
                  }

river_mci_limits = {'A': {'MCI': (130, 100000)},
                'B': {'MCI': (110, 100000)},
                'C': {'MCI': (90, 100000)},
                'D': {'MCI': (-1, 100000)}
                }

river_drp_limits = {'A': {'Dissolved reactive phosphorus median': (-1, 0.006),
                    'Dissolved reactive phosphorus Q95': (-1, 0.021)},
                'B': {'Dissolved reactive phosphorus median': (-1, 0.01),
                      'Dissolved reactive phosphorus Q95': (-1, 0.03)},
                'C': {'Dissolved reactive phosphorus median': (-1, 0.018),
                      'Dissolved reactive phosphorus Q95': (-1, 0.054)},
                'D': {'Dissolved reactive phosphorus median': (-1, 100000),
                      'Dissolved reactive phosphorus Q95': (-1, 100000)}
                }

river_clarity_limits = {'A': {1: (1.78, 100000), 2: (0.93, 100000),
                        3: (2.95, 100000), 4: (1.38, 100000)},
                'B': {1: (1.55, 100000), 2: (0.76, 100000),
                      3: (2.57, 100000), 4: (1.17, 100000)},
                'C': {1: (1.34, 100000), 2: (0.61, 100000),
                      3: (2.22, 100000), 4: (0.98, 100000)},
                'D': {1: (-1, 100000), 2: (-1, 100000),
                      3: (-1, 100000), 4: (-1, 100000)}
                }

river_dep_sed_limits = {'A': {1: (-1, 7), 2: (-1, 10),
                        3: (-1, 9), 4: (-1, 13)},
                'B': {1: (-1, 14), 2: (-1, 19),
                      3: (-1, 18), 4: (-1, 19)},
                'C': {1: (-1, 21), 2: (-1, 29),
                      3: (-1, 27), 4: (-1, 27)},
                'D': {1: (-1, 100000), 2: (-1, 100000),
                      3: (-1, 100000), 4: (-1, 100000)}
                }

river_fish_limits = {'A': {'ibi_score': (34, 100000)},
                'B': {'ibi_score': (28, 100000)},
                'C': {'ibi_score': (18, 100000)},
                'D': {'ibi_score': (-1, 100000)}
                }

# Lakes
lake_ecoli_limits = {
    'A': {
        'E. coli G540': (-1, 0.05),
        'E. coli G260': (-1, 0.2),
        'E. coli median': (-1, 130),
        'E. coli Q95': (-1, 540)
        },
    'B': {
        'E. coli G540': (-1, 0.1),
        'E. coli G260': (-1, 0.3),
        'E. coli median': (-1, 130),
        'E. coli Q95': (-1, 1000)
        },
    'C': {
        'E. coli G540': (-1, 0.2),
        'E. coli G260': (-1, 0.34),
        'E. coli median': (-1, 130),
        'E. coli Q95': (-1, 1200)
        },
    'D': {
        'E. coli G540': (-1, 0.3),
        'E. coli G260': (-1, 1.01),
        'E. coli median': (-1, 1000000),
        'E. coli Q95': (-1, 1000000)
        },
    'E': {
        'E. coli G540': (-1, 1.01),
        'E. coli G260': (-1, 1.01),
        'E. coli median': (-1, 1000000),
        'E. coli Q95': (-1, 1000000)
        }
    }

lake_ammonia_limits = {
    'A': {'Ammoniacal nitrogen median': (-1, 0.03),
          'Ammoniacal nitrogen Q95': (-1, 0.05)},
    'B': {'Ammoniacal nitrogen median': (-1, 0.24),
          'Ammoniacal nitrogen Q95': (-1, 0.40)},
    'C': {'Ammoniacal nitrogen median': (-1, 1.3),
          'Ammoniacal nitrogen Q95': (-1, 2.2)},
    'D': {'Ammoniacal nitrogen median': (-1, 100000),
          'Ammoniacal nitrogen Q95': (-1, 100000)}
    }

lake_tp_limits = {
    'A': {'Total phosphorus median': (-1, 10)},
    'B': {'Total phosphorus median': (-1, 20)},
    'C': {'Total phosphorus median': (-1, 50)},
    'D': {'Total phosphorus median': (-1, 100000)}
    }

lake_chla_limits = {
    'A': {'Chla median': (-1, 2),
          'Chla max': (-1, 10)},
    'B': {'Chla median': (-1, 5),
          'Chla max': (-1, 25)},
    'C': {'Chla median': (-1, 12),
          'Chla max': (-1, 60)},
    'D': {'Chla median': (-1, 100000),
          'Chla max': (-1, 100000)}
    }

lake_tn_limits = {
    'A': {
        True: (-1, 160),
        False: (-1, 300),
        },
    'B': {
        True: (-1, 350),
        False: (-1, 500),
        },
    'C': {
        True: (-1, 750),
        False: (-1, 800),
        },
    'D': {
        True: (-1, 100000),
        False: (-1, 100000),
        }
    }

lake_cyano_limits = {
    'A': {'Total cyano 80th': (-1, 0.5),
          },
    'B': {'Total cyano 80th': (-1, 1),
          },
    'C': {'Total cyano 80th': (-1, 10),
          'Toxic cyano 80th': (-1, 1.8)},
    'D': {'Total cyano 80th': (-1, 100000),
          'Toxic cyano 80th': (-1, 100000)}
    }


# Combo
bottom_line_limits = {
    ('river', 'Ammonia'): {'Ammoniacal nitrogen median': (-1, 0.24),
                           'Ammoniacal nitrogen Q95': (-1, 0.40)},
    ('river', 'Nitrate'): {'Nitrate + nitrite median': (-1, 2.4),
                'Nitrate + nitrite Q95': (-1, 3.5)},
    ('river', 'MCI'): {'MCI (2021)': (90, 100000)},
    ('river', 'Clarity'): {1: (1.34, 100000), 2: (0.61, 100000),
                3: (2.22, 100000), 4: (0.98, 100000)},
    ('river', 'Dep Sediment'): {1: (-1, 21), 2: (-1, 29),
                     3: (-1, 27), 4: (-1, 27)},
    ('lake', 'Ammonia'): {'Ammoniacal nitrogen median': (-1, 0.24),
                          'Ammoniacal nitrogen Q95': (-1, 0.40)},
    ('lake', 'Cyano'): {
        'Total cyano 80th': (-1, 10),
        'Toxic cyano 80th': (-1, 1.8)
        },
    ('lake', 'Chla'): {
        'Chla median': (-1, 12),
        'Chla max': (-1, 60)
        },
    ('lake', 'Total nitrogen'): {
        True: (-1, 750),
        False: (-1, 800),
        },
    ('lake', 'Total phosphorus'): {'Total phosphorus median': (-1, 50)},
    }


parameter_special_cols_dict = {
    ('river', 'Clarity'): ['Suspended_4_class', 'Visual clarity median'],
    ('river', 'Dep Sediment'): ['Deposited_4_class', 'dep_sed_cover'],
    ('lake', 'Total nitrogen'): ['stratified', 'Total nitrogen median'],
    }

parameter_limits_dict = {
    ('river', 'Ammonia'): river_ammonia_limits,
    ('river', 'Nitrate'): river_nitrate_limits,
    ('river', 'Clarity'): river_clarity_limits,
    ('river', 'E.coli'): river_ecoli_limits,
    ('river', 'MCI'): river_mci_limits,
    ('river', 'DRP'): river_drp_limits,
    ('river', 'Dep Sediment'): river_dep_sed_limits,
    ('river', 'Fish IBI'): river_fish_limits,
    ('lake', 'Ammonia'): lake_ammonia_limits,
    ('lake', 'Cyano'): lake_cyano_limits,
    ('lake', 'Chla'): lake_chla_limits,
    ('lake', 'Total nitrogen'): lake_tn_limits,
    ('lake', 'Total phosphorus'): lake_tp_limits,
    ('lake', 'E.coli'): lake_ecoli_limits,
    }


######################################################
### Models















































































