import json
import pandas as pd

# Read json files and write into csv files


def read_json(file):
    res = dict()
    with open(file, encoding='utf-8') as f:
        for line in f:
            temp_dic = json.loads(line)
            if not res:
                for key in temp_dic:
                    res[key] = list()
            for key in temp_dic:
                res[key].append(temp_dic[key])
    res = pd.DataFrame(res)
    return res


filelist = ['business', 'covid', 'review', 'tip', 'user']
data = dict()
for file in filelist:
    res = read_json(file + '.json')
    data[file] = res


# business_id with 'Cocktail Bars' in categories
bars_business_id = list()
for i in range(len(data['business'])):
    if data['business'].iloc[i, -2] and data['business'].iloc[i, -3] and data['business'].iloc[i, -4] and 'Cocktail Bars' in data['business'].iloc[i, -2].split(', '):
        bars_business_id.append(data['business'].iloc[i, 0])

# filter data
bars_data = dict()
filelist2 = ['business', 'covid', 'review', 'tip']
for file in filelist2:
    bars_data[file] = data[file][data[file]
                                 ['business_id'].isin(bars_business_id)]
    bars_data[file].reset_index(drop=True, inplace=True)
bars_data['user'] = data['user'][data['user']
                                 ['user_id'].isin(bars_data['review']['user_id'].unique())]
bars_data['user'].reset_index(drop=True, inplace=True)

# Write into csv files
for file in filelist:
    bars_data[file].to_csv('bars_' + file + '.csv', index=False)
