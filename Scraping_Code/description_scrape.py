from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import csv

options = ChromeOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without GUI).
options.add_argument("--no-sandbox")  # Required for running Chrome in headless mode on some systems.

# Create the undetected_chromedriver instance
driver = Chrome(options=options)

driver.get("https://ie.indeed.com/viewjob?jk=bff803bc53c7af29&from=serp&vjs=3")

job_text = driver.find_element(By.XPATH, '//div[contains(@id, "jobDescriptionText")]')

        
# Check if the job card has all the required elements
#title_element = job_text.find_element(By.XPATH, './/div[contains(@id, "job-title mt-xsm")]')
# Extract job title, company, and location
whole_text = job_text.text


# Print the extracted information
print(whole_text)


# Extract and print the job link
# #link_element = card.find_element(By.TAG_NAME, 'a')
#link = link_element.get_attribute('href')
#print("Job Link:", link)
print("-----------------------")
    
                
driver.quit()