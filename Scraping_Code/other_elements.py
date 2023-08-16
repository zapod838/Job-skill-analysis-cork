from undetected_chromedriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import csv

options = ChromeOptions()
options.add_argument("--headless")  # Run the browser in headless mode (without GUI).
options.add_argument("--no-sandbox")  # Required for running Chrome in headless mode on some systems.

# Create the undetected_chromedriver instance
driver = Chrome(options=options)

def scrape_data(num_pages_to_scrape):
    
    try:
        start_url = "https://ie.indeed.com/jobs?q=data+analyst&l=cork&start={}"
        page_number = 0
        job_description_urls = []

        for _ in range(num_pages_to_scrape):
            url = start_url.format(page_number)
            driver.get(url)
            time.sleep(10)
            #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "job-search-193lseq")]')))

            job_cards = driver.find_elements(By.XPATH, '//div[contains(@class, "job_seen_beacon")]')

            for card in job_cards:
                try:
                    # Check if the job card has all the required elements
                    jk_element = card.find_element(By.TAG_NAME, 'a')
                    # Extract job title, company, and location
                    jk = jk_element.get_attribute('data-jk')
                    new_url = "https://ie.indeed.com/viewjob?jk={}&from=serp&vjs=3"
                    job_description_urls.append(new_url.format(jk))
                except NoSuchElementException:
                    continue
            # Increment the page number by 10 for the next page
            page_number += 10

            # Check if there are any more job cards on the next page
            if len(job_cards) == 0:
                # If there are no more job cards, it indicates we have reached the last page
                break

            time.sleep(10)

        # Now iterate through job_description_urls to scrape detailed descriptions
        for url_1 in job_description_urls:
            driver.get(url_1)
            time.sleep(10)
            job_title_element = driver.find_element(By.XPATH, './/h1')
            company_element = driver.find_element(By.XPATH, './/div[contains(@class, "css-1h46us2 eu4oa1w0")]')
            location_element = driver.find_element(By.XPATH, './/div[contains(@class, "css-6z8o9s eu4oa1w0")]')
            #job_text = driver.find_element(By.XPATH, '//div[contains(@id, "jobDescriptionText")]')
            
            #whole_text = job_text.text

            #print(whole_text)
            job_title = job_title_element.text
            company = company_element.text
            location = location_element.text

            print("Job Title: ", job_title)
            print("Company: ", company)
            print("Company Location: ", location)
            print("-----------------------")    

    except NoSuchElementException:
        print("No such element found on the page!")

    finally:
        # Close the browser window and quit the driver.
        driver.quit()

    print(f"Data from {num_pages_to_scrape} pages has been successfully scraped.")

scrape_data(num_pages_to_scrape=1)
