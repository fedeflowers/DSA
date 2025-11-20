import json
import os
import re

NOTEBOOK_PATH = r"c:\Users\f.fiorio\Documents\Github\DSA\leetcode_patterns_DE_studies.ipynb"
BASE_DIR = r"c:\Users\f.fiorio\Documents\Github\DSA"

def sanitize_filename(name):
    # Remove invalid characters and spaces
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip().replace(' ', '_')
    return name

def extract_code_from_notebook():
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    current_topic = "Uncategorized"
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            lines = source.split('\n')
            
            for i, line in enumerate(lines):
                # Check for Topic Header (## )
                if line.strip().startswith('## ') and not line.strip().startswith('###'):
                    # Extract topic name, remove emojis and extra chars
                    topic_match = re.search(r'##\s*(?:🔹)?\s*(.*)', line)
                    if topic_match:
                        raw_topic = topic_match.group(1).strip()
                        # Remove "Amazon Medium Coding Interview Questions" header or similar if it's not a real topic
                        if "Amazon Medium" in raw_topic or "Key Topics" in raw_topic:
                            continue
                        current_topic = sanitize_filename(raw_topic)
                        print(f"Found Topic: {current_topic}")
                
                # Check for Problem Header (### 🔗 [Name](Link))
                elif line.strip().startswith('### 🔗'):
                    # Extract problem name and link
                    problem_match = re.search(r'\[(.*?)\]\((.*?)\)', line)
                    if problem_match:
                        problem_name = problem_match.group(1)
                        problem_link = problem_match.group(2)
                        safe_problem_name = sanitize_filename(problem_name)
                        
                        # Look for code block in the following lines
                        code_content = []
                        in_code_block = False
                        lang = ""
                        
                        # Scan remaining lines in this cell for the code block
                        # This assumes the code is in the SAME markdown cell as the header
                        for j in range(i + 1, len(lines)):
                            subline = lines[j]
                            if subline.strip().startswith('```'):
                                if in_code_block:
                                    in_code_block = False
                                    break # End of code block
                                else:
                                    in_code_block = True
                                    lang = subline.strip().replace('```', '')
                                    continue
                            
                            if in_code_block:
                                code_content.append(subline)
                        
                        if code_content:
                            # Create directory
                            topic_dir = os.path.join(BASE_DIR, current_topic)
                            os.makedirs(topic_dir, exist_ok=True)
                            
                            file_path = os.path.join(topic_dir, f"{safe_problem_name}.py")
                            
                            # Prepare file content
                            file_content = f"# Problem: {problem_name}\n"
                            file_content += f"# Link: {problem_link}\n\n"
                            file_content += "\n".join(code_content)
                            
                            # Write file
                            with open(file_path, 'w', encoding='utf-8') as out_f:
                                out_f.write(file_content)
                            
                            print(f"Created: {file_path}")

if __name__ == "__main__":
    extract_code_from_notebook()
