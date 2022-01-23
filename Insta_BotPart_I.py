#!/usr/bin/env python
# coding: utf-8

# # InstaBot - Part 1

# In[1]:


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time


# In[29]:


#opening the browser, change the path as per location of chromedriver in your system
driver = webdriver.Chrome(executable_path = 'C:/Users/admin/Downloads/Chromedriver/chromedriver.exe')
driver.maximize_window()


# In[30]:


#opening instagram
driver.get('https://www.instagram.com/')


# In[32]:


#update your username and password here
username = 'SAMPLE USERNAME'
password = 'SAMPLE PASSWORD'


# In[33]:


#initializing  wait object
wait = WebDriverWait(driver, 10)


# ### Problem 1 : Login to your Instagram
# Login to your Instagram Handle  
# Submit with sample username and password

# In[34]:


def LogIn(username, password):
    try :
        #locating username textbox and sending username
        user_name = wait.until(EC.presence_of_element_located((By.NAME,'username')))
        user_name.send_keys(username)
        #locating password box and sending password
        pwd = driver.find_element_by_name('password')
        pwd.send_keys(password)
        #locating login button 
        button = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button/div')))
        button.submit()
        #Save Your Login Info? : Not Now
        pop = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
        pop.click()
        
    except TimeoutException :
        print ("Something went wrong! Try Again")


# In[35]:


#Login to your Instagram Handle
LogIn(username, password)


# ### Problem 2 : Type for “food” in search bar
# Type for “food” in search bar and print all the names of the Instagram Handles that are displayed in list after typing “food”  
# Note : Make sure to avoid printing hashtags  

# In[8]:


def search(s):
    try:
        #locating serch bar and sending text
        search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'XTCLo')))
        search_box.send_keys(s)
        #waiting till all searched is located
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))
        #extracting all serched handle
        handle_names = driver.find_elements_by_class_name('yCE8d')
        names = []
        #extracting username
        for i in handle_names :
            if i.text[0] != '#' :
                names.append(i.text.split('\n')[0])             

        time.sleep(5)
        #clearing search bar
        driver.find_element_by_class_name('coreSpriteSearchClear').click()
 
        return names
    
    except TimeoutException :
        print('No Search Found!')
    


# In[9]:


#extracting all the names of the Instagram Handles that are displayed in list after typing “food” usimg search('food')
name_list = search('food')
for i in name_list :
    print(i)


# ### Problem 3 : Searching and Opening a profile
# Searching and Opening a profile using   
# Open profile of “So Delhi” 

# In[36]:


def search_open_profile(s):
    try:
        #locatong search box bar and sending text 
        search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'XTCLo')))
        search_box.send_keys(s)
        #locating serched result
        res = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'yCE8d')))
        res.click()           

        time.sleep(5)
        #driver.back()
    
    except TimeoutException :
        print('No Search Found!')
    


# In[11]:


search_open_profile('So Delhi')


# ### Problem 4 : Follow/Unfollow given handle
# Follow/Unfollow given handle -   
# 1.Open the Instagram Handle of “So Delhi”  
# 2.Start following it. Print a message if you are already following  
# 3.After following, unfollow the instagram handle. Print a message if you have already unfollowed.

# In[12]:


def follow():
    try :
        #locating follow button
        btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'_5f5mN')))
        #checking for text
        if btn.text == 'Follow' : 
            btn.click()
            time.sleep(3)
        
        else : 
            print('Already Following')

    except TimeoutException :
        print("Something Went Wrong!")
 


# In[13]:


def unfollow():
    try :
        #locating follow button
        btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'_5f5mN')))
        #checking for text
        if btn.text !='Follow' : 
            btn.click()
            time.sleep(2)
            #locating popup window (when you click on follow button)
            pop_up = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'aOOlW')))
            pop_up.click()
            time.sleep(3)
            
        else : 
            print('Already Unfollowed')

    except TimeoutException :
        print("Something Went Wrong!")


# In[14]:


#for search and open 'dilsefoodie' instagram handle
search_open_profile('So Delhi')
#for following this instgram handle
follow()
#for unfollowing this instgram handle
unfollow()


# ### Problem 5 : Like/Unlike posts
# Like/Unlike posts  
# 1.Liking the top 30 posts of the ‘dilsefoodie'. Print message if you have already liked it.  
# 2.Unliking the top 30 posts of the ‘dilsefoodie’. Print message if you have already unliked it.

# In[121]:


def Like_Post():
    try :
        #scrolling for locating post
        driver.execute_script('window.scrollTo(0, 6000);')
        time.sleep(3)
        driver.execute_script('window.scrollTo(0, -6000);')
        time.sleep(3)
        #locating post
        posts = driver.find_elements_by_class_name('v1Nh3')
        
        for i in range(30):
            posts[i].click()
            time.sleep(2)
            #locating like/unke button
            like = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'fr66n')))
            st = BeautifulSoup(like.get_attribute('innerHTML'),"html.parser").svg['aria-label']
        
            if st == 'Like' :
                like.click()
                time.sleep(2)
            else :
                print('You have already LIKED Post Number :', i+1)
                time.sleep(2)
            #locating cross button for closing post
            driver.find_element_by_class_name('yiMZG').click()
            time.sleep(2)
            
    except TimeoutException :
        print("Something Went Wrong!")


