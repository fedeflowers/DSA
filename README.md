# Data Structures & Algorithms (DSA)

A curated collection of LeetCode solutions organized by topic, featuring clean Python implementations with detailed explanations and complexity analysis.

## 📚 About This Repository

This repository contains my solutions to various LeetCode problems, organized by algorithmic patterns and data structures. Each solution includes:
- Clean, well-commented Python code
- Problem description and approach
- Time and space complexity analysis
- Runtime and memory statistics from LeetCode

**Note**: This repository contains selected problems that I find particularly interesting or educational. For my complete LeetCode activity, check my [LeetCode profile](https://leetcode.com/u/FedericoFiorio/).

## 📂 Repository Structure

Solutions are organized into topic-based folders following the pattern `Topic/ProblemName.py`:

```
DSA/
├── Array/              # Array manipulation problems
├── Backtracking/       # Backtracking and recursion
├── Binary_Search/      # Binary search variants
├── Bit_Manipulation/   # Bitwise operations
├── Class/              # Object-oriented design problems
├── Dynamic_Programming/# DP optimization problems
├── Fenwick_Tree/       # Binary Indexed Tree
├── Graph/              # Graph algorithms (BFS, DFS, etc.)
├── Greedy/             # Greedy algorithms
├── Hash_Table/         # Hash-based solutions
├── Heap/               # Priority queue problems
├── Linked_Lists/       # Linked list operations
├── Math/               # Mathematical problems
├── Sliding_Window/     # Sliding window technique
├── Stack/              # Stack-based solutions
├── String/             # String manipulation
├── Tree/               # Binary tree problems
├── Trie/               # Prefix tree implementations
├── Two_Pointers/       # Two-pointer technique
├── Union_Find/         # Disjoint set union
└── LeetCode_Sync_Extension/  # Browser extension for auto-sync
```

## 🔄 LeetCode Sync Extension

### What It Does

The **LeetCode Sync Extension** is a Chrome/Edge browser extension that automatically syncs your accepted LeetCode submissions to this GitHub repository. When you successfully solve a problem on LeetCode, the extension:

1. **Detects** your accepted submission automatically
2. **Fetches** problem details and tags from LeetCode
3. **Generates** an AI-powered explanation and complexity analysis using OpenAI or Google Gemini
4. **Organizes** the solution into the appropriate topic folder
5. **Pushes** the code and explanation to your GitHub repository
6. **Notifies** you when the sync is complete

### How to Use the Extension

#### Installation

1. Navigate to the `LeetCode_Sync_Extension` folder in this repository
2. Open Chrome or Edge browser
3. Go to `chrome://extensions` (or `edge://extensions`)
4. Enable **Developer Mode** (toggle in top right corner)
5. Click **Load unpacked**
6. Select the `LeetCode_Sync_Extension` folder

#### Configuration

1. Click the extension icon in your browser toolbar
2. Configure the following settings:
   - **GitHub Personal Access Token**: Create a token with `repo` scope at [GitHub Settings](https://github.com/settings/tokens)
   - **Target Repository**: Enter your repository name (e.g., `fedeflowers/DSA`)
   - **LLM Provider**: Choose between OpenAI or Google Gemini
   - **API Key**: Enter your API key for the selected LLM provider
3. Click **Save Settings**

#### Usage

Once configured, the extension works automatically:

1. Solve problems on [LeetCode](https://leetcode.com)
2. Submit your solution
3. When you see the "Accepted" message, the extension automatically syncs
4. Receive a browser notification confirming the sync
5. Your solution appears in the appropriate folder in this repository

#### Troubleshooting

- **Sync Failed**: Check the browser console (right-click extension icon → Inspect) for error details
- **No Notification**: Ensure browser notifications are enabled
- **Wrong Folder**: The extension uses LeetCode's primary tag to determine the folder

## 🛠️ Technologies

- **Language**: Python 3.x
- **Extension**: JavaScript (Manifest V3)
- **AI Integration**: OpenAI GPT / Google Gemini
- **Version Control**: Git & GitHub

## 📈 Progress

Check my [LeetCode profile](https://leetcode.com/u/FedericoFiorio/) for my current stats and progress.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
