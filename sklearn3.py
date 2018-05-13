from sklearn import model_selection, svm, metrics
import glob, os.path,re, json
import matplotlib.pyplot as plt
import pandas as pd

files = glob.glob("./train/*.txt")
train_data = []
train_label = []

for file_name in files:
    # 레이블 구하기
    basename = os.path.basename(file_name)
    lang = basename.split("-")[0]
    # 텍스트 추출하기
    file = open(file_name,"r",encoding="utf-8")
    text = file.read()
    text = text.lower()
    file.close()
    # 알파벳 출현 빈도 구하기
    code_a = ord("a")
    code_z = ord("z")
    count = [0 for n in range(0,26)]
    for character in text:
        code_current = ord(character)
        if code_a <= code_current <=code_z:
            count[code_current - code_a] += 1
    # 정규화
    total = sum(count)
    count = list(map(lambda n: n/total, count))
    # 리스트에 넣기
    train_data.append(count)
    train_label.append(lang)

print(train_data)
graph_dic={}
for i in range(0,len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not (label in graph_dic):
        graph_dic[label] = data
asclist = [[chr(n) for n in range(97,97+26)]]
df = pd.DataFrame(graph_dic,index=asclist)