# In[124]:


def Unlike_Post():
    try :
        #scrolling for locating post
        driver.execute_script('window.scrollTo(0, 6000);')
        time.sleep(3)
        driver.execute_script('window.scrollTo(0, -6000);')
        time.sleep(3)
        #locating post
        posts = driver.find_elements_by_class_name('v1Nh3')
     
        for i in range(30):
            posts[i].click()
            time.sleep(2)
            #locating like/unke button
            like = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'fr66n')))
            st = BeautifulSoup(like.get_attribute('innerHTML'),"html.parser").svg['aria-label']
        
            if st == 'Unlike' :
                like.click()
                time.sleep(2)
            else :
                print('You have already UNLIKED Post Number', i+1)
                time.sleep(2)
            #locating cross button for closing post
            driver.find_element_by_class_name('yiMZG').click()
            time.sleep(2)
            
    except TimeoutException :
        print("Something Went Wrong!")


# In[119]:


#for search and open 'dilsefoodie' instagram handle
search_open_profile('dilsefoodie')


# In[123]:


#Liking the top 30 posts 
Like_Post()


# In[125]:


#Unliking the top 30 posts 
Unlike_Post()


# ### Problem 6 : Extract list of followers
# Extract list of followers  
# 1.Extract the usernames of the first 500 followers of ‘foodtalkindia’ and ‘sodelhi’.  
# 2.Now print all the followers of “foodtalkindia” that you are following but those who don’t follow you.

# In[51]:


def Extract_Followers():
    try :
        # locating followers button and click on it
        followers_btn = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'g47SY')))
        followers_btn[1].click()
        
        #locating followers list
        frame = driver.find_element_by_class_name('isgrP')
        #scrolling untill first 500 user is located
        for i in range(50):
            time.sleep(1)
            driver.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight",frame)
        
        names = []
        #extracting userdata
        followers = driver.find_elements_by_class_name('d7ByH')
        #extracting username
        for i in followers[:500] :
                names.append(i.text.split('\n')[0])
            
        return names
    except TimeoutException :
        print("Something Went Wrong!")


# ##### First 500 followers of ‘foodtalkindia’ 

# In[52]:


#for search and open 'foodtalkindia' instagram handle
search_open_profile('foodtalkindia')


# In[53]:


# Extracting followers using Extract_Followers() function
users = Extract_Followers()
ind = 1
for username in users:
    print(ind,username)
    ind += 1


# ##### First 500 followers of ‘sodelhi’ 

# In[54]:


#for search and open 'sodelhi' instagram handle
search_open_profile('sodelhi')


# In[57]:


# Extracting followers using Extract_Followers() function
users = Extract_Followers()
ind = 1
for username in users:
    print(ind,username)
    ind += 1


# #####  Print all the followers of “foodtalkindia” that you are following but those who don’t follow you.

# In[74]:


def Following():
    try :
        # locating following button and click on it
        followers_btn = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'-nal3')))
        followers_btn[2].click()
        
        #locating followers list
        frame = driver.find_element_by_class_name('isgrP')
        #scrolling untill all users are located
        for i in range(20):
            time.sleep(1)
            driver.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight",frame)
        
        names = []
        #extracting userdata
        following = driver.find_elements_by_class_name('d7ByH')
        #extracting username
        for i in following :
                names.append(i.text.split('\n')[0])
            
        return names
    except TimeoutException :
        print("Something Went Wrong!")


# In[79]:


#for search and open 'foodtalkindia' instagram handle
search_open_profile('foodtalkindia')
# Extracting followers using Extract_Followers() function
followers_of_foodind = Extract_Followers()
#casting into set
followers_of_foodind = set(followers_of_foodind)


# In[80]:


#now finding all user followed by me for that I'll use search_open_profile() after that using Following() I will extrat all user
#followed by me
search_open_profile(username)
followed_by_me = Following()
followed_by_me = set(followed_by_me)


# In[83]:


#taking intersection so s1 contains only that user who followed by me
s1=(followers_of_foodind).intersection(followed_by_me)
if len(s1) == 0:
    print('No such users found')
else:
    #now extracting my followers
    my_follower = Extract_Followers()
    my_follower = set(my_follower)
    #taking intersection with s1, so s2 contains only users that I am following them but they don’t follow me
    s2=s1.intersection(my_follower)
    if len(s2) == 0:
        print('No such users found')
    else:
        for user in s2:
            print(user)
    


# ### Problem 7 : Check the story of ‘coding.ninjas’
# Check the story of ‘coding.ninjas’. Consider the following Scenarios and print error messages accordingly -  
# 1.If You have already seen the story.  
# 2.Or The user has no story.  
# 3.Or View the story if not yet seen.  

# In[61]:


def Check_Story():
    try:
        #locating story or profile pic
        story = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"RR-M-.h5uC0")))
    
        #check the Profile photo size to find out story is available or not
        height = driver.find_element_by_class_name('CfWVH').get_attribute('height')
        if int(height) == 166:
            print("Already seen the story")
        else:
            print("Viewing the story")
            driver.execute_script("arguments[0].click();",story)
    except:
        print("No story is available to view")


# In[64]:


#searching 'coding.ninjas' using search_open_profile() function
search_open_profile('coding.ninjas')


# In[66]:


#for checking story
Check_Story()


# In[ ]:




