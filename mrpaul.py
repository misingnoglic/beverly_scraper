import requests
url = 'bhhs.bhusd.org/apps/staff/' #Url to parse from
r = requests.get("http://" +url)

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
    
data = r.text
data = data.splitlines()
names = []
for line in data:
    if '''<span id="staff''' in line:
        name = strip_tags(line)
        name = name.strip('\t')
        names.append(name)
names = names[1:] #taking out attendence office
for name in names:
    if ',' in name:
        l = name.split(',')
        print l[1][1]+l[0]+"@bhusd.org"
