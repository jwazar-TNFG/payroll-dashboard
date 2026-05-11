import re

# Read current file
with open('index.html', 'r') as f:
    content = f.read()

# 1. Update the Categories card to be larger and scrollable
old_cat_card = '''<!-- Categories -->
        <div class="card">
            <div class="card-title">Payroll Categories</div>
            <div class="card-subtitle">Breakdown by type</div>
            <div id="categoryChart"></div>
        </div>'''

new_cat_card = '''<!-- Categories -->
        <div class="card span-2" style="max-height: 500px;">
            <div class="card-title">Payroll Categories</div>
            <div class="card-subtitle">All categories from system</div>
            <div id="categoryChart" style="max-height: 420px; overflow-y: auto;"></div>
        </div>'''

content = content.replace(old_cat_card, new_cat_card)

# 2. Update the category bar styling for compactness
old_cat_bar = '''.category-bar {
            display: flex;
            align-items: center;
            margin: 10px 0;
        }'''

new_cat_bar = '''.category-bar {
            display: flex;
            align-items: center;
            margin: 6px 0;
            padding: 4px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .category-bar:last-child { border-bottom: none; }'''

content = content.replace(old_cat_bar, new_cat_bar)

# Update timestamp
import datetime
now = datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p ET')
content = re.sub(r'Last updated: [^<]+', f'Last updated: {now}', content)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated categories section")
