import requests
url = 'bhhs.bhusd.org/apps/staff/' #Url to parse from
r = requests.get("http://" +url)

from HTMLParser import HTMLParser

class MLStripper(HTMLParser): #TBH I stole this from stackoverflow, strips html tags from strings
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
    
data = r.text #text on the url page
data = data.splitlines() #splits it into a list of lines
names = [] #list of names
for line in data:
    if '''<span id="staff''' in line: #line with a name
        name = strip_tags(line) #strips the tags
        name = name.strip('\t') #takes out the tabs in the beginning
        names.append(name) #adds it to a list of names
names = names[1:] #taking out attendence office
for name in names:
    if ',' in name: #if it's an actual name
        l = name.split(',') #split it by the first/last name
        print l[1][1]+l[0]+"@bhusd.org" #print out first initial last name @ bhusd.org


#Sorry I didn't have any permutations or generators in here Mr. Paul :(
