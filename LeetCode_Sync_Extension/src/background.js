import { getSubmissionDetails, getProblemTags, getLeetCodeUsername, getLastAcceptedSubmission } from './leetcode_client.js';
import { generateExplanation } from './llm_client.js';
import { syncToGitHub } from './github_client.js';

// Simple 1x1 transparent PNG as data URI for notifications
const ICON_DATA_URI = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==';

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'SUBMISSION_DETECTED') {
        handleSubmission(message.payload);
    } else if (message.type === 'MANUAL_SYNC_LAST') {
        handleManualSync();
        sendResponse({ status: 'started' });
    }
    // Return true if we were to await something before sending response, 
    // but here we sendResponse immediately for the ack, so we don't strictly need to return true 
    // unless we want to keep the channel open. 
    // However, handleManualSync is async and we are NOT awaiting it for the response.
});

async function handleManualSync() {
    try {
        console.log('Starting manual sync...');
        const username = await getLeetCodeUsername();
        if (!username) throw new Error('Could not retrieve LeetCode username. Are you logged in?');

        const lastSubmission = await getLastAcceptedSubmission(username);
        if (!lastSubmission) throw new Error('No accepted submissions found.');

        await handleSubmission({
            submissionId: lastSubmission.id,
            stats: { runtime: 'N/A', memory: 'N/A' },
            url: `https://leetcode.com/problems/${lastSubmission.titleSlug}/`
        });

    } catch (error) {
        console.error('Manual sync failed:', error);
        chrome.notifications.create({
            type: 'basic',
            iconUrl: ICON_DATA_URI,
            title: 'Manual Sync Failed',
            message: error.message || 'Unknown error'
        });
    }
}

async function handleSubmission(payload) {
    const { submissionId, stats, url } = payload;
    console.log(`Processing submission ${submissionId} for ${url}`);

    try {
        // 1. Get Settings
        const settings = await chrome.storage.local.get(['githubToken', 'repoName', 'llmProvider', 'llmApiKey']);
        if (!settings.githubToken || !settings.llmApiKey) {
            console.error('Missing API keys');
            chrome.notifications.create({
                type: 'basic',
                iconUrl: ICON_DATA_URI,
                title: 'LeetCode Sync Error',
                message: 'Missing API Keys. Please configure the extension.'
            });
            return;
        }

        // 2. Fetch Submission Code & Details
        const submissionData = await getSubmissionDetails(submissionId);
        const code = submissionData.code;
        const lang = submissionData.lang.name;
        const questionTitle = submissionData.question.title;
        const questionSlug = submissionData.question.titleSlug;

        // 3. Fetch Problem Tags
        const tags = await getProblemTags(questionSlug);
        
        // 4. Generate Explanation
        const explanation = await generateExplanation(
            code, 
            questionTitle, 
            stats, 
            settings.llmProvider, 
            settings.llmApiKey
        );

        // 5. Sync to GitHub
        await syncToGitHub(
            settings.githubToken,
            settings.repoName,
            {
                code,
                lang,
                tags,
                title: questionTitle,
                explanation,
                stats
            }
        );

        console.log('Sync complete!');
        chrome.notifications.create({
            type: 'basic',
            iconUrl: ICON_DATA_URI,
            title: 'LeetCode Sync Success',
            message: `Synced ${questionTitle} to GitHub!`
        });

    } catch (error) {
        console.error('Sync failed:', error);
        chrome.notifications.create({
            type: 'basic',
            iconUrl: ICON_DATA_URI,
            title: 'LeetCode Sync Failed',
            message: error.message || 'Unknown error occurred'
        });
    }
}
