# LeetCode to GitHub Sync Extension

This Chrome/Edge extension automatically syncs your accepted LeetCode submissions to your GitHub repository, organized by topic, with an AI-generated explanation.

## Features
- **Automatic Sync**: Listens for successful submissions.
- **Smart Organization**: Categorizes problems into folders based on LeetCode tags (e.g., `Dynamic_Programming/Climbing_Stairs.py`).
- **AI Explanations**: Generates a brief explanation and complexity analysis using OpenAI or Google Gemini.
- **Stats**: Includes runtime and memory usage stats.

## Installation

1. **Download/Clone** this repository.
2. Open Chrome or Edge.
3. Navigate to `chrome://extensions`.
4. Enable **Developer Mode** (top right).
5. Click **Load unpacked**.
6. Select the `LeetCode_Sync_Extension` folder.

## Configuration

1. Click the extension icon in the browser toolbar.
2. Enter your **GitHub Personal Access Token**.
    - Scope required: `repo` (to read/write to your repository).
3. Enter your **Target Repository** (e.g., `fedeflowers/DSA`).
4. Select your **LLM Provider** (OpenAI or Gemini) and enter the **API Key**.
5. Click **Save Settings**.

## Usage

Just solve problems on LeetCode! When you see the "Accepted" message, the extension will automatically:
1. Fetch the problem details and tags.
2. Generate an explanation.
3. Push the code and explanation to your GitHub repo.
4. You will receive a browser notification upon success.

## Troubleshooting

- **Sync Failed**: Check the browser console (Inspect the background page/service worker) for error details.
- **No Notification**: Ensure notifications are enabled for the browser.
