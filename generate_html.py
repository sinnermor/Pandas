import json

import os
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template


app = Flask(__name__)


json_data = json.load(open('data/AnalyzingSourceCode.json'))
items = json_data['issues']
minor = 0
major = 0
critical = 0
info = 0
for el1 in items:
    sev = el1.get('severity')
    if sev=='MINOR':
        minor = minor + 1
    elif sev == "MAJOR":
        major = major + 1
    elif sev == "CRITICAL":
        critical = critical + 1
    else: info = info + 1

bug_count = {"info": info, "minor": minor, "major": major, "critical": critical}


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
        'my_list': items,
        'bugs': bug_count,
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
