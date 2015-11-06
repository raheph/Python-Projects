import urllib.request
import re
url = urllib.request.urlopen("http://www.google.com")
page = url.read()
links =re.findall("<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", page)
for link in links:
    print('href: %s, HTML text: %s' % (link[0], link[1]))
