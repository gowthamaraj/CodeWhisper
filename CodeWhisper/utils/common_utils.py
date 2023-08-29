import requests

def get_content(url):
    try:
        response = requests.get(url, timeout=5, verify=False)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return ""
