// Inject the interceptor script into the main page context
const script = document.createElement('script');
script.src = chrome.runtime.getURL('src/injected_interceptor.js');
script.onload = function() {
    this.remove();
};
(document.head || document.documentElement).appendChild(script);

// Listen for messages from the injected script
window.addEventListener('message', (event) => {
    // We only accept messages from ourselves
    if (event.source !== window) return;

    if (event.data.type && event.data.type === 'LEETCODE_SUBMISSION_SUCCESS') {
        console.log('LeetCode Sync: Received successful submission data');
        
        // Forward to background script
        chrome.runtime.sendMessage({
            type: 'SUBMISSION_DETECTED',
            payload: event.data.payload
        });
    }
});
