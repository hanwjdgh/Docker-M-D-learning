import codecs, glob, os
from bs4 import BeautifulSoup
from konlpy.tag import Komoran
komoran = Komoran()

files = glob.glob("./Corpus/Input_Data/**/*.txt",recursive=True)
for file_name in files:
    basename = os.path.basename(file_name)
    categorty = basename.split("_")[0][5:]
    i_file = open(file_name,"r",encoding="utf-8")

    t_str = "./data/"+categorty+"/"+basename

    w_file = open(t_str,"w",encoding="utf-8")

    while True:
        answer = ""
        text = i_file.readline()
        if not text: 
            break
        if len(text) > 1:
            s_line = text[:-1].split("\t")
            t_line = komoran.pos(s_line[0]) 

            for i, lists in enumerate(t_line):
                if i < len(t_line)-1:
                    answer += lists[0]+"/"+lists[1]
                    answer += "+"
                else:
                    answer += lists[0]+"/"+lists[1]
            w_file.write(s_line[0]+'\t'+answer+'\n')
        else:
            w_file.write('\n')
    i_file.close()
    w_file.close()