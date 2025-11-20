document.addEventListener('DOMContentLoaded', () => {
    // Load saved settings
    chrome.storage.local.get(['githubToken', 'repoName', 'llmProvider', 'llmApiKey'], (result) => {
        if (result.githubToken) document.getElementById('githubToken').value = result.githubToken;
        if (result.repoName) document.getElementById('repoName').value = result.repoName;
        if (result.llmProvider) document.getElementById('llmProvider').value = result.llmProvider;
        if (result.llmApiKey) document.getElementById('llmApiKey').value = result.llmApiKey;
    });

    // Save settings
    document.getElementById('saveBtn').addEventListener('click', () => {
        const githubToken = document.getElementById('githubToken').value;
        const repoName = document.getElementById('repoName').value;
        const llmProvider = document.getElementById('llmProvider').value;
        const llmApiKey = document.getElementById('llmApiKey').value;

        chrome.storage.local.set({
            githubToken,
            repoName,
            llmProvider,
            llmApiKey
        }, () => {
            const status = document.getElementById('status');
            status.textContent = 'Settings saved!';
            setTimeout(() => {
                status.textContent = '';
            }, 2000);
        });
    });

    // Manual Sync
    document.getElementById('syncLastBtn').addEventListener('click', () => {
        const status = document.getElementById('status');
        status.textContent = 'Syncing...';
        status.style.color = '#007bff';

        chrome.runtime.sendMessage({ type: 'MANUAL_SYNC_LAST' }, (response) => {
            if (chrome.runtime.lastError) {
                status.textContent = 'Error: ' + chrome.runtime.lastError.message;
                status.style.color = 'red';
            } else {
                // The background script will handle the notification
                status.textContent = 'Sync started. Check notifications.';
            }
        });
    });
});
