import re
import pandas as pd
s = open('E:\\Downloads\\MemExpFile_HSS9860_31.txt', 'r')
s = s.readlines()
s = str(s[1:])

# Regex matches one IMPI with next UserState - any IMPI in between is skipped
regex =  r"IMPI=(?P<IMPI>)[+0-9]+[^\d][a-z]+[^\d][a-z]+[0-9]+[^\d][a-z]+[0-9]+[^\d][3][a-z]+[^\d][a-z]+"
regex2 = r"UserState=(?P<UserState>[1-2]+)"
regex3 = r'[^\d](SUBBEGIN)'
regex4 = r'[^\d](SUBEND)'
data_dict = {}
def parse_data(s):
	data = []
	if re.search(regex3, s):
		for match in re.finditer(regex, s):
			if match.group():
				if re.search(regex4, s):
					matches1 = match.group()
					list_impu = matches1.split('=')
					data.append(list_impu)
		for match in re.finditer(regex2, s):
			if match.group():
				if re.search(regex4,s):
					matches2 = match.group()
					list_user = matches2.split('=')
					data.append(list_user)
				else:
					if match.group() is None:
						empty = 'UserState=0'
						list_empty = empty.split('=')
						data.append(list_empty)
	return data

for i in parse_data(s):
    if i[0] not in data_dict:
        data_dict[i[0]] = [i[1]]

    else:
        data_dict[i[0]].append(i[1])

pd.DataFrame.from_dict(data_dict, orient = 'index').T.to_csv('filename2.csv')
