#!/usr/bin/python
import urllib
import urllib3
from urllib import urlopen as o
import requests, re, urllib2, os, sys, codecs					
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time,random
from random import sample as rand				   		
from platform import system	
import datetime
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init		
from urlparse import urlparse									
from requests.packages.urllib3.exceptions import InsecureRequestWarning

init (autoreset=True)

requests.packages.urllib3.disable_warnings (InsecureRequestWarning)

####### Colors ######	
	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT										

####################### 

os.system('clear')
start_raw = raw_input("\033[92m[>]\033[91m List Of Sites [\033[97mlist.txt\033[91m]:# ")
try:
    with open(start_raw, 'r') as f:
        sites = f.read().splitlines()
except IOError:
	pass

try:
    sites = list((sites))
except NameError:
    print '\n [!] List Not Found\n'
    raw_input(' \033[92m[\033[91mExit\033[92m]')


Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"

def rand_str (len = None) :
	if len == None :
		len = 8
	return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))
	
def prepare(url, ua):
	try:
		global user_agent
		headers = {
			'User-Agent' : user_agent,
			'x-forwarded-for' : ua
		}
		cookies = urllib2.Request(url, headers=headers)
		result = urllib2.urlopen(cookies)
		cookieJar = result.info().getheader('Set-Cookie')
		injection = urllib2.Request(url, headers=headers)
		injection.add_header('Cookie', cookieJar)
		urllib2.urlopen(injection)
	except:
		pass
	
	
def cms(url):
    
    try:
        if requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[Joomla] \033[92mURL:",url 
            open('CMS/Joomla.txt', 'a').write(url+'\n')
            
            
        elif requests.get(url + "/language/en-GB/en-GB.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/language/en-GB/en-GB.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[Joomla] \033[92mURL:",url 
            open('CMS/Joomla.txt', 'a').write(url+'\n')
            
    except :
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		if "/wp-content/" in Checktwo.text.encode('utf-8'):
			print "\033[92m[Wordpress] \033[92mURL:",url
			open('CMS/Wordpress.txt', 'a').write(url+'/wp-login.php\n')
			open('CMS/wp.txt','a').write(url+'\n')
					
		else:
			print ''.format(sb, sd, url, fc,fc, sb,fr)       		
    except :
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		if "/sites/default/" in Checktwo.text.encode('utf-8'):
			print "\033[92m[Drupal] \033[92mURL:",url
			open('CMS/Drupal.txt', 'a').write(url+'\n')
			drupal(url)			       			
    except :
        pass	
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "prestashop" in Checktwo.text.encode('utf-8'):
			print "\033[0m[Prestashop] \033[92mURL:",url
			
			open('CMS/Prestashop.txt', 'a').write(url+'\n')
			prestashop(url)					
    except :
        pass
    try:		
		
		CheckOsc = requests.get(url + '/admin/images/cal_date_over.gif')
		CheckOsc2 = requests.get(url + '/admin/login.php')
		
		if 'GIF89a' in CheckOsc.text.encode('utf-8') or 'osCommerce' in CheckOsc2.text.encode('utf-8'):
			print "\033[0m[osCommerce] \033[92mURL:",url
			open('CMS/osCommerce.txt', 'a').write(url+'\n')
			osrce(url)						
    except :
        pass
    try:		
		
		Checktree = requests.get(url + '/application/configs/application.ini')
		
		if "APPLICATION_PATH" in Checktree.text.encode('utf-8'):
			print "\033[92m[Zen] \033[92mURL:",url
			
			open('CMS/zen.txt', 'a').write(url+'\n')
			zenbot(url)						
    except :
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "Magento" in Checktwo.text.encode('utf-8'):
			print "\033[92m[Magento] \033[92mURL:",url
			
			open('CMS/Magento.txt', 'a').write(url+'\n')					
    except :
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		
		if "OpenCart" in Checktwo.text.encode('utf-8'):
			print "\033[92m[OpenCart] \033[92mURL:",url
			
			open('CMS/OpenCart.txt', 'a').write(url+'\n')					
    except :
        pass
    try:		
		
		Checktwo = requests.get(url, timeout=5)
		if "vBulletin" in Checktwo.text.encode('utf-8'):
			print "\033[92m[vBulletin] \033[92mURL:",url
			open('CMS/vBulletin.txt', 'a').write(url+'\n')					
    except :
        pass
		
	
def Main():
    try:
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(cms, sites)
        print('Finished in : ' + str(timer() - start) + ' seconds')
    except :
        pass


if __name__ == '__main__':
    Main()
