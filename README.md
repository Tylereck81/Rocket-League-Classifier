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
A Rocket League player's stastics are publicly tracked and displayed on the [Rocket League Tracker](https://rocketleague.tracker.network/) website. By using the [scrape.py](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/blob/master/Scraped%20Data/scrape.py) python script, these 11 features were collected to train the ML models:

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

## Preprocessing 
The collected data was then cleaned to remove all records that had missing data. By using the [clean.py](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/blob/master/Clean%20Data/clean.py) python script, all the records that had rows filled with 0's or 1's (which indicates that the data was missing from the website) was completed removed. 

### Before Cleaning
![nonclean](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/assets/68008817/c2347cd4-3593-408f-b72f-f1fe861f16f0)

### After Cleaning 
![clean](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/assets/68008817/143e513f-94cd-4d29-97ae-bc2bffeff3d4)
    
Lastly, all of the clean data from each of the three Rocket League ranks (SuperSonic Legend, Grand Champion, and Champion) was combined into the single csv file [combined.csv](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/blob/master/Combined%20Data/combined.csv) using the [combine.py](https://github.com/Tylereck81/Rocket-League-Rank-Classifier/blob/master/Combined%20Data/combine.py) python script. 

## Setup 
This project already has the cleaned and combined data that is used to train the ML models, so in order to run the programs locally, follow the necessary steps below:    

1.  Download and install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) - Python 3.5 or 3.6
     
2.   Create and activate an environment, and download the necessary packages below using "conda install".
      
   * Pandas
   * Numpy
   * Selenium
   * BeautifulSoup

3. For Logistic Regression, run "python LR.py" in the environment.
4. For Random Forest, run "python RF.py" in the environment.
5. For Support Vector Classifier, run "python SVC.py" in the environment.



