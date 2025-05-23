import os
import re
import bleach

CONTENT_MD = os.path.join(os.path.dirname(__file__), '../content/content.md')
TEMPLATE_HTML = os.path.join(os.path.dirname(__file__), '../templates/index.html')
OUTPUT_HTML = TEMPLATE_HTML  # Overwrite index.html directly (backup recommended for prod)

# Allowed HTML tags for sanitized output
ALLOWED_TAGS = ['b', 'i', 'em', 'strong', 'a', 'ul', 'ol', 'li', 'p', 'br', 'span', 'h3', 'h4']
ALLOWED_ATTRS = {'a': ['href', 'target', 'rel'], 'span': ['class'], 'h3': ['class'], 'h4': ['class']}

def parse_content_md(md_text):
    """
    Enhanced parser for content.md that supports clusters, components, and reinforcement questions in the format:
    **Q:** ...\n**Choices:**\n* A) ...\n* B) ...\n* C) ...\n* D) ...\n**Correct:** X
    """
    clusters = []
    cluster = None
    component_re = re.compile(r'^- (.+)')
    # Match both '## Cluster: Title' and '### Cluster: Title', and capture the title (must not be empty)
    cluster_re = re.compile(r'^##+ Cluster: (.+)$')
    component_header_re = re.compile(r'^## Component: (.+)')
    question_start_re = re.compile(r'^(\*\*Q:\*\*|Q:)\s*(.+)')
    # Allow optional leading '+' for Choices
    choices_header_re = re.compile(r'^(\+)?\*\*Choices:\*\*')
    choice_re = re.compile(r'^[\+\*]?\s*([A-D])\)\s*(.+)')
    # Allow optional leading '+' for Correct
    correct_re = re.compile(r'^\+?(?:\*\*Correct:\*\*|Correct:)\s*:?\s*([A-D])')
    lines = md_text.splitlines()
    # Only process lines between TRAINING-CONTENT-START and TRAINING-CONTENT-END markers
    start_idx = None
    end_idx = None
    for idx, line in enumerate(lines):
        if '<!-- TRAINING-CONTENT-START -->' in line:
            start_idx = idx + 1
        if '<!-- TRAINING-CONTENT-END -->' in line:
            end_idx = idx
            break
    if start_idx is not None and end_idx is not None and start_idx < end_idx:
        lines = lines[start_idx:end_idx]
    else:
        lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        cluster_match = cluster_re.match(line)
        if cluster_match:
            if cluster:
                clusters.append(cluster)
            cluster = {'title': cluster_match.group(1), 'components': [], 'body': [], 'questions': []}
        elif component_re.match(line):
            component = component_re.match(line).group(1)
            if cluster is not None:
                cluster['components'].append(component)
            else:
                print(f"Warning: component '{component}' found before any cluster header; skipping.")
        elif component_header_re.match(line):
            # skip component header, handled by next lines
            pass
        elif question_start_re.match(line):
            # Parse a full question block
            q_match = question_start_re.match(line)
            q_text = q_match.group(2).strip()
            choices = []
            correct = None
            explanation_lines = []
            # Look ahead for choices, correct, and explanations
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if choices_header_re.match(next_line):
                    j += 1
                    while j < len(lines):
                        c_line = lines[j].strip()
                        c_match = choice_re.match(c_line)
                        if c_match:
                            choices.append({'label': c_match.group(1), 'text': c_match.group(2)})
                            j += 1
                        else:
                            break
                elif correct_re.match(next_line):
                    correct_match = correct_re.match(next_line)
                    if correct_match and correct_match.group(1):
                        correct = correct_match.group(1)
                    j += 1
                elif (question_start_re.match(next_line) or cluster_re.match(next_line) or component_re.match(next_line) or component_header_re.match(next_line)):
                    break
                elif next_line:
                    explanation_lines.append(next_line)
                    j += 1
                else:
                    j += 1
            cluster['questions'].append({'q': q_text, 'choices': choices, 'correct': correct, 'explanation': '\n'.join(explanation_lines) if explanation_lines else None})
            i = j - 1
        else:
            if cluster is not None:
                cluster['body'].append(line)
            else:
                print(f"Warning: body content '{line}' found before any cluster header; skipping.")
        i += 1
    if cluster:
        clusters.append(cluster)
    return clusters

def sanitize_html(text):
    return bleach.clean(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS)

