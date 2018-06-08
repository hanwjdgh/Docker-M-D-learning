import csv, codecs
"""
csv = """"""\
p,x,s,n,t,p,f,c,n,k,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,y,t,a,f,c,b,k,e,c,s,s,w,w,p,w,o,p,n,n,g
e,b,s,w,t,l,f,c,b,n,e,c,s,s,w,w,p,w,o,p,n,n,m
p,x,y,w,t,p,f,c,n,n,e,e,s,s,w,w,p,w,o,p,k,s,u
e,x,s,g,f,n,f,w,b,k,t,e,s,s,w,w,p,w,o,e,n,a,g\
""""""
splitted = csv.split("\n")
for item in splitted:
    list_mushroom = item.split(",")
    # 요소 하나 선택
    print(list_mushroom[0])
    print(list_mushroom[-1])

    # 요소 범위 선택
    print(list_mushroom[1:4])
    print(list_mushroom[5:])
"""

filename = "test.csv"
file = codecs.open(filename,"r","euc_kr")
reader = csv.reader(file,delimiter=",",quotechar='"')

for cells in reader:
    print(cells[1],cells[2])