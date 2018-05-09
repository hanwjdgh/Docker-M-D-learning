from sklearn import model_selection, svm, metrics
import glob, os.path,re, json
import pandas as pd

csv = pandas.read_csv("iris.csv")
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

train_data, test_data, train_label, test_label =\
    train_test_split(data,label)

clf = svm.SVC()
clf.fit(train_data,train_label)
result = clf.predict(test_data)
print(result)
score = metrics.accuracy_score(result,test_label)
print(score)