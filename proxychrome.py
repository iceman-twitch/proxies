from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import sys
import os, platform
import random 
import string
import time

proxy = '196.18.149.133:3128'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 OPR/75.0.3969.171'
options = Options()
options.add_argument( "user-agent=" + ua )

options.add_argument( f'--proxy-server={ proxy }' )
chromepath = r'd:\\0\\python\\chromedriver.exe'
chromepath = chromepath.replace("\\","/")
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = chromepath, options=options)
driver.implicitly_wait(55)
driver.set_page_load_timeout(55)
#driver.get( 'https://ident.me/')
driver.get( 'https://www.instagram.com/data/shared_data/')
while True:
    a = 1