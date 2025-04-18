from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time

''' 
selenium webdriver to open new chrome window and have full control over it 
selenium.common.exceptions for handling missing or unclickable buttons
selenium.by to define what type of selectors to navigate through elements and attributes
time this is responsible for waiting till the page loaded
'''

url = f'https://www.glassdoor.com/Job/egypt-data-analyst-jobs-SRCH_IL.0,5_IN69_KO6,18.htm'
driver = webdriver.Chrome()
driver.get(url)
job_postings = []
seen_jobs = set()


'''
open a window that selenium controls 
initializing a list that will store the data we scraped
seen jobs role is to store job ids to avoid duplicates 
'''
while True :
    time.sleep(5) # wait to page to load 
    soup = BeautifulSoup(driver.page_source,'html.parser')
    jobs_block = soup.find("div", {'class': 'JobsList_wrapper__EyUF6'})
    jobs = jobs_block.find_all("li",{'class':'JobsList_jobListItem__wjTHv'})
    new_jobs_added = 0

    for job in jobs:
        job_id = job.get('data-id') or str(job)  # get the id of each job
        if job_id in seen_jobs:                  # check the id if its already stored we skip it to avoid duplicates
            continue
        try:
            job_title = job.find("div",{'class':'JobCard_jobCardContainer__arQlW'}).a.text.strip()
            company = job.find("div",{'class':'EmployerProfile_employerNameContainer__ptolz'})
            company_name = company.find('span',{'class':'EmployerProfile_compactEmployerName__9MGcV'}).text.strip()
            location = job.find("div",{'class':'JobCard_location__Ds1fM'}).text.strip()
            days = job.find("div",{'class':'JobCard_listingAge__jJsuc'}).text.strip()
            description = job.find("div",{'class':'JobCard_jobDescriptionSnippet__l1tnl'}).text.strip()
            job_link = job.find('a', {'class': 'JobCard_jobTitle__GLyJ1'})['href']

            job_postings.append({
                "Title": job_title,
                "Company": company_name,
                "Location": location,
                "Posted": days,
                "link":job_link,
                "Description": description
            })

            seen_jobs.add(job_id)
            new_jobs_added += 1
        except Exception as e:
            print("Error parsing job:", e)
            continue

    print(f"Added {new_jobs_added} new jobs")

    if new_jobs_added == 0:
        print("No new jobs found, ending loop.")
        break
    ''' 
    The part that is responsible for clicking the show more button :
    first we save the xpath of the button in load_more_button variable then we scroll down in the page
    till we found it , then we click on it 
    '''
    try:
        load_more_button = driver.find_element(By.XPATH,'//*[@id="left-column"]/div[2]/div/div/button')
        driver.execute_script("arguments[0].scrollIntoView(true)",load_more_button)
        time.sleep(2)
        load_more_button.click()
        print("Clicked 'Show More' button")
    except NoSuchElementException:
        print("No more 'Show More' button found.")   
        break
    except ElementClickInterceptedException:
        print("Button not clickable at the moment. Retrying...")
        time.sleep(2)

df = pd.DataFrame(job_postings)
df.to_excel("glassdoor_data_analyst_jobs.xlsx", index=False)
print("Saved to Excel ✅")

# By Abdelrhman Yakout