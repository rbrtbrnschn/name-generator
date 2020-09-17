#!/usr/bin/env python3

import requests, json
from bs4 import BeautifulSoup

#-------------------------HELPER-----------------------------------------
def loop(_list):
	for x,i in enumerate(_list):
		print(i.get_text())
		#print("---------------------------------------")
		#print(x)
		#print("---------------------------------------")
		#input("ready")

#-------------------------HELPER-----------------------------------------

# Webscraper
uri = "https://family.disney.com/articles/1000-most-popular-girl-names/"
page = requests.get(uri)
page

# Parse html
soup = BeautifulSoup(page.content,"html.parser")
soup_list = list(soup.children)
html = list(soup.children)[10]
html_list = list(html.children)
# LOCATED AT INDEX 5
body = list(html.children)[5]
body_list = list(body.children)
# LOCATED AT INDEX 1
a = list(body.children)[1]
aa = list(a.children)
# LOCATED AT INDEX 3
b = list(a.children)[3]
bb = list(b.children)
# LOCATED AT INDEX 3
c = list(b.children)[7]
cc = list(c.children)
# @ 1
d = list(c.children)[1]
dd = list(d.children)
# @ 5
e = list(d.children)[5]
ee = list(e.children)
# @ 1
f = list(e.children)[1]
ff = list(f.children)
# @ 8
ol = list(f.children)[8]
lis = [i.get_text() for x,i in enumerate(ol) if x % 2 != 0]

def update_file(names):
    pathName = "names.txt"
    with open(pathName,"w") as file:
        json.dump(names, file)
    return names
update_file(lis)
