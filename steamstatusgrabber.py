import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
quote_page = 'http://steamcommunity.com/profiles/XXXXXXXXXXXXXX'
# above url must be replaced with a public steam user's profile
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
price_box = soup.find('div', attrs={'class':'profile_in_game_header'})
price = price_box.text
print price
print str(datetime.now())


import csv
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([price, datetime.now()])