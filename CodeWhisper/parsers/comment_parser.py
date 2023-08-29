import re

def extract_js_comments(content):
    pattern = r'//.*?$|/\*.*?\*/'
    return re.findall(pattern, content, re.DOTALL | re.MULTILINE)

def extract_html_comments(content):
    pattern = r'<!--.*?-->'
    return re.findall(pattern, content, re.DOTALL | re.MULTILINE)