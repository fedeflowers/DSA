import json
import os
import re

BASE_DIR = r"c:\Users\f.fiorio\Documents\Github\DSA"
ARRAY_DIR = os.path.join(BASE_DIR, "Array")

# Mapping: Source Notebook Relative Path -> Target Folder Name
MAPPING = {
    r"BFS\bfs array.ipynb": "Graph",
    r"BIT\BIT.ipynb": "Fenwick_Tree",
    r"Binary Search\Binary Search.ipynb": "Binary_Search",
    r"Combinatorics\Combinatorics.ipynb": "Math",
    r"Dynamic programming\Dynamic programming.ipynb": "Dynamic_Programming",
    r"Generic\Generic algs.ipynb": "Array",
    r"Greedy\Greedy.ipynb": "Greedy",
    r"Hash table\hash_table.ipynb": "Hash_Table",
    r"Heapq\heapq.ipynb": "Heap",
    r"Math\Math.ipynb": "Math",
    r"Prefix sum\prefix sum_difference arr.ipynb": "Array",
    r"Prefix_suffix\Prefix_Suffix.ipynb": "Array",
    r"Sliding Window\Sliding Window.ipynb": "Sliding_Window",
    r"Stack\Stack.ipynb": "Stack",
    r"String\BFS\BFS.ipynb": "Graph",
    r"String\Backtracking\Backtracking.ipynb": "Backtracking",
    r"String\General\String.ipynb": "String",
    r"String\Sliding window\Sliding Window.ipynb": "Sliding_Window",
    r"Union find\Union find.ipynb": "Union_Find"
}

def sanitize_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip().replace(' ', '_')
    return name

def extract_from_notebook(notebook_rel_path, target_folder):
    notebook_path = os.path.join(ARRAY_DIR, notebook_rel_path)
    if not os.path.exists(notebook_path):
        print(f"Skipping missing notebook: {notebook_path}")
        return

    print(f"Processing {notebook_rel_path} -> {target_folder}")
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"Error reading {notebook_path}: {e}")
        return

    target_dir = os.path.join(BASE_DIR, target_folder)
    os.makedirs(target_dir, exist_ok=True)

    current_problem_name = "Unknown_Problem"
    
    for i, cell in enumerate(nb['cells']):
        # Try to find problem name in markdown cells
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            # Look for headers like "## Problem Name" or "### Problem Name"
            # Or links like "[Problem Name](url)"
            
            # Heuristic 1: Link with name
            match = re.search(r'\[(.*?)\]\(.*leetcode\.com.*\)', source, re.IGNORECASE)
            if match:
                current_problem_name = sanitize_filename(match.group(1))
                continue
            
            # Heuristic 2: Header
            lines = source.split('\n')
            for line in lines:
                if line.strip().startswith('#'):
                    # Remove # and extra chars
                    clean_line = line.lstrip('#').strip()
                    if len(clean_line) > 3 and "http" not in clean_line:
                        current_problem_name = sanitize_filename(clean_line)
                        break

        # Extract code from code cells
        elif cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if not source.strip():
                continue
                
            # Heuristic: If code contains "class Solution", it's likely a solution
            if "class Solution" in source:
                # Use current_problem_name
                # If filename exists, append a number
                filename = f"{current_problem_name}.py"
                file_path = os.path.join(target_dir, filename)
                
                counter = 1
                while os.path.exists(file_path):
                    filename = f"{current_problem_name}_{counter}.py"
                    file_path = os.path.join(target_dir, filename)
                    counter += 1
                
                with open(file_path, 'w', encoding='utf-8') as out_f:
                    out_f.write(source)
                try:
                    print(f"  Extracted: {filename}")
                except UnicodeEncodeError:
                    print(f"  Extracted: {filename.encode('ascii', 'replace').decode()}")
                
                # Reset problem name to avoid reusing it for unrelated code blocks
                # But keep it if the next cell is just a continuation (unlikely for separate problems)
                # current_problem_name = "Unknown_Problem" 

if __name__ == "__main__":
    for nb_path, target in MAPPING.items():
        extract_from_notebook(nb_path, target)
