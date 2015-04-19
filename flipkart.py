from bs4 import BeautifulSoup
import requests
import subprocess
import os,sys
import time

def pricecheck():
	r = requests.get("http://www.flipkart.com/cooler-master-notepal-l1-cooling-pad/p/itmdyh7fzpggufdc")
	# r = requests.get("http://vikasparashar.in/")
	data = r.text
	soup = BeautifulSoup(data)
	for price in soup.find_all(itemprop="price"):
		p = price.get('content')
		p = p.replace(',','')
		if int(p) < 1000:
			subprocess.Popen(['vlc', '-vvv', '/home/vicodin/Music/Music/eminem/01 Rap God.mp3'])
			exit()
		else:
			print "checking...", p
			time.sleep(3600)
			pricecheck()

pricecheck()