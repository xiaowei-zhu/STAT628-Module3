import pandas as pd
import numpy as np

business = pd.read_csv('bars_business.csv')
business['attributes'] = business['attributes'].apply(eval)

att_dict = {}
for index, row in business['attributes'].items():
    for k, v in row.items():
        if k not in att_dict:
            att_dict[k] = 0
        att_dict[k] += 1

att_Ser = pd.Series(att_dict)
att_Ser = att_Ser[pd.Series(att_dict)/len(business) > 0.7]

att_df = pd.DataFrame(data=np.NaN, index=business.index, columns=att_Ser.keys())

for index, rows in att_df.iterrows():
    for k in business.loc[index, 'attributes']:
        if k in att_Ser.keys():
            att_df.loc[index, k] = business.loc[index, 'attributes'][k]


# auto-EDA
#from dataprep.eda import create_report
#create_report(att_df)