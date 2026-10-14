-- ## 💡 Logic
-- ##
-- ## We have two tables: Users and Transactions.
-- ## The Users table contains account numbers and user names.
-- ## The Transactions table contains money received or transferred.
-- ##
-- ## The balance of an account is the sum of all its
-- ## transaction amounts.
-- ##
-- ## We need to return the name and balance of users whose
-- ## balance is greater than 10000.
-- ##
-- ## JOIN connects Users and Transactions using account.
-- ## SUM(t.amount) calculates the total balance.
-- ## GROUP BY groups transactions for each user.
-- ## HAVING filters users whose total balance exceeds 10000.


-- ## 🔄 Algorithm
-- ##
-- ## 1. Start with the Users table.
-- ##
-- ## 2. Join Users with Transactions using the account column.
-- ##
-- ## 3. Group the records by account and name.
-- ##
-- ## 4. Calculate the total balance using SUM(t.amount).
-- ##
-- ## 5. Use HAVING to keep balances greater than 10000.
-- ##
-- ## 6. Return the user's name and balance.


-- ## 🧑‍💻 SQL Code

SELECT
    u.name,
    SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t
    ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;


-- ## 🧪 Dry Run
-- ##
-- ## Example transactions:
-- ##
-- ## Alice: 7000 + 7000 - 3000 = 11000
-- ## Bob:   1000
-- ## Charlie: 6000 + 6000 - 4000 = 8000
-- ##
-- ## Check each balance:
-- ##
-- ## Alice:
-- ## 11000 > 10000, so include Alice.
-- ##
-- ## Bob:
-- ## 1000 <= 10000, so exclude Bob.
-- ##
-- ## Charlie:
-- ## 8000 <= 10000, so exclude Charlie.
-- ##
-- ## Final Output:
-- ##
-- ## name  | balance
-- ## Alice | 11000


-- ## 🎯 Interview Explanation
-- ##
-- ## "I join the Users and Transactions tables using the
-- ## account column.
-- ## Then I group the records by account and user name.
-- ## I use SUM() to calculate each user's total balance.
-- ## Finally, I use HAVING to return only users whose
-- ## balance is greater than 10000."


-- ## ⭐ Key Trick
-- ##
-- ## WHERE filters individual rows before grouping.
-- ## HAVING filters groups after aggregation.
-- ##
-- ## Since we need to filter the result of SUM(),
-- ## we use HAVING SUM(t.amount) > 10000.


-- ## ⏱️ Complexity
-- ##
-- ## Conceptually, the query processes the transaction records
-- ## and groups them by account.
-- ## Exact time and space complexity depend on the database
-- ## engine, indexes, and execution plan.