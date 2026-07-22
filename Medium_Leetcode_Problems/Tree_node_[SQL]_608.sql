-- Logic:
--
-- 1. If p_id is NULL,
--    the node is Root.
--
-- 2. Else if the node's id
--    never appears in p_id,
--    it has no children,
--    so it is a Leaf.
--
-- 3. Otherwise,
--    it has both parent
--    and child,
--    so it is an Inner node.

-- Algorithm:
--
-- 1. Read every row.
--
-- 2. Check:
--      p_id IS NULL
--      -> Root
--
-- 3. Otherwise,
--      check whether id exists
--      in p_id column.
--
-- 4. If id does not exist,
--      -> Leaf
--
-- 5. Else
--      -> Inner
--
-- 6. Return id and type.

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id NOT IN (
            SELECT DISTINCT p_id
            FROM Tree
            WHERE p_id IS NOT NULL
        ) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree;

-- Interview Explanation:
--
-- 1. I used a CASE statement
--    to classify each node.
--
-- 2. If p_id is NULL,
--    the node is Root.
--
-- 3. If the node's id does not
--    appear in the p_id column,
--    it has no children,
--    so it is Leaf.
--
-- 4. Otherwise,
--    it is an Inner node.
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)
