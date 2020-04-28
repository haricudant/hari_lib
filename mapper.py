import sys,os,math
import statistics
from statistics import *
from collections import defaultdict
import pandas as pd

# Creating the dataframe
df = pd.read_csv("Mortality_05_UT_COLUMN_DEL_altered.csv")
from math import *
data_dict = defaultdict(list)
gk = df.groupby('Year')
print(gk)
for line in sys.stdin:
    try:
        line = line.rstrip(os.linesep)
        year_of_death,rural_urban = line.split(",")
        #year_of_death = int(year_of_death)

        #rural_urban = int(rural_urban)
        data_dict[rural_urban].append(year_of_death)
    except Exception:
        pass

for k,v in data_dict.items():
    print("%s,%s" %(k,len(v)))