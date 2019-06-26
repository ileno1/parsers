import re
import pandas as pd
import sys

# Regex matches one IMPI with next UserState - any IMPI in between is skipped
regex =  r"IMPI=(?P<IMPI>)[+0-9]+[^\d][a-z]+[^\d][a-z]+[0-9]+[^\d][a-z]+[0-9]+[^\d][3][a-z]+[^\d][a-z]+"
regex2 = r"UserState=(?P<UserState>[1-2]+)"
data_dict = {}
def parse_data(infile):
    with open(infile, 'r') as s:
        s = s.readlines()
        s = str(s[1:])
        data = []
        m = re.findall('SUBBEGIN(.*?)SUBEND', s, re.MULTILINE)
        for e in m:
            impi = re.search(regex, e).group().split('=')
            data.append(impi)
            if e.find('UserState') > -1:
                user = re.search(regex2, e)
                if user:
                    state = user.group().split('=')
                    data.append(state)
            else:
                data.append(['UserState', '0'])
    return data


if __name__ == "__main__":
    infile = sys.argv[1]
    for i in parse_data(infile):
        if i[0] not in data_dict:
            data_dict[i[0]] = [i[1]]

        else:
            data_dict[i[0]].append(i[1])

    pd.DataFrame.from_dict(data_dict, orient = 'index').T.to_csv(sys.argv[2])
