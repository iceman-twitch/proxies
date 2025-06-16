from xml.etree.ElementTree import tostring
import requests, time, random, threading
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def testproxy( header, proxy ):
    http_proxy  = proxy
    proxyDict = { 
                "http"  : http_proxy,
                }
    r = requests.get( "https://twitch.tv/theicyman", proxies=proxyDict, headers = header )
    if r.status_code == 200:
        print( http_proxy, header )

class Test:
    def __init__( self ):
        self.lock = threading.Lock()
        self.url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=500&anonymity=elite"
        self.software_names = [SoftwareName.CHROME.value]
        self.operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
        self.header = ""
        self.user_agent = ""
        self.proxyhardtest()
        
    def getuseragent( self ):
        self.user_agent_rotator = UserAgent(software_names=self.software_names, operating_systems=self.operating_systems, limit=100)
        self.user_agent = self.user_agent_rotator.get_random_user_agent()
        # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        
    def getheader( self ):
        self.getuseragent()
        self.header = { 'User-Agent': self.user_agent }

    def getproxylist( self ):
        
        self.getheader()
        response = requests.get( self.url, headers = self.header ).text.split( '\n' )
        proxies = [ item.strip() for item in response ]
        # address = address[random.randint(0,len(proxies)-1)]
        # print(address)
        return proxies

    def getproxy( self, proxies, line ):
        proxy = proxies[ line ]
        
        return proxy

    def testproxy( self, proxy ):
        http_proxy  = proxy
        self.getheader()
        proxyDict = { 
                    "http"  : http_proxy,
                    }
        r = requests.get( "https://twitch.tv/theicyman", proxies=proxyDict, headers = self.header )
        if r.status_code == 200:
            print( http_proxy )

    def proxyhardtest( self ):
        proxies = self.getproxylist()
        i = 0
        while i < len( proxies ):
            if i < len( proxies ):
                proxy = self.getproxy( proxies, i )
                if proxy != "":
                    self.getheader()
                    threading.Thread( target = testproxy, args = ( self.header, proxy, ) ).start() 
                i = i + 1

if __name__ == '__main__':
    Test()