import os
import shutil

BASE_DIR = r"c:\Users\f.fiorio\Documents\Github\DSA"
ARRAY_DIR = os.path.join(BASE_DIR, "Array")

# List of subfolders to remove (relative to Array)
SUBFOLDERS_TO_REMOVE = [
    "BFS",
    "BIT",
    "Binary Search",
    "Combinatorics",
    "Dynamic programming",
    "Generic",
    "Greedy",
    "Hash table",
    "Heapq",
    "Math",
    "Prefix sum",
    "Prefix_suffix",
    "Sliding Window",
    "Stack",
    "String", # This contains subfolders too, need to be careful or recursive
    "Union find"
]

def cleanup():
    for sub in SUBFOLDERS_TO_REMOVE:
        path = os.path.join(ARRAY_DIR, sub)
        if os.path.exists(path):
            print(f"Removing {path}...")
            try:
                shutil.rmtree(path)
                print("  Done.")
            except Exception as e:
                print(f"  Failed: {e}")
        else:
            print(f"Skipping {path} (not found)")

if __name__ == "__main__":
    cleanup()
