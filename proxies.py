from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time


def get_proxy_list():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    header = {'User-Agent': user_agent}
    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=500&anonymity=elite"
    response = requests.get(url, headers=header).text.split('\n')
    address = [item.strip() for item in response]
    return address

def open_whats_my_ip(PROXY):
    print(PROXY)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={PROXY}')

    chrome = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\Zygimantas\Desktop\Python\BE selenium\chromeriver\chromedriver.exe")
    chrome.get("https://whatsmyip.com/your-ip-address")
    chrome.maximize_window()
    input('press enter to continous')
    chrome.close()

for proxy in get_proxy_list()[:1]:
    open_whats_my_ip("140.82.33.196:30162")