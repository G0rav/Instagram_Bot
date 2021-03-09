'''
Download chromedriver or any browser driver as per your browser version.
Put it in a disk and assign path variable to the path of the driver.

https://sites.google.com/a/chromium.org/chromedriver/downloads

'''
#pip install selenium            #to install selenium

#Importing necessary libraries

import time
from super_secret import *
from selenium import webdriver      #importing webdrivers to use browsers for automation
from selenium.webdriver.common.keys import Keys    # importing Keys (not keys) for various mouse and keyboard fumctions

driverpath = "C:\chromedriver\chromedriver.exe"   #assigning path for chromeweb driver exe file
driver = webdriver.Chrome(driverpath)       #making chrome webdriver object for use

driver.maximize_window()
maximum_size = driver.get_window_size()
maximum_size

driver.set_window_size(maximum_size['width']/2,
                       maximum_size['height'])
driver.set_window_position(maximum_size['width']/2,0)


#Open Instagram & Enter Login details

driver.get('https://www.instagram.com/')     # .get function for accessing any website

time.sleep(3)
username = driver.find_element_by_name('username')
username.clear()
username.send_keys(Username)        #to enter any text in box
password = driver.find_element_by_name('password')
password.clear()
password.send_keys(Password)
log_in = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
log_in.click()      #to click on button


#Function to extract users
def scrap_users(url):
    """
    Input url of webpage
    Output: users list
    """
    
    driver.get(url)
    print('I am currently on',driver.title)

    while True:
        try:
            view_more_button = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/main/button')
            view_more_button.click()
            time.sleep(4)
        except:
            break

    users = []
    users_class = driver.find_elements_by_class_name("-utLf")
    for user_element in users_class:
        users.append(user_element.text)

    return users


#Function to unfollow or unrequest users
def unfollow(users, start, end):
     """
    Input: users list, start and end index
    """
    
    for i,user in enumerate(users[start:end], start=1):
        time.sleep(2)
        print('user:',user)
        
        try:
            #Enter username
            search_bar_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]'
            driver.find_element_by_xpath(search_bar_xpath).click()
            search_box_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
            search_box = driver.find_element_by_xpath(search_box_xpath)
            search_box.clear()
            search_box.send_keys(user)
            time.sleep(2)                   

            #find username
            username_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]'    
            driver.find_element_by_xpath(username_xpath).click()
            time.sleep(2)   

            try:
                #following-unfollow
                time.sleep(1)
                following_button_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div[2]/div/span/span[1]/button'      
                driver.find_element_by_xpath(following_button_xpath).click()

            except:
                pass

            try:                
                #unrequest
                #just to make request vsisible
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/div/button/img').click() 
                time.sleep(1)
                request_xpath = '//*[@id="react-root"]/section/main/div/header/div/div/div/button/img'      
                driver.find_element_by_xpath(request_xpath).click()
                time.sleep(1)
                request_button_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/button'
                driver.find_element_by_xpath(request_button_xpath).click()
                time.sleep(2)

            except:
                pass

            #unfollow
            time.sleep(1)
            xpath = '/html/body/div[5]/div/div/div/div[3]/button[1]'
            unfollow_button = driver.find_element_by_xpath(xpath)
            time.sleep(1)
            unfollow_button.click()
            time.sleep(2)

            print(f'{i} success')

        except:
            pending.append(user)
            print(f'{i} fail')
            pass
        print(f'{int(i*100/len(users[start:end]))}% completed')
        print()


#------------- for requested users---------------------#
requested_users = scrap_users('https://www.instagram.com/accounts/access_tool/current_follow_requests')

for user in requested_use:
    f = open('requested_users.txt','a')
    f.write(f'{user},')
    f.close()


f = open('reuested_users.txt','r')
requested_users = f.readline().split(',')
f.close()


pending = []
start = 30
end = 40
unfollow(requested_users,start,end)

#------------- end block---------------------#



#------------- for following users---------------------#
following_users = scrap_users('https://www.instagram.com/accounts/access_tool/accounts_you_follow')
len(following_users)

for user in following_use:
    f = open('following_users.txt','a')
    f.write(f'{user},')
    f.close()


f = open('following_users.txt','r')
following_users = f.readline().split(',')
f.close()


pending = []
start = 540
end = 570
unfollow(following_users,start,end)

#------------- end block---------------------#

