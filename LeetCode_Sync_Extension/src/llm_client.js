export async function generateExplanation(code, title, stats, provider, apiKey) {
    const prompt = `
    Explain the following LeetCode solution for the problem "${title}".
    
    Code:
    \`\`\`
    ${code}
    \`\`\`
    
    Runtime: ${stats.runtime || 'N/A'}
    Memory: ${stats.memory || 'N/A'}
    
    Please provide:
    1. A brief explanation of the approach.
    2. Time and Space Complexity analysis.
    3. Why this approach is efficient.
    
    Output in Markdown format.
    `;

    if (provider === 'openai') {
        return await callOpenAI(apiKey, prompt);
    } else if (provider === 'gemini') {
        return await callGemini(apiKey, prompt);
    } else {
        throw new Error('Unknown LLM provider');
    }
}

async function callOpenAI(apiKey, prompt) {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: "gpt-4o-mini",
            messages: [{ role: "user", content: prompt }]
        })
    });

    const data = await response.json();
    if (data.error) throw new Error(data.error.message);
    return data.choices[0].message.content;
}

async function callGemini(apiKey, prompt) {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
    
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            contents: [{
                parts: [{ text: prompt }]
            }]
        })
    });

    const data = await response.json();
    if (data.error) throw new Error(data.error.message);
    return data.candidates[0].content.parts[0].text;
}
