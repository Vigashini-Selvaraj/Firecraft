import json
import re

transcript_path = r'C:\Users\vigas\.gemini\antigravity-ide\brain\615a134f-4adf-4906-b4e9-68665cc0fba7\.system_generated\logs\transcript_full.jsonl'
lines = []
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        lines.append(line)

print("Processing transcript for diff block...")
target_css = ''
for line in reversed(lines):
    data = json.loads(line)
    if data.get('type') == 'USER_INPUT':
        content = data.get('content', '').replace('\r\n', '\n')
        if 'FIREBORN HOME 2' in content:
            # Try to extract it
            blocks = re.findall(r'\[diff_block_start\]\n@@.*?@@\n(.*?)\[diff_block_end\]', content, re.DOTALL)
            for diff_text in blocks:
                if 'FIREBORN HOME 2' in diff_text:
                    diff_lines = diff_text.split('\n')
                    cleaned = [l[1:] if l.startswith('-') else l for l in diff_lines]
                    target_css = '\n'.join(cleaned)
                    break
        if target_css:
            break

if target_css:
    with open(r'c:\Users\vigas\Desktop\firecraft\css\home2.css', 'w', encoding='utf-8') as out:
        out.write(target_css.strip())
    print("SUCCESS")
else:
    print("FAILED")
