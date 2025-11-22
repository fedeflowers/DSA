(function () {
    const originalFetch = window.fetch;

    window.fetch = async function (...args) {
        const response = await originalFetch.apply(this, args);

        try {
            const url = args[0] ? args[0].toString() : '';

            // Check if this is a submission check URL
            // Pattern: https://leetcode.com/submissions/detail/<submission_id>/check/
            if (url.includes('/submissions/detail/') && url.includes('/check/')) {
                const clone = response.clone();
                clone.json().then(data => {
                    // Check if it's a real submission (has percentile data)
                    // "Run Code" also returns state: 'SUCCESS' and status_msg: 'Accepted'
                    // but usually lacks the percentile info that a real submission has.
                    const isSubmission = data.state === 'SUCCESS' &&
                        data.status_msg === 'Accepted' &&
                        (data.runtime_percentile !== undefined || data.memory_percentile !== undefined);

                    if (isSubmission) {
                        // Extract submission ID safely
                        const match = url.match(/\/submissions\/detail\/(\d+)\//);
                        const submissionId = match ? match[1] : null;

                        if (!submissionId) {
                            console.error('LeetCode Sync: Could not extract submission ID from URL', url);
                            return;
                        }

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
