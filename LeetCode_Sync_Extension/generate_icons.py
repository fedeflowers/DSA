import base64
import os

# Simple 16x16 Green Square PNG Base64
icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAF0lEQVR42mNk+M9Qz0AEYBx0wGg4gBEAPjMC/f4D5O4AAAAASUVORK5CYII="
icon_data = base64.b64decode(icon_base64)

icons_dir = r"c:\Users\f.fiorio\Documents\Github\DSA\LeetCode_Sync_Extension\icons"

if not os.path.exists(icons_dir):
    os.makedirs(icons_dir)

# Write to all required sizes (browser will scale them, this is just to satisfy manifest)
for name in ["icon16.png", "icon48.png", "icon128.png"]:
    path = os.path.join(icons_dir, name)
    with open(path, "wb") as f:
        f.write(icon_data)
    print(f"Created {path}")
