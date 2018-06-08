import codecs, glob, os
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from konlpy.tag import Kkma
from konlpy.tag import Komoran

print(twitter.morphs(u'단독입찰보다 복수입찰의 경우'))
print(twitter.nouns(u'유일하게 항공기 체계 종합개발 경험을 갖고 있는 KAI는'))
print(twitter.phrases(u'날카로운 분석과 신뢰감 있는 진행으로'))
print(twitter.pos(u'이것도 되나욬ㅋㅋ'))
print(twitter.pos(u'이것도 되나욬ㅋㅋ', norm=True))
print(twitter.pos(u'이것도 되나욬ㅋㅋ', norm=True, stem=True))