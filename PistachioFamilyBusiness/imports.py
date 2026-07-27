

#%% 
import numpy as  np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set_style('dark')
palette = sns.color_palette('Set2')

import os
from zipfile import ZipFile as zf
from datetime import datetime
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings('ignore')

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import xgboost
from xgboost import XGBRegressor

path = "D:\\Machine learning\\MLprojects\\bussiness.csv" 
# path = "D:\Machine learning\MLprojects\PistachioBusiness.zip"


#%%



