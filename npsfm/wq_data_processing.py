#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:40:44 2023

@author: mike
"""
import io
import os
import pathlib
import pandas as pd
import geopandas as gpd
import nzrec

pd.options.display.max_columns = 10


#######################################################
### Parameters

data_path = pathlib.Path('/media/nvme1/Projects/aquanet/Greater Wellington Eastern Wairarapa/data')

rec_mapping_csv = '/media/nvme1/data/NIWA/REC25_rivers/rec2_to_rec1_mapping.csv'

river_reaches_path = data_path.joinpath('river_reaches_all_order.gpkg')
river_catches_path = data_path.joinpath('river_catchments.gpkg')

nzrec_data_path = '/media/nvme1/git/nzrec/data'

## Conc data
mfe_data_path = pathlib.Path('/media/nvme1/data/mfe')

base_cols = ['measr_b', 'measure', 'units', 'nzsgmnt', 'strm_rd', 'value', 'mesrmnt', 'climate', 'src_f_f']
main_cols = ['measr_b', 'units', 'nzsgmnt', 'value', 'mesrmnt']

nitrogen_csv = 'river-water-quality-nitrogen-modelled-2016-2020.csv'
phos_csv = 'river-water-quality-phosphorus-modelled-2016-2020.csv'
turb_csv = 'river-water-quality-clarity-and-turbidity-modelled-2016-2020.csv'
ecoli_csv = 'river-water-quality-escherichia-coli-modelled-2016-2020.csv'
macro_csv = 'river-water-quality-macroinvertebrate-community-index-modell.csv'
fish_csv = 'fish-index-of-biotic-integrity-1998-2018.csv'
sed_csv = 'sediment-classes-for-rec24-nzsegments.csv'
# dep_sed_csv = 'deposited-sediment-in-rivers-2014-2019.csv'
dep_sed_csv = 'predicted-reference-and-current-streambed-deposited-fine-sed.csv'

## Output
# agg_conc_csv = 'wairarapa_stream_data.csv'
agg_conc_feather = 'river_data.feather'

#####################################################
### Processing

## Get the necessary reaches
# geo1 = gpd.read_file(river_reaches_path, include_fields=['nzsegment', 'catchment_name'])
# geo1['segment_length'] = geo1.geometry.length.round().astype('int32')
# reaches_df = pd.DataFrame(geo1.drop('geometry', axis=1))

## nitrogen
# n0 = pd.read_csv(mfe_data_path.joinpath(nitrogen_csv), usecols=main_cols)
# n0 = n0.rename(columns={'measr_b': 'measurement', 'nzsgmnt': 'nzsegment', 'mesrmnt': 'mtype'})

# n1 = pd.merge(reaches_df, n0, on='nzsegment')

## phosphorus
# phos0 = pd.read_csv(mfe_data_path.joinpath(phos_csv), usecols=main_cols)
# phos0 = phos0.rename(columns={'measr_b': 'measurement', 'nzsgmnt': 'nzsegment', 'mesrmnt': 'mtype'})

# phos1 = pd.merge(reaches_df, phos0, on='nzsegment')

## turbidity
# turb0 = pd.read_csv(mfe_data_path.joinpath(turb_csv), usecols=main_cols)
# turb0 = turb0.rename(columns={'measr_b': 'measurement', 'nzsgmnt': 'nzsegment', 'mesrmnt': 'mtype'})

# turb1 = pd.merge(reaches_df, turb0, on='nzsegment')

## e.coli
# ecoli0 = pd.read_csv(mfe_data_path.joinpath(ecoli_csv), usecols=main_cols)
# ecoli0 = ecoli0.rename(columns={'measr_b': 'measurement', 'nzsgmnt': 'nzsegment', 'mesrmnt': 'mtype'})

# ecoli1 = pd.merge(reaches_df, ecoli0, on='nzsegment')

## macro
# macro0 = pd.read_csv(mfe_data_path.joinpath(macro_csv), usecols=main_cols)
# macro0 = macro0.rename(columns={'measr_b': 'measurement', 'nzsgmnt': 'nzsegment', 'mesrmnt': 'mtype'})

# macro1 = pd.merge(reaches_df, macro0, on='nzsegment')

## fish
fish0 = pd.read_csv(mfe_data_path.joinpath(fish_csv), usecols=['nzreach', 'ibi_score'])
fish0 = fish0.rename(columns={'nzreach': 'rec1_nzsegment'}).dropna()

rec_map0 = pd.read_csv(rec_mapping_csv).drop_duplicates(subset=['rec1_nzsegment'])
fish1 = pd.merge(rec_map0, fish0, on='rec1_nzsegment').drop('rec1_nzsegment', axis=1)

# fish1 = pd.merge(reaches_df, fish0, on='nzsegment')

## sediment classes
sed0 = pd.read_csv(mfe_data_path.joinpath(sed_csv), usecols=['nzsegment', 'AmmendedCSOFG', 'Deposited_4_class', 'Suspended_4_class'])
sed0 = sed0.replace({'Deposited_4_class': {'naturally soft-bottomed': 0}})
# sed0.to_csv(mfe_data_path.joinpath(sed_csv), index=False)
# sed0 = sed0.rename(columns={'measr_b': 'measurement', 'nzsgmnt': 'nzsegment', 'mesrmnt': 'mtype'})
sed0['Suspended_4_class'] = sed0['Suspended_4_class'].astype('int8')
sed0['Deposited_4_class'] = sed0['Deposited_4_class'].astype('int8')

# sed1 = pd.merge(reaches_df, sed0, on='nzsegment')

## deposited sediment
sed1 = pd.read_csv(mfe_data_path.joinpath(dep_sed_csv), usecols=['NZREACH', 'BRT_ALL_O'])
sed1 = sed1.rename(columns={'NZREACH': 'rec1_nzsegment', 'BRT_ALL_O': 'dep_sed_cover'}).dropna()
sed1 = pd.merge(rec_map0, sed1, on='rec1_nzsegment').drop('rec1_nzsegment', axis=1)

### Already available in nzrec
w0 = nzrec.Water(nzrec_data_path)

# reach_tags = {way_id: w0._way_tag[way_id] for way_id in reaches_df.nzsegment.unique()}

reaches_list = []
for seg, reaches in w0._way_tag.items():
    r1 = pd.DataFrame.from_dict([reaches])
    r1['nzsegment'] = seg
    reaches_list.append(r1)

reaches_data = pd.concat(reaches_list).drop('Catchment name', axis=1)
reaches_data1 = pd.merge(reaches_df, reaches_data, on='nzsegment')
reaches_data1 = pd.merge(reaches_data1, sed0, on='nzsegment')
reaches_data1 = pd.merge(reaches_data1, fish1, on='nzsegment', how='left')
reaches_data1 = pd.merge(reaches_data1, sed1, on='nzsegment', how='left')

reaches_data1['nzsegment'] = reaches_data1['nzsegment'].astype('int32')
# reaches_data1['end_seg'] = reaches_data1['end_seg'].astype('int32')

reaches_data1.to_csv(data_path.joinpath(agg_conc_csv), index=False)
reaches_data1.to_feather(data_path.joinpath(agg_conc_feather))




########################################################
### REC network

rec_rivers_shp = '/media/data01/data/niwa/rec/rec25_rivers_clean.shp'
rec_rivers_fgb = '/media/data01/data/niwa/rec/rec25_rivers_clean.fgb'
rec_rivers_feather = '/media/data01/data/niwa/rec/rec25_rivers_clean.feather'


rec_rivers0 = gpd.read_file(rec_rivers_shp)
rec_rivers0.rename(columns={'stream_ord': 'stream_order'}, inplace=True)

rec_rivers0.to_file(rec_rivers_fgb, driver='FlatGeobuf')

b1 = io.BytesIO()
rec_rivers0.to_file(b1, driver='FlatGeobuf')

rr0 = gpd.read_file(b1, engine='fiona', driver='FlatGeobuf')
rr0 = gpd.read_feather(rec_rivers_feather)


































