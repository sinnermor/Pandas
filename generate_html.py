import json

import os
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


json_data = json.load(open('data/AnalyzingSourceCode.json'))
items = json_data['issues']

# @app.route("/")
# def template_test():
#     return render_template('templates/new_template.html', my_list=items)

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    fname = "output.html"

    context = {
        'my_list': items
    }
    #
    with open(fname, 'w') as f:
        html = render_template('new_template.html', context)
        f.write(html)


def main():
    create_index_html()


########################################

if __name__ == "__main__":
    main()
