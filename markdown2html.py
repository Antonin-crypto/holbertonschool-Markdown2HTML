#!/usr/bin/python3
import sys
import os
import markdown


if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

with open(input_file, 'r', encoding='utf-8') as md_file:
    markdown_content = md_file.read()

html_content = markdown.markdown(markdown_content)

with open(output_file, 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)
sys.exit(0)
