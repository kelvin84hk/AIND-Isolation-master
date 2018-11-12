# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:56:24 2018

@author: Kelvin
"""

import pandas as pd
import seaborn as sns
import numpy as np

x=['AB_Improved','AB_Custom','AB_Custom_2','AB_Custom_3','AB_Custom_4','AB_Custom_5']
y=[57.5,62.5,59.2,55.0,62.5,61.7]
z=[61.7,61.7,55.8,55.0,47.5,59.9]

data =pd.DataFrame(np.transpose([x,y,z]),columns=['heuristic function','player','opponent'])
data= pd.melt(data, id_vars="heuristic function", var_name="playing position", value_name="win rate")
data['win rate']=data['win rate'].convert_objects(convert_numeric=True)
sns.factorplot(x='heuristic function', y='win rate', hue='playing position', data=data, kind='bar',size=10)
