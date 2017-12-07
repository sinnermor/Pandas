import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


def generate_data():
    json_data=json.load(open('data/AnalyzingSourceCode.json'))
    items = json_data['issues']

    df = pd.DataFrame(items)
    print(df[:1]['component'])

    dnn = df.groupby(['component','rule','message','severity','line']).size()

    table = pd.pivot_table(df, index=['component', 'message', 'rule'], values='line')
    return table

table = generate_data()
generate_data()
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("templates/myreport.html")

template_vars = {"title": "test",
                 "my_pivot_table": table.to_html()}

html_out = template.render(template_vars)
with open("index.html", "w") as e:
    e.write(html_out)