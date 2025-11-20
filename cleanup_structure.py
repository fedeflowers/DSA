import os
import shutil

BASE_DIR = r"c:\Users\f.fiorio\Documents\Github\DSA"

MOVES = {
    "Graphs_and_BFSDFS": "Graph",
    "Trees_and_Binary_Trees": "Tree",
    "Arrays_and_Strings": "Array",
    "Greedy_Algorithms": "Greedy",
    "Hash_Maps_and_Sets": "Hash_Table",
    "Stacks_and_Queues": "Stack",
    "Two_Pointers_and_Sliding_Window": "Two_Pointers",
    "Dynamic_Programming": "Dynamic_Programming", # Keep as is, but ensure consistent casing if needed
    "Linked_Lists": "Linked_Lists" # Keep as is
}

def cleanup_structure():
    for src_name, dst_name in MOVES.items():
        src_path = os.path.join(BASE_DIR, src_name)
        dst_path = os.path.join(BASE_DIR, dst_name)
        
        if os.path.exists(src_path):
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
                print(f"Created {dst_path}")
            
            # Move files
            for item in os.listdir(src_path):
                s = os.path.join(src_path, item)
                d = os.path.join(dst_path, item)
                if os.path.isfile(s):
                    shutil.move(s, d)
                    print(f"Moved {item} to {dst_name}")
                elif os.path.isdir(s):
                    # If it's a directory, move it inside (or merge if exists)
                    # For simplicity, just move the dir
                    if not os.path.exists(d):
                        shutil.move(s, d)
                        print(f"Moved directory {item} to {dst_name}")
                    else:
                        print(f"Directory {item} already exists in {dst_name}, skipping move of directory itself (content merge not implemented for subdirs)")

            # Remove source dir if empty
            if not os.listdir(src_path):
                os.rmdir(src_path)
                print(f"Removed empty directory {src_name}")
            else:
                print(f"Directory {src_name} not empty, could not remove")

if __name__ == "__main__":
    cleanup_structure()
