# Rocket League Rank Classifier
![ranks](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/assets/68008817/190c16d9-9e2f-43f9-90c4-1fcef820d201)

Author: Tyler Edwardo Eck  
Class: Machine Learning    
Professor: 顏士淨 (Shi-Jim Yen)   

## Introduction 
Rocket League Rank Classifier is my final project for the 2023 Machine Learning class. The objective for this project is to determine what factors influence a player's rank in the vehicular soccer game Rocket League. The three machine learning algorithms, Logistic Regression, Random Forest, and SVC, were trained and tested with data that was collected from the [Rocket League Tracker](https://rocketleague.tracker.network/) website. The scraping, preprocessing, and training of ML models were all done manually and results are presented in my [final presentation](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/blob/master/410821337_Rocket%20League%20Rank%20Classifier.pptx)

## Method
1. Data Collection - scrape 1v1 Duel data using a Python script
2. Pre-processing - "cleaning" or fixing the mistakes in the data
3. Training of the ML models - Logistic Regression, Random Forest, and SVC
4. Testing - comparing accuracies after multiple changes in configurations
     
## Data Collection 
A Rocket League player's stastics are publicly tracked and displayed on the [Rocket League Tracker](https://rocketleague.tracker.network/) website. By using the scrape.py python script, these 11 features were collected to train the ML models:

1. Goals/Game – goals per game
2. Shots/Game – shots per game
3. Saves/Game – saves per game
4. Total # Of Matches – total # of 1v1 matches played
5. Shot Accuracy – percentage of shots on goal
6. Goals/Saves- goals to saves Ratio 
7. Total Goals – lifetime goals 
8. Total Wins – lifetime wins 
9. Total Assists – lifetime assists 
10. Total MVP – lifetime MVP
11. Total Saves – lifetime saves 

![rank 2](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/assets/68008817/d67c3de3-04c9-4b93-b236-244471cac638)

