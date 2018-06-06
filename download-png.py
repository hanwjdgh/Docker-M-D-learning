import urllib.request

"""
url ="http://uta.pw/shodou/img/28/214.png"
savename ="test.png"

mem = urllib.request.urlopen(url).read()

#urllib.request.urlretrieve(url,savename)

with open(savename,mode="wb") as f:
    f.write(mem)
    print("저장되었습니다!")
"""
url = "http://api.aoikujira.com/ip/ini"
mem = urllib.request.urlopen(url).read()
print(mem.decode("utf-8"))
