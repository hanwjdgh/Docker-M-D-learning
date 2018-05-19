from gensim.models import word2vec
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

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
for word, count in keys[:500]:
    print("{0}({1}) ".format(word, count), end="")
print()

# list로 바꾸기
"""
with open("","w",encoding="utf-8") as fp:
    fp.write(output)
"""

data = word2vec.LineSentance("")
word2vec.Word2vec(data,size=200,window=10,hs=1,min_count=2,sg=1)
model.save("")

# model = word2vec.Word2vec.load("")
# model.most_similar(positive=[""])