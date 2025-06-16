import random
import requests
from selenium import webdriver
import re
from fake_useragent import UserAgent
 
def get_proxy(link):
    while True:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
		path_chromedriver = 'chromedriver.exe' # поменять путь к chromedriver
        driver = webdriver.Chrome(executable_path = path_chromedriver, options=options)
        driver.get("https://hidemyna.me/ru/proxy-list/?maxtime=300&ports=3128..")
        while True:
            time.sleep(1)
            if "maxtime" in driver.page_source:
                ip_list = re.findall(r'\d{2,3}[.]\d{2,3}[.]\d{2,3}[.]\d{2,3}', driver.page_source)
                # print ('ip_list: ',ip_list)
                break
        ua = UserAgent()
        header = {'User-Agent': str(ua.chrome)}
        driver.quit()
        html = None
        for it in range(5):
            print('it =', it)
            proxy = random.choice(ip_list[1:]) + ":3128"
            proxies = {
              'https': 'https://{}'.format(proxy),
            }
            try:    
                html = requests.get(link, proxies=proxies, headers=header).content
                soup = BeautifulSoup(html, 'lxml')
                if html is not None and 'We have detected' not in soup.text:
                   break
            except:
                continue
 
        if html is not None:
            break
        else:
            continue
 
    print('good proxy: {}'.format(proxy))
    driver.quit()
    return proxies # вставить полученные proxies в requests.get