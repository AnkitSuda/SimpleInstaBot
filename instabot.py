from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import logging
import sys

# Change this to your own chromedriver path!
chromedriver_path = 'C:/Users/Suda/Downloads/Compressed/chromedriver_win32_2/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
# Change with your username
username.send_keys('USER_NAME')
password = webdriver.find_element_by_name('password')
# Change with your password
password.send_keys('PASS_WORD')
try:
    button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
except:
    button_login = webdriver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(5)
try:
    savebt = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    savebt.click()
except:
    pass

try:
    notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click()
except:
	pass

# Change with hashtags you want to use
hashtag_list = ['lightroom', 'mobilephotography', 'like4like']

prev_user_list = []

d_users = []
tag = -1
likes = 0

for hashtag in hashtag_list:
    tag += 1
    # Opens hashtag
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    # It clicks on first photo to open photo window
    first_thumbnail = webdriver.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div')
    first_thumbnail.click()
    sleep(randint(1,2))    
    
    try:        
        for x in range(1,200):
            # Copies username of user
            username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/div/a').text
            print(username)
            d_users.append(username)

            # Clicks on like button
            button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            button_like.click()

            # Increaments likes array
            likes += 1
            sleep(5)
          
            # Next picture
            webdriver.find_element_by_link_text('Next').click()
            sleep(randint(25,29))
    except:
        # If error occurres, skip to next hashtag
        print("Oops!", sys.exc_info()[0], "occurred.")
        continue

for n in range(0,len(d_users)):
    prev_user_list.append(d_users[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))