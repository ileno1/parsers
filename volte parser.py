s = open('E:\\Downloads\\MemExpFile_HSS9860_31.txt', 'r')
s = s.readlines()
s = str(s[1:])
s = s.strip()
import re
import pandas as pd



regex1 = r'IMPI=(?P<IMPI>)[+0-9]+[^\d][a-z]+[^\d][a-z]+[0-9]+[^\d][a-z]+[0-9]+[^\d][3][a-z]+[^\d][a-z]+'
regex2 = r"UserState=(?P<UserState>[1-2]+)"
regex3 = r'[^\d](SUBBEGIN)'
regex4 = r'[^\d](SUBEND)'
data_dict = {}
def ordered_set(inlist):
    out_list = []
    for val in inlist:
        if not val in out_list:
            out_list.append(val)
    return out_list

def str_match(s):
    data = []
    for match in re.finditer(regex1, s, re.MULTILINE|re.DOTALL):
        matches1 = match.group()
        print(matches1)
        list_impu = matches1.split('=')
    for match in re.finditer(regex2, s, re.MULTILINE|re.DOTALL):
        data.append(ordered_set(list_impu))
        matches2 = match.group()
        data.append(matches2.split('='))
    return data 


for i in str_match(s):
    if i[0] not in data_dict:
        data_dict[i[0]] = [i[1]]

    else:
        data_dict[i[0]].append(i[1])

pd.DataFrame.from_dict(data_dict, orient = 'index').T.to_csv('filename.csv')