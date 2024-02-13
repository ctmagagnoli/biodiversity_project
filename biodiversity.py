"""
NAME:
    Biodiversity Portfolio Project
    
PURPOSE:
    Explore biodiversity in national parks
    
REFERENCE:
    Christina T. Magagnoli

CALLING SEQUENCE:
    python3 "biodiversity.py"

MODIFICATION HISTORY:
    Created on 2024-02-13
    Last modified on 2024-02-13
"""
import csv
import pandas as pd
import numpy as np
#Import everything that might be needed for this project
#*******************************************************************************
obs = pd.read_csv('observations.csv')
spec = pd.read_csv('species_info.csv')
#read in our CSVs to pandas DataFrames

print('OBSERVATIONS:')
#print(obs.head())
print(obs.info())
print('SPECIES:')
#print(spec.head())
print(spec.info())
#start of EDA. Observations has no obvious NaNs, but species has conservation 
#data for only 3% of rows.


