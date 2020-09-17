from urllib import request
import requests
from bs4 import BeautifulSoup
import lxml
import re


##The question is how can I do specific query from form without circular imports? This current strategy is overkill.


#Mohawk#
url = "http://www.mohawkaustin.com/events/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

lstofdates = []
alldates = soup.find_all('span','dates')
for date in alldates:
	lstofdates.append(date.string)

print(lstofdates[0])
print(lstofdates)
print(len(lstofdates))

lstofdates2 = []
for el in lstofdates:
	lstofdates2.append(el[-6:])
	
print(lstofdates2)		

allshows = soup.find_all('h1', "event-name headliners")

lstofshows = []
for show in allshows:
	lstofshows.append(show.string)

print(lstofshows)


mohawkenvelope = dict(zip(lstofdates2, lstofshows)) 
print(mohawkenvelope)

#mohawkshow = a[0].string
#print(mohawkshow)



#Parish 

url = "https://www.theparishaustin.com/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')


a = soup.find_all('div', 'tw-name')
zoom1 = a[0]
#print(zoom1)

zoom3 = zoom1.children

lst =[]
for el in zoom3:
	lst.append(el.string)    #### Why are these not the same? 
	parishshow = el.string  #### Why are these not the same?
	#print(parishshow)
#print(lst)
parishshow = lst[1]
#print(parishshow)