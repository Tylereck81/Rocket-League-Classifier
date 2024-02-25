#Tyler Eck 
#410821337 
#6/8/2023
#Machine Learning Final Project
import pandas as pd 

# Cleaning SSL Data (7 files)
 
for i in range(1,8):
    file_name = "RL_SSL_"+str(i)+".csv"

    #Reading the csv files
    df = pd.read_csv("../Scraped Data/"+file_name)

    #Renaming the column titles
    df = df.rename(columns={'0': 'Goals Per Game', '1': 'Shots Per Game', '2': 'Saves Per Game', '3': 'Total Matches', '4': 'Shot Accuracy', '5': 'Goals/Saves', '6': 'Total Goals', '7': 'Total Wins', '8': 'Total Assists', '9': 'Total MVP', '10': 'Total Saves' , '11': 'Link'})
    df = df.drop("Link", axis=1)

    #Changing Shot Accuracy from percentage to float decimal
    df['Shot Accuracy'] = df['Shot Accuracy'].str.rstrip("%").astype(float)/100

    #Removing rows filled with 0's and 1's
    bad_rows = df[ (df['Goals Per Game'].astype(int) == 1) & (df['Shots Per Game'].astype(int) == 1) & (df['Saves Per Game'].astype(int) == 1) & (df['Goals/Saves'].astype(int) == 1)].index
    df.drop(bad_rows, inplace = True)
    bad_rows = df[ (df['Goals Per Game'].astype(int) == 0) & (df['Shots Per Game'].astype(int) == 0) & (df['Saves Per Game'].astype(int) == 0) & (df['Goals/Saves'].astype(int) == 0)].index
    df.drop(bad_rows, inplace = True)

    #Adding the actual rank column
    df['Actual_Rank'] = 3

    #Saving the cleaned data
    df.to_csv("RL_SSL_"+str(i)+"_clean.csv", index=False)


##########################################################################################################
# Cleaning Grand Champion Data (9 files)
 
for i in range(1,10):
    file_name = "RL_GC_"+str(i)+".csv"

    #Reading the csv files
    df = pd.read_csv("../Scraped Data/"+file_name)

    #Renaming the column titles
    df = df.rename(columns={'0': 'Goals Per Game', '1': 'Shots Per Game', '2': 'Saves Per Game', '3': 'Total Matches', '4': 'Shot Accuracy', '5': 'Goals/Saves', '6': 'Total Goals', '7': 'Total Wins', '8': 'Total Assists', '9': 'Total MVP', '10': 'Total Saves' , '11': 'Link'})
    df = df.drop("Link", axis=1)

    #Changing Shot Accuracy from percentage to float decimal
    df['Shot Accuracy'] = df['Shot Accuracy'].str.rstrip("%").astype(float)/100

    #Removing rows filled with 0's and 1's
    bad_rows = df[ (df['Goals Per Game'].astype(int) == 1) & (df['Shots Per Game'].astype(int) == 1) & (df['Saves Per Game'].astype(int) == 1) & (df['Goals/Saves'].astype(int) == 1)].index
    df.drop(bad_rows, inplace = True)
    bad_rows = df[ (df['Goals Per Game'].astype(int) == 0) & (df['Shots Per Game'].astype(int) == 0) & (df['Saves Per Game'].astype(int) == 0) & (df['Goals/Saves'].astype(int) == 0)].index
    df.drop(bad_rows, inplace = True)

    #Adding the actual rank column
    df['Actual_Rank'] = 2

    #Saving the cleaned data
    df.to_csv("RL_GC_"+str(i)+"_clean.csv", index=False)


##########################################################################################################
# Cleaning Champion Data (15 files)
 
for i in range(1,16):
    file_name = "RL_C_"+str(i)+".csv"

    #Reading the csv files
    df = pd.read_csv("../Scraped Data/"+file_name)

    #Renaming the column titles
    df = df.rename(columns={'0': 'Goals Per Game', '1': 'Shots Per Game', '2': 'Saves Per Game', '3': 'Total Matches', '4': 'Shot Accuracy', '5': 'Goals/Saves', '6': 'Total Goals', '7': 'Total Wins', '8': 'Total Assists', '9': 'Total MVP', '10': 'Total Saves' , '11': 'Link'})
    df = df.drop("Link", axis=1)

    #Changing Shot Accuracy from percentage to float decimal
    df['Shot Accuracy'] = df['Shot Accuracy'].str.rstrip("%").astype(float)/100

    #Removing rows filled with 0's and 1's
    bad_rows = df[ (df['Goals Per Game'].astype(int) == 1) & (df['Shots Per Game'].astype(int) == 1) & (df['Saves Per Game'].astype(int) == 1) & (df['Goals/Saves'].astype(int) == 1)].index
    df.drop(bad_rows, inplace = True)
    bad_rows = df[ (df['Goals Per Game'].astype(int) == 0) & (df['Shots Per Game'].astype(int) == 0) & (df['Saves Per Game'].astype(int) == 0) & (df['Goals/Saves'].astype(int) == 0)].index
    df.drop(bad_rows, inplace = True)

    #Adding the actual rank column
    df['Actual_Rank'] = 1

    #Saving the cleaned data
    df.to_csv("RL_C_"+str(i)+"_clean.csv", index=False)
