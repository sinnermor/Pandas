import matplotlib.pyplot as plt
import pandas as pd
import json

json_data = json.load(open('AnalyzingSourceCode.json'))
items = json_data['issues']
df = pd.DataFrame(items)
print(df)