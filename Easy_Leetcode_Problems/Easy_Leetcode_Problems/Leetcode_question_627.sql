-- ## 💡 Logic
-- ##
-- ## The Salary table contains employee information.
-- ## The sex column contains either 'm' or 'f'.
-- ##
-- ## We need to swap all 'm' values to 'f' and all 'f'
-- ## values to 'm'.
-- ##
-- ## We must use only one UPDATE statement.
-- ## We cannot use a SELECT statement or temporary table.
-- ##
-- ## The CASE statement checks the current value of sex.
-- ##
-- ## If sex = 'm', change it to 'f'.
-- ## If sex = 'f', change it to 'm'.
-- ##
-- ## The id, name, and salary columns remain unchanged.


-- ## 🔄 Algorithm
-- ##
-- ## 1. Start with the Salary table.
-- ##
-- ## 2. Use a single UPDATE statement.
-- ##
-- ## 3. Use the SET clause to update the sex column.
-- ##
-- ## 4. Use CASE to check the current sex value.
-- ##
-- ## 5. If sex is 'm', set it to 'f'.
-- ##
-- ## 6. If sex is 'f', set it to 'm'.
-- ##
-- ## 7. Update all rows and finish.
-- ##
-- ## 8. No SELECT statement or temporary table is required.


-- ## 🧑‍💻 SQL Code

UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    WHEN sex = 'f' THEN 'm'
END;


-- ## 🧪 Example
-- ##
-- ## Before:
-- ##
-- ## id | name | sex | salary
-- ## 1  | A    | m   | 2500
-- ## 2  | B    | f   | 1500
-- ## 3  | C    | m   | 5500
-- ## 4  | D    | f   | 500
-- ##
-- ## After:
-- ##
-- ## id | name | sex | salary
-- ## 1  | A    | f   | 2500
-- ## 2  | B    | m   | 1500
-- ## 3  | C    | f   | 5500
-- ## 4  | D    | m   | 500
-- ##
-- ## The sex values are swapped.
-- ## All other columns remain unchanged.


-- ## 🎯 Interview Explanation
-- ##
-- ## "I use a single UPDATE statement with a CASE expression
-- ## to swap the values in the sex column.
-- ## If the current value is 'm', I change it to 'f'.
-- ## If the current value is 'f', I change it to 'm'.
-- ## The query updates all rows without using a SELECT
-- ## statement or a temporary table."


-- ## ⭐ Key Trick
-- ##
-- ## Use CASE inside UPDATE to change values conditionally.
-- ##
-- ## UPDATE Salary
-- ## SET sex = CASE
-- ##     WHEN sex = 'm' THEN 'f'
-- ##     WHEN sex = 'f' THEN 'm'
-- ## END;
-- ##
-- ## This swaps both values in one statement.


-- ## ⏱️ Complexity
-- ##
-- ## Time Complexity: O(n)
-- ## The database processes all n rows.
-- ##
-- ## Extra Space Complexity: O(1) conceptually
-- ## No temporary table is created by the query.
-- ## Actual database execution may use internal resources.