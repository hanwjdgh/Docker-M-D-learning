import codecs, glob, os
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from konlpy.tag import Kkma
from konlpy.tag import Komoran

file = codecs.open("","r",encoding="utf-16")

soup = BeautifulSoup(file, "html_parser")
body = soup.select_one("text > body")
text = body.getText()
 
twitter = Twitter()

word_dic ={}
lines = text.split("\r\n")
for line in lines:
    malist = twitter.pos(line)
    for word in malist:
        if word[1] == "Noun": 
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 


keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()