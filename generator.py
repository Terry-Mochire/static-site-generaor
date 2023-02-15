#!/usr/bin/env python3
import os

import markdown
from jinja2 import FileSystemLoader, Environment


# Convert markdown to html
def markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    with open(output_file, 'w') as f:
        f.write(html)


# Render Jinja2 template with data
def render_template(template_file, output_file, context):
    if not os.path.exists('templates/'):
        os.makedirs('templates/')

    loader = FileSystemLoader('templates/')
    env = Environment(loader=loader)
    template = env.get_template(template_file)
    html = template.render(context)
    print(html)

    with open(output_file, 'w') as f:
        f.write(html)
