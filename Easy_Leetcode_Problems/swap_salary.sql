
# Approach:
# Use single UPDATE statement with CASE expression.
# If sex = 'm', make it 'f'
# Else make it 'm'

# Logic:
# CASE acts like if-else in SQL.
# It checks each row and swaps the value directly.



UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    ELSE 'm'
END;