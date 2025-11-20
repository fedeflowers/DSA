(function() {
    const originalFetch = window.fetch;

    window.fetch = async function(...args) {
        const response = await originalFetch.apply(this, args);
        
        try {
            const url = args[0] ? args[0].toString() : '';
            
            // Check if this is a submission check URL
            // Pattern: https://leetcode.com/submissions/detail/<submission_id>/check/
            if (url.includes('/submissions/detail/') && url.includes('/check/')) {
                const clone = response.clone();
                clone.json().then(data => {
                    if (data.state === 'SUCCESS' && data.status_msg === 'Accepted') {
                        // We found a successful submission!
                        // We need to extract more details. The check/ endpoint gives some stats.
                        // But we might need the code. The code is usually in the submission page or sent in the submit request.
                        // However, capturing the submit request (POST) is harder because we need the payload.
                        // A better way might be to fetch the submission details using the submission ID we just found.
                        
                        const submissionId = url.split('/detail/')[1].split('/')[0];
                        
                        window.postMessage({
                            type: 'LEETCODE_SUBMISSION_SUCCESS',
                            payload: {
                                submissionId: submissionId,
                                stats: data,
                                url: window.location.href // Current problem URL
                            }
                        }, '*');
                    }
                }).catch(err => console.error('LeetCode Sync: Error parsing response', err));
            }
        } catch (e) {
            console.error('LeetCode Sync: Error in fetch interceptor', e);
        }

        return response;
    };
})();
