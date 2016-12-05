
from bs4 import BeautifulSoup
from urllib2 import urlopen

import pandas

html0 = urlopen("https://pip.pypa.io/en/latest/installing/")


soup = BeautifulSoup(html0, 'html.parser')

print("ok")