from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

from sonar import df1

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("templates/myreport.html")

template_vars = {"title" : "Sales Funnel Report - National",
                 "national_pivot_table": df1.to_html()}

html_out = template.render(template_vars)


HTML(string=html_out).write_pdf("report.pdf")