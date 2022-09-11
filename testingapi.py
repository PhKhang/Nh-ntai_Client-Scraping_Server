from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

import urllib.request, os
from flask import Flask
app = Flask(__name__)
       
def createbrowser():
    global browser
    browser = uc.Chrome(use_subprocess=True, version_main=104, suppress_welcome=True)
    print('New browser')

@app.route("/") 
def new_uploads():
    
    try:
        browser.get('https://nhentai.net')
        print('Variable exist.')
    except:
        print('Variable don\'t exist.')
        createbrowser()
    
    browser.minimize_window()
    print('Pseudo browser opened, waiting for Cloudflare protection...')
    browser.get("https://nhentai.net")
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "gallery")))
    
    print('Homepage')
    
    soup = BeautifulSoup(browser.page_source.encode("utf-8"), features="html.parser")
    
    for s in soup.select('script'):
        s.extract() # remove scripts
        
    for s in soup.select('section.advertisement'):
        s.decompose() # remove ads
    
    script = soup.new_tag("script")
    script['src']='https://code.jquery.com/jquery-3.1.1.js'

    scriptbttm = soup.new_tag("script")
    c = open('app.js','r')
    scriptbttm.string=c.read()
    
    soup.html.head.append(script)
    soup.html.body.append(scriptbttm)

    soup.section.extract() # remove ads
    
    stylecontent = soup.new_tag('style')
    c = open('style.css','r')
    stylecontent.string = c.read()
    soup.html.body.append(stylecontent)
    
    return soup.prettify()

@app.route('/g/<g_id>/')
def manga(g_id):
    browser.get("https://nhentai.net"+'/g/'+g_id)
    print('Manga Page')
    
    soup = BeautifulSoup(browser.page_source.encode("utf-8"), features="html.parser")

    for s in soup.select('script'):
        s.extract() # remove scripts
        
    for s in soup.select('section.advertisement'):
        s.decompose() # remove ads
    
    script = soup.new_tag("script")
    script['src']='https://code.jquery.com/jquery-3.1.1.js'

    scriptbttm = soup.new_tag("script")
    c = open('app.js','r')
    scriptbttm.string=c.read()
    
    soup.html.head.append(script)
    soup.html.body.append(scriptbttm)
    
    stylecontent = soup.new_tag('style')
    c = open('style.css','r')
    stylecontent.string = c.read()
    soup.html.body.append(stylecontent)
    
    return soup.prettify()
    
@app.route('/<path:url>/')
def everythingelse(url):
    browser.get("https://nhentai.net"+'/'+url+'/')
    print('Others: ' + "https://nhentai.net"+'/'+url+'/')
    
    soup = BeautifulSoup(browser.page_source.encode("utf-8"), features="html.parser")

    for s in soup.select('script'):
        s.extract() # remove scripts
        
    for s in soup.select('section.advertisement'):
        s.decompose() # remove ads
    
    script = soup.new_tag("script")
    script['src']='https://code.jquery.com/jquery-3.1.1.js'

    scriptbttm = soup.new_tag("script")
    c = open('app.js','r')
    scriptbttm.string=c.read()
    
    soup.html.head.append(script)
    soup.html.body.append(scriptbttm)
    
    stylecontent = soup.new_tag('style')
    c = open('style.css','r')
    stylecontent.string = c.read()
    soup.html.body.append(stylecontent)
    
    return soup.prettify()

if __name__ == "__main__":
    app.run(debug=True)