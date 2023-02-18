#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. scrape the job-title, job-location, company_name, experience_required. scrape first 10 
      jobs data.


# In[89]:


get_ipython().system('pip install selenium')


# In[90]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


# In[91]:


driver=webdriver.Chrome(r"C:\Users\msi 1\Downloads\chromedriver_win32\chromedriver.exe")
#connect to the driver


# In[92]:


#open the naukri page
driver.get("http://www.naukri.com/")


# In[93]:


#enter designation and location as per question
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')


# In[94]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[95]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[88]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[80]:


#scraping job title
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[81]:


#scraping job location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)


# In[82]:


#scraping company_name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[83]:


#scraping job exp
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[84]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[85]:


import pandas as pd


# In[86]:


df=pd.DataFrame({"title":job_title,"location":job_location,"company_name":company_name,"Experience":experience_required})
df


# In[ ]:


# 2. :Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data


# In[96]:


get_ipython().system('pip install selenium')


# In[97]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[98]:


driver=webdriver.Chrome(r"C:\Users\msi 1\Downloads\chromedriver_win32\chromedriver.exe")
#connect to the driver


# In[99]:


#open the naukri page
driver.get("http://www.naukri.com/")


# In[100]:


#enter designation and location as per question
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[101]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[102]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[103]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[104]:


#scraping job title
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[105]:


#scraping job location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)


# In[106]:


#scraping company_name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[107]:


#scraping job exp
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[108]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[109]:


import pandas as pd


# In[110]:


df=pd.DataFrame({"title":job_title,"location":job_location,"company_name":company_name,"Experience":experience_required})
df


# In[1]:


#3. 


# In[13]:


get_ipython().system('pip install selenium')


# In[14]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[15]:


driver=webdriver.Chrome(r"C:\Users\msi 1\Downloads\chromedriver_win32\chromedriver.exe")
#connect to the driver


# In[16]:


#open the naukri page
driver.get("http://www.naukri.com/")


# In[19]:


#enter designation and location as per question
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[20]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[23]:


#scraping job title
job_title=[]
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[25]:


#4. Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
#1. Brand
#2. ProductDescription
#3. Price


# In[26]:


driver=webdriver.Chrome(r"C:\Users\msi 1\Downloads\chromedriver_win32\chromedriver.exe")
#connect to the driver


# In[27]:


#open the naukri page
driver.get("https://www.flipkart.com/")


# In[29]:


product=driver.find_element(By.CLASS_NAME,"_3704LK" )
product.send_keys('sunglasses')


# In[31]:


brand=[]


# In[39]:


#scrap brand
brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[1:20]:
    brand=i.text
    brand_tags.append(brand)


# In[40]:


#scraping job product description
product_desc=[]
product_desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_desc[1:20]:
    product=i.text
    product_desc.append(product)


# In[41]:


#scraping price
price=[]
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags[1:20]:
    price=i.text
    price_tags.append(price)


# In[42]:


print(len(brand),len(product_desc),len(price))


# In[ ]:




