#Tyler Eck 
#410821337 
#6/8/2023
#Machine Learning Final Project

import pandas as pd 
import numpy as np


# Combining SSL Clean Data 

df1 = pd.read_csv("../Clean Data/RL_SSL_1_clean.csv")
df2 = pd.read_csv("../Clean Data/RL_SSL_2_clean.csv")
df3 = pd.read_csv("../Clean Data/RL_SSL_3_clean.csv")
df4 = pd.read_csv("../Clean Data/RL_SSL_4_clean.csv")
df5 = pd.read_csv("../Clean Data/RL_SSL_5_clean.csv")
df6 = pd.read_csv("../Clean Data/RL_SSL_6_clean.csv")
df7 = pd.read_csv("../Clean Data/RL_SSL_7_clean.csv")

frames = [df1,df2,df3,df4,df5,df6,df7]
result = pd.concat(frames)
result.to_csv("RL_SSL.csv",index = False)

############################################################################################
# Combining Grand Champion Clean Data 

df1 = pd.read_csv("../Clean Data/RL_GC_1_clean.csv")
df2 = pd.read_csv("../Clean Data/RL_GC_2_clean.csv")
df3 = pd.read_csv("../Clean Data/RL_GC_3_clean.csv")
df4 = pd.read_csv("../Clean Data/RL_GC_4_clean.csv")
df5 = pd.read_csv("../Clean Data/RL_GC_5_clean.csv")
df6 = pd.read_csv("../Clean Data/RL_GC_6_clean.csv")
df7 = pd.read_csv("../Clean Data/RL_GC_7_clean.csv")
df8 = pd.read_csv("../Clean Data/RL_GC_8_clean.csv")
df9 = pd.read_csv("../Clean Data/RL_GC_9_clean.csv")

frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9]
result = pd.concat(frames)
result.to_csv("RL_GC.csv",index = False)


############################################################################################

#Combining Champion Clean Data 

df1 = pd.read_csv("../Clean Data/RL_C_1_clean.csv")
df2 = pd.read_csv("../Clean Data/RL_C_2_clean.csv")
df3 = pd.read_csv("../Clean Data/RL_C_3_clean.csv")
df4 = pd.read_csv("../Clean Data/RL_C_4_clean.csv")
df5 = pd.read_csv("../Clean Data/RL_C_5_clean.csv")
df6 = pd.read_csv("../Clean Data/RL_C_6_clean.csv")
df7 = pd.read_csv("../Clean Data/RL_C_7_clean.csv")
df8 = pd.read_csv("../Clean Data/RL_C_8_clean.csv")
df9 = pd.read_csv("../Clean Data/RL_C_9_clean.csv")
df10 = pd.read_csv("../Clean Data/RL_C_10_clean.csv")
df11 = pd.read_csv("../Clean Data/RL_C_11_clean.csv")
df12 = pd.read_csv("../Clean Data/RL_C_12_clean.csv")
df13 = pd.read_csv("../Clean Data/RL_C_13_clean.csv")
df14 = pd.read_csv("../Clean Data/RL_C_14_clean.csv")
df15 = pd.read_csv("../Clean Data/RL_C_15_clean.csv")

frames = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15]
result = pd.concat(frames)
result.to_csv("RL_C.csv",index = False)


#Combing ALL CLEAN data and taking only 350 records from each
df1 = pd.read_csv("RL_C.csv")
df2 = pd.read_csv("RL_GC.csv")
df3 = pd.read_csv("RL_SSL.csv")
df1 = df1.head(350)
df2 = df2.head(350)
df3 = df3.head(350)

#Concat all and shuffle
frames = [df3,df2,df1]
result = pd.concat(frames)
result = result.sample(frac = 1)

#Correlation Matrix 
m = result.corr()
print(m["Actual_Rank"])


result.to_csv("combined.csv",index = False)