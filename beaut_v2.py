import requests
from bs4 import BeautifulSoup
"""
import time

url="http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")

#soup.select_one()
results = soup.select("#section_body span")

for result in results:
    print("제목: ", result.string)
"""

#로그인
session = requests.session()
url = "http://google.com"
data = {
    "a":"10",
    "b":"20"
}
response = session.post(url,data=data)
response.raise_for_status()

#정보
url = "http://google.com"
response = session.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text,"html.parser")
text = soup.select_one("").get_text()
print(text)