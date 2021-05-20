import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_1248986.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
numberList = list()
spanTag = soup("span")
for tag in spanTag :
    numberList.append(int(tag.string))
print("The sum of the numbers scrape is", sum(numberList))