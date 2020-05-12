#!/usr/bin/python3
import os
import threading
import urllib3 

urls=["https://api.github.com ", " http://bilgisayar.mu.edu.tr/ ",
" https://www.python.org/ ", " http://akrepnalan.com/ceng2034 ",
"https://github.com/caesarsalad/wow "]

def checking_url(url):
  for i in range (len(urls)):
    a=request.get(urls[i])
    if a.status_code // 100==2:
      return 'valid'
    return 'invalid'

  
  urlChecker= urllib3.urlopen(url)
  html =urlChecker.read()
  print(html)



threads= [threading.Thread(target=checking_url, args= (urls)) for url in urls]

for thread in threads:
  thread.start()
for thread in threads:
  thread.join()
