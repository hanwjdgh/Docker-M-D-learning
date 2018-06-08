from sklearn import model_selection, svm, metrics
import glob, os.path,re, json
import matplotlib.pyplot as plt
import pandas as pd

datas = [[0,0],[1,0],[0,1],[1,1]]
labels = [0,1,1,0]
examples = [[0,0],[1,0]]
examples_label = [0,1]

clf = svm.SVC()
clf.fit(datas,labels)
result = clf.predict(examples)
print(result) #[0,1]

score = metrics.accuracy_score(examples_label,result)
print(score)