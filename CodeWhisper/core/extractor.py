from CodeWhisper.parsers import url_parser, comment_parser
from CodeWhisper.utils import common_utils

def extract_comments_from_feroxbuster_output(output_text):
    urls = url_parser.extract_urls(output_text)
    js_comments = []
    html_comments = []

    for url in urls:
        if url.endswith('.js'):
            content = common_utils.get_content(url)
            comments = comment_parser.extract_js_comments(content)
            js_comments.extend(comments)
        elif url.endswith('.html') or url in ['.php', '.aspx', '.jsp']:  # Adding other potential HTML file extensions
            content = common_utils.get_content(url)
            comments = comment_parser.extract_html_comments(content)
            html_comments.extend(comments)

    return js_comments, html_comments
