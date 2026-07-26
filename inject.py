import re

with open('index.html', 'r') as f:
    html = f.read()

with open('new_sections.html', 'r') as f:
    new_content = f.read()

# Replace the old features section with all the new sections
pattern = re.compile(r'<section id="features" class="features-grid-section section">.*?</section>', re.DOTALL)
html = pattern.sub(new_content, html)

with open('index.html', 'w') as f:
    f.write(html)