def generate_training_html(clusters):
    html = []
    first_question_generated_overall = True  # Flag for the very first question
    for idx, cluster in enumerate(clusters, 1):
        section_id = f"cluster-{idx}"
        html.append(f'<div class="mb-6">')
        html.append(f'<h3 class="text-xl font-semibold training-heading mb-2 collapsible-heading cursor-pointer flex justify-between items-center text-emerald-700" id="{section_id}">')
        html.append(f'<span class="flex items-center"><span class="checkbox mr-2 text-emerald-700">☐</span><span>{sanitize_html(cluster["title"])}</span></span>')
        html.append('</h3>')
        html.append('<div class="collapsible-content hidden ml-4 pl-4 border-l-2 border-emerald-200 text-gray-600">')
        html.append('<ul class="list-disc ml-8 space-y-1">')
        for comp in cluster['components']:
            html.append(f'<li>{sanitize_html(comp)}</li>')
        html.append('</ul>')
        if cluster['body']:
            html.append('<div class="cluster-body mb-4">')
            for line in cluster['body']:
                if line.startswith('* '):
                    html.append('<ul class="list-disc ml-8 space-y-1">')
                    while line.startswith('* '):
                        html.append(f'<li>{sanitize_html(line[2:])}</li>')
                        i = cluster['body'].index(line)
                        cluster['body'].pop(i)
                        if i >= len(cluster['body']):
                            break
                        line = cluster['body'][i]
                    html.append('</ul>')
                else:
                    html.append(f'<p>{sanitize_html(line)}</p>')
            html.append('</div>')
        if cluster['questions']:
            html.append('<button class="toggle-questions-btn mt-4 px-3 py-1 bg-gray-200 text-gray-700 rounded hover:bg-gray-300 text-sm">Show Questions</button>')
            html.append('<div class="question-area hidden mt-2 pt-2 border-t border-gray-300">')
            for qidx, qa in enumerate(cluster['questions'], 1):
                if first_question_generated_overall:
                    html.append('<div class="mb-2" id="first-question-container">')
                    first_question_generated_overall = False
                else:
                    html.append('<div class="mb-2">')
                html.append(f'<div class="font-semibold">Q{qidx}: {sanitize_html(qa["q"])}</div>')
                html.append('<button class="show-answer-btn px-2 py-1 bg-emerald-100 rounded text-emerald-800 text-xs ml-2">Show/Hide Answer</button>')
                if "choices" in qa and qa["choices"]:
                    html.append('<div class="choices space-y-1 mb-2">')
                    for choice in qa["choices"]:
                        html.append(f'<label class="block"><input type="radio" class="quiz-answer mr-2" name="q{idx}_{qidx}" value="{choice["label"]}"> {choice["label"]}) {sanitize_html(choice["text"])} </label>')
                    html.append('</div>')
                if "correct" in qa and qa["correct"]:
                    html.append(f'<div class="answer hidden ml-4 mt-1 text-gray-700"><strong>Correct Answer:</strong> {sanitize_html(qa["correct"])}</div>')
                if "explanation" in qa and qa["explanation"]:
                    html.append(f'<div class="explanation ml-4 mt-1 text-gray-600">{sanitize_html(qa["explanation"]).replace("\n", "<br>")}</div>')
                html.append('</div>')
            html.append('</div>')
        html.append('</div>')
        html.append('</div>')
    return '\n'.join(html)

def inject_training_html(template_html, training_html):
    """
    Replace the training section content in index.html with generated training HTML.
    Assumes a marker <!-- TRAINING-CONTENT-START --> ... <!-- TRAINING-CONTENT-END -->
    """
    start_marker = '<!-- TRAINING-CONTENT-START -->'
    end_marker = '<!-- TRAINING-CONTENT-END -->'
    start = template_html.find(start_marker)
    end = template_html.find(end_marker)
    if start == -1 or end == -1:
        raise ValueError('Training content markers not found in index.html')
    before = template_html[:start + len(start_marker)]
    after = template_html[end:]
    return before + '\n' + training_html + '\n' + after

def main():
    with open(CONTENT_MD, encoding='utf-8') as f:
        md_text = f.read()
    clusters = parse_content_md(md_text)
    training_html = generate_training_html(clusters)
    with open(TEMPLATE_HTML, encoding='utf-8') as f:
        template_html = f.read()
    output_html = inject_training_html(template_html, training_html)
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(output_html)
    print('Training page updated successfully.')

if __name__ == '__main__':
    main()
