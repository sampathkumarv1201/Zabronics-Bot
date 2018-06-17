import urllib2 
from bs4 import BeautifulSoup
page_link='http://results.kongu.edu/allresout.php?regno=15CSR178-ODD_2017-NOVEMBER_2017'
page=urllib2.urlopen(page_link)
soup=BeautifulSoup(page,'html.parser')
#print(soup)
name=soup.find_all("th")
'''for n in name:
	print(n)'''
print(name[4].text)
print(name[5].text)
print(name[6].text)
print(name[28].text)

