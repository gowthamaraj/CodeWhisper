from CodeWhisper.core import extractor
import json

if __name__ == "__main__":

    feroxbuster_output = ''
    with open("input.json", "r") as f:
        data = f.readlines()
        feroxbuster_output = [json.loads(entry.strip()) for entry in data]
    js_comments, html_comments = extractor.extract_comments_from_feroxbuster_output(feroxbuster_output)

    print("JS Comments:")
    print("\n".join(js_comments))

    print("\nHTML Comments:")
    print("\n".join(html_comments))
