#Tyler Eck 
#410821337 
#6/8/2023
#Machine Learning Final Project

# Note: 
# I have to individually scrape each page separately because if I try to have to use a for loop to loop 
# through each page number and scrape, the website eventually blocks my requests. It is not illegal to
# scrape it, but I believe it was not meant for scraping purposes. 
 
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium import webdriver
import time


driverPath = 'chromedriver.exe'

# Pages from the leaderboard that I will scrape for each rank (SSL has the most valid data so we scrape less pages than Champion)
#SSL - 1-18 (1,4,6,9,13,15,18)
#GC - 25-127 (25,38,51,64,76,89,101,114,127)
#C - 152-900 (152, 199,246,293, 339, 387, 434, 481, 526, 575, 620,667, 713, 808,900)

data = []
rocket_league_url = "https://rocketleague.tracker.network/rocket-league/leaderboards/playlist/all/default?page=152&playlist=10"

response = requests.get(rocket_league_url)
soup = BeautifulSoup(response.content, 'html.parser')

leaderboard_table = soup.find('table', class_='trn-table')

rows = leaderboard_table.find_all('tr')

#first title rows
rows = rows[1:]

c = 0

for row in rows:
    error_count = 0
    error_count1 = 0
    d = []
    columns = row.find_all('td')


    link_search = BeautifulSoup(str(columns[1]), 'html.parser')
    links = link_search.find('a')

    #after getting the link we visit their profile to get the stats 
    user_profile_link = str("https://rocketleague.tracker.network" +links['href'] + "/mmr?playlist=10")

    options = Options()
    options.add_argument("--start-maximized")
    #opens browser to apple website
    browser = webdriver.Chrome(executable_path = driverPath, options = options)
    browser.get(user_profile_link)
  

    # Wait for the page to load (adjust the sleep duration if needed)
    time.sleep(4)

    goals_per_game = 0
    shots_per_game = 0
    saves_per_game = 0
    total_matches = 0
    shot_accuracy = 0
    goals_to_save = 0
    
    total_goals = 0
    total_wins = 0
    total_assists = 0 
    total_MVP = 0 
    total_saves = 0
    title_check = ""

    flag1 = 0
    try: 
        #Not all profiles have 1v1 information, so we check to see if the information is there 
        title_check = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/div/div/div[3]/div/table/tbody/tr/td[1]/div/div/div[1]')
        title_check = title_check.text
    except NoSuchElementException or AttributeError: 
        error_count1+=1
        if error_count1 == 7: 
            break
        time.sleep(2)

    #if there is no Ranked Duel 1v1 data that is available, we fill in with dummy values (1's) and move on
    if(title_check != 'Ranked Duel 1v1'): 
        goals_per_game = 1
        shots_per_game = 1
        saves_per_game = 1
        total_matches = 1
        shot_accuracy = 1
        goals_to_save = 1
        total_goals = 1
        total_wins = 1
        total_assists = 1
        total_MVP = 1 
        total_saves = 1
        d.append(goals_per_game)
        d.append(shots_per_game)
        d.append(saves_per_game)
        d.append(total_matches)
        d.append(shot_accuracy)
        d.append(goals_to_save)
        d.append(total_goals)
        d.append(total_wins)
        d.append(total_assists)
        d.append(total_MVP)
        d.append(total_saves)

        d.append(user_profile_link)
        data.append(d)
        # Close the browser
        browser.quit()
        flag1 = 1
        
    else:
        flag = 0
        #If there is data for the Ranked Duel 1v1 data, we try to scrape data. If not available then we fill with dummy values 0
        while not flag: 
            try:
                goals_per_game = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/div/div/div[3]/div/table/tbody/tr[1]/td[2]')
                shots_per_game = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/div/div/div[3]/div/table/tbody/tr[1]/td[3]')
                saves_per_game = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/div/div/div[3]/div/table/tbody/tr[1]/td[5]')
                total_matches = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/div/div/div[3]/div/table/tbody/tr[1]/td[7]')
                shot_accuracy = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/div/div/div[4]/div/table/tbody/tr[1]/td[2]')
                goals_to_save = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/div/div/div[4]/div/table/tbody/tr[1]/td[3]')
                total_goals = browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/aside/div[3]/div/div[3]/div/div[2]/span[2]')

                total_wins = browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/aside/div[3]/div/div[1]/div/div[2]/span[2]')
                total_assists = browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/aside/div[3]/div/div[5]/div/div[2]/span[2]')
                total_MVP = browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/aside/div[3]/div/div[7]/div/div[2]/span[2]')
                total_saves = browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/main/div[3]/div[3]/div[1]/aside/div[3]/div/div[6]/div/div[2]/span[2]')
                flag = 1
            except NoSuchElementException: 
                error_count+=1
                goals_per_game = 0
                shots_per_game = 0
                saves_per_game = 0
                total_matches = 0
                shot_accuracy = 0
                goals_to_save = 0
                total_goals = 0
                total_wins = 0
                total_assists = 0
                total_MVP = 0
                total_saves = 0
                if(error_count == 7): 
                    break
                time.sleep(2)


        if(error_count == 7): 
            d.append(goals_per_game)
            d.append(shots_per_game)
            d.append(saves_per_game)
            d.append(total_matches)
            d.append(shot_accuracy)
            d.append(goals_to_save)
            d.append(total_goals)
            d.append(total_wins)
            d.append(total_assists)
            d.append(total_MVP)
            d.append(total_saves)

        else:
            d.append(goals_per_game.text)
            d.append(shots_per_game.text)
            d.append(saves_per_game.text)
            d.append(int(str(total_matches.text).replace(',','')))
            d.append(shot_accuracy.text)
            d.append(goals_to_save.text)
            d.append(int(str(total_goals.text).replace(',','')))
            d.append(int(str(total_wins.text).replace(',','')))
            d.append(int(str(total_assists.text).replace(',','')))
            d.append(int(str(total_MVP.text).replace(',','')))
            d.append(int(str(total_saves.text).replace(',','')))

        d.append(user_profile_link)
        data.append(d)
        # Close the browser
        browser.quit()
        c+=1
        print(c)

data = pd.DataFrame(data)

#Naming Convention for files are "RL_<SSL,GC,C>_#.csv". The # depends on how many pages will be scraped.
data.to_csv('RL_C_1.csv',index = False)
print(data)