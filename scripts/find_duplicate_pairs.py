import glob
import re
from collections import Counter

html_files = glob.glob('*.html')
slugs = [f.replace('.html', '') for f in html_files]

pairs = []
for i, s1 in enumerate(slugs):
    words1 = set(s1.split('-'))
    for s2 in slugs[i+1:]:
        words2 = set(s2.split('-'))
        # Jaccard similarity of slug words
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        sim = len(intersection) / len(union)
        
        # If words are almost identical (e.g. subset or 80%+ overlap)
        if sim >= 0.75 and len(union) >= 3:
            pairs.append((s1, s2, sim))

print(f"High similarity slug pairs (>=75% keyword overlap): {len(pairs)}")
for s1, s2, sim in sorted(pairs, key=lambda x: -x[2]):
    print(f"  {s1} <--> {s2} (sim: {sim:.2f})")
