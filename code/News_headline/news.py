import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://twitter.com/i/moments'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

news_headline = soup.find_all('div', class_='MomentCapsuleSummary-details')

for news_headlines in news_headline:
	for tag in news_headlines.find_all('a'):
		try:
			print(tag['title'])
		except KeyError:
			pass
