import feedparser
import urllib2

from settings import url,folder,timeout
from watchlist import list

feed = feedparser.parse('https://www.nyaa.se/?page=rss')
i = 0;
x = 0;

feedLen = len(feed['entries'])
listLen = len(list)

while(i < feedLen):
	while(x < listLen):
		if(list[x]['Title'] in feed['entries'][i]['title']):
			ok = 1
			title = feed['entries'][i]['title']
			words = list[x]['Keywords']
			forbidden = list[x]['Forbidden']
			if all(x in title for x in words):
				if not any(x in title for x in forbidden):
					t = feed['entries'][i]['title']
					t = folder+t+suffix
					link = feed['entries'][i]['link']
					print t
					print link
					content = urllib2.urlopen(link).read()
					f = open(t, 'w')
					f.write(content)
					f.close()
		x = x + 1
	x = 0
	i = i +1
print 'Finished!'
