const LEETCODE_GRAPHQL_URL = 'https://leetcode.com/graphql';

export async function getSubmissionDetails(submissionId) {
    const query = `
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            lang {
                name
            }
            question {
                title
                titleSlug
                content
            }
        }
    }
    `;

    const response = await fetch(LEETCODE_GRAPHQL_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query,
            variables: { submissionId: parseInt(submissionId, 10) }
        })
    });

    const data = await response.json();
    if (data.errors) {
        throw new Error('Failed to fetch submission details: ' + data.errors[0].message);
    }
    return data.data.submissionDetails;
}

export async function getProblemTags(titleSlug) {
    const query = `
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            topicTags {
                name
                slug
            }
        }
    }
    `;

    const response = await fetch(LEETCODE_GRAPHQL_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query,
            variables: { titleSlug }
        })
    });

    const data = await response.json();
    if (data.errors) {
        throw new Error('Failed to fetch tags: ' + data.errors[0].message);
    }
    if (!data.data || !data.data.question) {
        console.warn('LeetCode Sync: No question data found for slug:', titleSlug);
        return [];
    }
    return data.data.question.topicTags.map(tag => tag.name);
}

export async function getLeetCodeUsername() {
    const query = `
    query globalData {
        userStatus {
            username
            isSignedIn
        }
    }
    `;

    const response = await fetch(LEETCODE_GRAPHQL_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
    });

    const data = await response.json();
    if (data.data && data.data.userStatus && data.data.userStatus.isSignedIn) {
        return data.data.userStatus.username;
    }
    return null;
}

export async function getLastAcceptedSubmission(username) {
    const query = `
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            id
            title
            titleSlug
            timestamp
        }
    }
    `;

    const response = await fetch(LEETCODE_GRAPHQL_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            query,
            variables: { username, limit: 1 }
        })
    });

    const data = await response.json();
    if (data.data && data.data.recentAcSubmissionList && data.data.recentAcSubmissionList.length > 0) {
        return data.data.recentAcSubmissionList[0];
    }
    return null;
}
