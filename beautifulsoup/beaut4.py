import requests
from bs4 import BeautifulSoup

import time

url="http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

#soup.select_one()
results = soup.select("#section_body span")

for result in results:
    print("제목: ", result.string)
