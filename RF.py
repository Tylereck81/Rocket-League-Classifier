#Tyler Eck 
#410821337 
#6/8/2023
#Machine Learning Final Project

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# DEFAULT: DSDF: Default Settings Default Features 
df = pd.read_csv("Combined Data/combined.csv")
X = df.drop("Actual_Rank", axis = 1)
X = X.values
Y = df["Actual_Rank"]
Y = Y.values 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1234) 
randomForest = RandomForestClassifier()
randomForest.fit(X_train, Y_train)
accuracy = randomForest.score(X_test, Y_test)
print(accuracy)


# ###############################################################################################
# # DSSF: Default Settings Specific Features 

# df = pd.read_csv("Combined Data/combined.csv")
# X = df.drop("Actual_Rank", axis = 1)

# X = X.drop("Goals Per Game",axis=1)
# X = X.drop("Shots Per Game",axis=1)
# X = X.drop("Saves Per Game",axis=1)
# # X = X.drop("Total Matches",axis=1)
# X = X.drop("Shot Accuracy",axis=1)
# X = X.drop("Goals/Saves",axis=1)
# # X = X.drop("Total Goals",axis=1)
# # X = X.drop("Total Wins",axis=1)
# # X = X.drop("Total Assists",axis=1)
# # X = X.drop("Total MVP",axis=1)
# # X = X.drop("Total Saves",axis=1)

# X = X.values
# Y = df["Actual_Rank"]
# Y = Y.values 

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1234) 
# randomForest = RandomForestClassifier()
# randomForest.fit(X_train, Y_train)
# accuracy = randomForest.score(X_test, Y_test)
# print(accuracy)


###############################################################################################
# SSDF: Specific Settings Default Features 

# df = pd.read_csv("Combined Data/combined.csv")
# X = df.drop("Actual_Rank", axis = 1)

# X = X.values
# Y = df["Actual_Rank"]
# Y = Y.values 

# highest_acc = 0
# highest_c = 0
# acc = []
# c = []
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1234)
# for i in range(1,200): 
#     randomForest = RandomForestClassifier(n_estimators=i)
#     randomForest.fit(X_train, Y_train)
#     accuracy = randomForest.score(X_test, Y_test)
#     acc.append(accuracy) 
#     c.append(i)
#     if(accuracy>highest_acc): 
#         highest_acc = accuracy
#         highest_c = i

# print(highest_acc)
# print(highest_c)

# plt.plot(c,acc) 
# plt.show()


###############################################################################################
# SSSF: Specific Settings Specific Features 
# df = pd.read_csv("Combined Data/combined.csv")
# X = df.drop("Actual_Rank", axis = 1)

# X = X.drop("Goals Per Game",axis=1)
# X = X.drop("Shots Per Game",axis=1)
# X = X.drop("Saves Per Game",axis=1)
# # X = X.drop("Total Matches",axis=1)
# X = X.drop("Shot Accuracy",axis=1)
# X = X.drop("Goals/Saves",axis=1)
# # X = X.drop("Total Goals",axis=1)
# # X = X.drop("Total Wins",axis=1)
# # X = X.drop("Total Assists",axis=1)
# # X = X.drop("Total MVP",axis=1)
# # X = X.drop("Total Saves",axis=1)

# X = X.values
# Y = df["Actual_Rank"]
# Y = Y.values 

# highest_acc = 0
# highest_c = 0
# acc = []
# c = []
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1234)
# for i in range(1,200): 
#     randomForest = RandomForestClassifier(n_estimators=i)
#     randomForest.fit(X_train, Y_train)
#     accuracy = randomForest.score(X_test, Y_test)
#     acc.append(accuracy) 
#     c.append(i)
#     if(accuracy>highest_acc): 
#         highest_acc = accuracy
#         highest_c = i

# print(highest_acc)
# print(highest_c)

# plt.plot(c,acc) 
# plt.show()
