from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import urllib.request, os

def new_uploads():
    browser = uc.Chrome(use_subprocess=True, version_main=104, suppress_welcome=True)
    browser.minimize_window()
    browser.get("https://nhentai.net")
    soup = BeautifulSoup(browser.page_source)
    
    print(soup)

    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gallery")))

        uploads = []
        new_uploads = browser.find_elements(by=By.CLASS_NAME, value="gallery")
        for i in new_uploads[5:30]:
            caption = i.find_element(by=By.CLASS_NAME, value="caption")
            uploads.append(caption.text)

        browser.quit()
        return uploads
        
    except TimeoutException:
        return "TimeoutException: Loading took so much time!"


if __name__ == "__main__":
    print(new_uploads())