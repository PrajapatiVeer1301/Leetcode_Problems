-- Logic:
--
-- 1. Select only the records
--    where the login year is 2020.
--
-- 2. Group the records by user_id.
--
-- 3. Find the latest login
--    using MAX(time_stamp).
--
-- 4. Display user_id
--    and the latest login time.

-- Algorithm:
--
-- 1. Read the Logins table.
--
-- 2. Filter records
--    where YEAR(time_stamp) = 2020.
--
-- 3. Group by user_id.
--
-- 4. Use MAX(time_stamp)
--    to find the latest login.
--
-- 5. Return user_id
--    and last_stamp.

SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;

-- Interview Explanation:
--
-- 1. I filtered the records
--    to include only logins from 2020.
--
-- 2. I grouped the records
--    by user_id.
--
-- 3. I used MAX(time_stamp)
--    to get the latest login
--    for each user.
--
-- 4. Users without a login in 2020
--    are automatically excluded
--    because of the WHERE condition.
--
-- Time Complexity: O(n)
-- Space Complexity: O(1) (excluding output)
