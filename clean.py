# this cleans Oracle DB data

#%%
import os
import matplotlib
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from config import db_password

#%%
# de-duplicate; primary key is DPN
# load data files
arev_load = "data\parts_arev_na.txt"
xrev_load = "data\parts_xrev_na.txt"

#%%
# load x/a-rev into dataframe
df_a = pd.read_csv(arev_load, sep=';')
df_x = pd.read_csv(xrev_load, sep=";")

#%%
# display data in DF
# df_a
df_x

#%%
# find number of dupes
# df_x.duplicated(subset=['ITEM_NUMBER'])
# df_a.duplicated(subset=['ITEM_NUMBER'])

dup_xrevDF = df_x[df_x.duplicated(['ITEM_NUMBER'])]
print(dup_xrevDF)


#%%
# drop
dedup_xRev = df_x[df_x.duplicated(subset=['ITEM_NUMBER'], keep='first')]
# len(dedup_xRev)
dedup_xRev

# write to csv

# future, build function to locate data sources
#%%
# find nulls; should be none in DPN, PC, PT, CPC, CPT & GCS

# drop nulls


# use this later for findind N/A in attribute fields
    ## get list of values in each column

#%%
# next???

#%%


#%%
# Load into SQL DB
db_string = f"postgres://postgres:{db_password}@127.0.0.1:51734/<-PATH->"
engine = create_engine(db_string)
parts_df.to_sql(name='part', con=engine)