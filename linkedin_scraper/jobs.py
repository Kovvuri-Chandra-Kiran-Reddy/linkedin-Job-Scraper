from selenium.common.exceptions import TimeoutException

from .objects import Scraper
from . import constants as c
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Job(Scraper):

    def __init__(
        self,
        linkedin_url=None,
        job_title=None,
        company=None,
        company_linkedin_url=None,
        location=None,
        posted_date=None,
        applicant_count=None,
        job_description=None,
        benefits=None,
        driver=None,
        close_on_complete=True,
        scrape=True,
        already_applied = None,
        easy_apply = None,
    ):
        super().__init__()
        self.linkedin_url = linkedin_url
        self.job_title = job_title
        self.driver = driver
        self.company = company
        self.company_linkedin_url = company_linkedin_url
        self.location = location
        self.posted_date = posted_date
        self.applicant_count = applicant_count
        self.job_description = job_description
        self.benefits = benefits
        self.already_applied = already_applied
        self.easy_apply = easy_apply

        if scrape:
            self.scrape(close_on_complete)

    def __repr__(self):
        return f"<Job {self.job_title} {self.company}>"

    def scrape(self, close_on_complete=True):
        if self.is_signed_in():
            self.scrape_logged_in(close_on_complete=close_on_complete)
        else:
            raise NotImplemented("This part is not implemented yet")

    def to_dict(self):
        return {
            "linkedin_url": self.linkedin_url,
            "job_title": self.job_title,
            "company": self.company,
            "company_linkedin_url": self.company_linkedin_url,
            "location": self.location,
            "posted_date": self.posted_date,
            "applicant_count": self.applicant_count,
            "job_description": self.job_description,
            "benefits": self.benefits,
            "already_applied":self.already_applied,
            'easy_apply':self.easy_apply
        }


    def scrape_logged_in(self, close_on_complete=True):
        driver = self.driver
        
        driver.get(self.linkedin_url)
        self.focus()
        self.job_title = self.wait_for_element_to_load(name="job-details-jobs-unified-top-card__job-title").text.strip()
        self.easy_apply = ''
        self.company = self.wait_for_element_to_load(name="job-details-jobs-unified-top-card__primary-description").text.strip()
        self.company_linkedin_url = None
        self.already_applied = None
        job_description_elem = self.wait_for_element_to_load(name="jobs-description")
        self.mouse_click(job_description_elem.find_element(By.TAG_NAME,"button"))
        job_description_elem = self.wait_for_element_to_load(name="jobs-description")
        job_description_elem.find_element(By.TAG_NAME,"button").click()
        self.job_description = job_description_elem.text.strip()
        self.benefits = None

        if close_on_complete:
            driver.close()