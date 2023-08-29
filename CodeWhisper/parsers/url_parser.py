import re

def extract_urls(output_text):
    urls = [endpoint['url'] for endpoint in output_text if endpoint['type'] == 'response']
    return (urls)