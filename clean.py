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

# find number of dupes

# compare

# drop


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