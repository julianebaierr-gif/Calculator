import os
import re

tools = [
    "a1c-calculator.html",
    "bac-calculator.html",
    "body-surface-area-calculator.html",
    "bsa-calculator.html",
    "calorie-deficit-calculator.html",
    "calories-burned-calculator.html",
    "carbohydrate-intake-calculator.html",
    "cholesterol-ratio-calculator.html"
]

print("=== VERIFYING BATCH 21 WORD COUNTS (> 1,000 words) ===")
all_pass = True
for tool in tools:
    if not os.path.exists(tool):
        print(f"FAILED: {tool} does not exist!")
        all_pass = False
        continue
    with open(tool, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Extract article-body
    match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
    if not match:
        print(f"FAILED: {tool} missing article-body!")
        all_pass = False
        continue
    
    body = match.group(1)
    # Strip HTML tags
    text = re.sub(r'<[^>]+>', ' ', body)
    # Strip KaTeX math blocks
    text = re.sub(r'\$\$.*?\$\$', ' ', text, flags=re.DOTALL)
    text = re.sub(r'\\\(.*?\\\)', ' ', text)
    words = text.split()
    word_count = len(words)
    status = "PASS" if word_count >= 1000 else "FAIL (< 1,000 words)"
    if word_count < 1000:
        all_pass = False
    print(f"{tool}: {word_count} words -> {status}")

print("======================================================")
if all_pass:
    print("SUCCESS: All 8 Batch 21 tools strictly exceed 1,000 words in article-body!")
else:
    print("WARNING: Some tools did not meet the 1,000 word threshold.")
