import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

json_data=json.load(open('data/AnalyzingSourceCode.json'))
    # open('data/AnalyzingSourceCode.json').read()
items = json_data['issues']
df = pd.DataFrame(items)
# df.groupby(axis='rule')
dnn = df.groupby(['component','rule','message','severity','line']).size().unstack

df1=  df[['component','rule','message','severity','line']]
# tt = pd.pivot_table(items,'component','rule','message','severity','line')
# print(tt)

# df.rule df.component
# print(df1)
df1.to_html('index.html')
#