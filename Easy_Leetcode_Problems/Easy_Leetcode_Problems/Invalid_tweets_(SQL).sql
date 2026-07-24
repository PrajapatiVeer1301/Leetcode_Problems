-- Logic:
--
-- 1. Read every tweet.
--
-- 2. Find the length of content.
--
-- 3. If length is greater than 15,
--    it is an invalid tweet.
--
-- 4. Return the tweet_id.

-- Algorithm:
--
-- 1. Select tweet_id.
--
-- 2. Calculate the length of content
--    using LENGTH().
--
-- 3. Check:
--      LENGTH(content) > 15
--
-- 4. Return the matching tweet IDs.

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;

-- Interview Explanation:
--
-- 1. I selected the tweet IDs
--    from the Tweets table.
--
-- 2. I used the LENGTH() function
--    to count the number of characters
--    in each tweet.
--
-- 3. If the length is greater than 15,
--    I returned that tweet's ID.
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)