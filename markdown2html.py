#!/usr/bin/python3
"""
markdown2html.py
A script to convert a Markdown file to an HTML file without using external
libraries.

Usage:
    ./markdown2html.py input_file.md output_file.html

Markdown Syntax Supported:
    - Headings: #, ##, ###, ####, #####, ######

"""

import sys
import os


def parse_markdown_line(line):
    """
    Parses a single line of Markdown and converts it to HTML.
    Supports only heading syntax (#).

    Args:
        line (str): A single line of Markdown.

    Returns:
        str: The converted HTML line, or the original line if no match.
    """
    if line.startswith("#"):
        heading_level = 0
        while heading_level < len(line) and line[heading_level] == "#":
            heading_level += 1

        if 1 <= heading_level <= 6:
            content = line[heading_level:].strip()
            return f"<h{heading_level}>{content}</h{heading_level}>"


    return line


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to an HTML file.

    Args:
        input_file (str): Path to the Markdown file.
        output_file (str): Path to the output HTML file.
    """
    with open(input_file, 'r', encoding='utf-8') as md_file:
        lines = md_file.readlines()

    with open(output_file, 'w', encoding='utf-8') as html_file:
        for line in lines:
            html_line = parse_markdown_line(line.strip())
            html_file.write(html_line + "\n")


def main():
    """
    Main entry point of the script.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
               file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)


    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)


if __name__ == "__main__":
    main()
