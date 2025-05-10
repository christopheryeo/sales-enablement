import os
import re

CONTENT_MD = os.path.join(os.path.dirname(__file__), '../content/content.md')
TEMPLATE_HTML = os.path.join(os.path.dirname(__file__), '../templates/index.html')

# Helper to extract all visible text from HTML (basic, for static content)
def extract_text_from_html(html):
    # Remove script/style
    html = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL)
    # Remove tags
    text = re.sub(r'<[^>]+>', '', html)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_training_text():
    with open(TEMPLATE_HTML, encoding='utf-8') as f:
        html = f.read()
    # Only check the training section (between markers)
    start_marker = '<!-- TRAINING-CONTENT-START -->'
    end_marker = '<!-- TRAINING-CONTENT-END -->'
    start = html.find(start_marker)
    end = html.find(end_marker)
    if start == -1 or end == -1:
        raise ValueError('Training content markers not found in index.html')
    training_html = html[start+len(start_marker):end]
    return extract_text_from_html(training_html)

def extract_md_text():
    with open(CONTENT_MD, encoding='utf-8') as f:
        md = f.read()
    # Remove markdown syntax for a fair comparison
    md = re.sub(r'^#+\s*', '', md, flags=re.MULTILINE) # headings
    md = re.sub(r'^-\s*', '', md, flags=re.MULTILINE) # bullets
    md = re.sub(r'\*\*|__|\*|_', '', md) # bold/italic
    md = re.sub(r'\s+', ' ', md)
    return md.strip()

def normalize(text):
    # Lowercase, remove punctuation, collapse whitespace
    text = text.lower()
    text = re.sub(r'[\.,:;\-\–\—\(\)\[\]\{\}\'\"\`]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def main():
    html_text = extract_training_text()
    md_text = extract_md_text()
    html_lines = [normalize(l) for l in html_text.split('\n') if l.strip()]
    md_lines = [normalize(l) for l in md_text.split('\n') if l.strip()]
    # Fuzzy comparison: consider a line present if any html line contains it as a substring
    missing = []
    for md_line in md_lines:
        if not md_line:
            continue
        found = False
        for html_line in html_lines:
            if md_line in html_line:
                found = True
                break
        if not found:
            missing.append(md_line)
    if missing:
        print('Inconsistencies found! The following content from content.md was not found in the training HTML:')
        for m in missing:
            print(f'- {m}')
        exit(1)
    else:
        print('All content from content.md is present in the training HTML.')

if __name__ == '__main__':
    main()
