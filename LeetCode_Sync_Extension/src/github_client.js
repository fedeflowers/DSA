const GITHUB_API_BASE = 'https://api.github.com';

export async function syncToGitHub(token, repo, data) {
    const { code, lang, tags, title, explanation, stats } = data;

    // Determine path: Primary Tag / ProblemTitle.ext
    // We use the first tag as the folder
    const folder = tags.length > 0 ? tags[0].replace(/\s+/g, '_') : 'Uncategorized';
    const filename = toCamelCase(title) + getExtension(lang);
    const path = `${folder}/${filename}`;

    // We also want to save the explanation. Maybe as a comment in the code or a separate MD file?
    // User requested: "push the code that ive submitted with an explanation of the exercise"
    // Let's append the explanation as a comment block at the top of the file.

    const content = formatContent(code, explanation, stats, lang);

    await createOrUpdateFile(token, repo, path, content, `Add solution for ${title}`);
}

function getExtension(lang) {
    const map = {
        'python': '.py',
        'python3': '.py',
        'java': '.java',
        'cpp': '.cpp',
        'javascript': '.js',
        'typescript': '.ts',
        'golang': '.go',
        'ruby': '.rb',
        'swift': '.swift',
        'kotlin': '.kt',
        'scala': '.scala',
        'rust': '.rs',
        'csharp': '.cs'
    };
    return map[lang.toLowerCase()] || '.txt';
}

function formatContent(code, explanation, stats, lang) {
    const commentStart = lang.includes('python') || lang.includes('ruby') ? '"""' : '/*';
    const commentEnd = lang.includes('python') || lang.includes('ruby') ? '"""' : '*/';

    return `${commentStart}
${explanation}

Runtime: ${stats.runtime}
Memory: ${stats.memory}
${commentEnd}

${code}
`;
}

async function createOrUpdateFile(token, repo, path, content, message) {
    // 1. Get current file SHA (if exists) to update
    let sha = null;
    try {
        const response = await fetch(`${GITHUB_API_BASE}/repos/${repo}/contents/${path}`, {
            headers: {
                'Authorization': `token ${token}`,
                'Accept': 'application/vnd.github.v3+json'
            }
        });
        if (response.ok) {
            const data = await response.json();
            sha = data.sha;
        }
    } catch (e) {
        // File doesn't exist, ignore
    }

    // 2. Create/Update file
    const body = {
        message: message,
        content: btoa(unescape(encodeURIComponent(content))), // Base64 encode handling unicode
        branch: 'main' // Assuming main branch
    };

    if (sha) {
        body.sha = sha;
    }

    const response = await fetch(`${GITHUB_API_BASE}/repos/${repo}/contents/${path}`, {
        method: 'PUT',
        headers: {
            'Authorization': `token ${token}`,
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    });

    if (!response.ok) {
        const err = await response.json();
        throw new Error(`GitHub API Error: ${err.message}`);
    }
}

function toCamelCase(str) {
    return str.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase());
}
