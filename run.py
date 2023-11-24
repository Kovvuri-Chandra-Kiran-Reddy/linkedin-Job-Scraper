from linkedin_scraper import JobSearch, actions,parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

email = input("Enter ur email id : ")
password = input("Enter ur password : ")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

actions.login(driver, email, password)
job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)

job_listings_sde = job_search.search("C++ Developer")
parse.main(job_listings_sde, 'LinkedIn-data', 'linkedin-scrapper-405914-90250fc9ee1d.json')
print("SUCCESS! job list ready to view")