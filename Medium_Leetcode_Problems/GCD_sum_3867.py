# Logic:
#
# 1. Traverse the array.
#
# 2. Maintain the maximum element seen so far.
#
# 3. Compute gcd(current number, maximum).
#
# 4. Store it in prefixGcd.
#
# 5. Sort prefixGcd.
#
# 6. Pair the smallest and largest elements.
#
# 7. Compute gcd of every pair.
#
# 8. Add all gcd values.
#
# 9. Return the total sum.

# Algorithm:
#
# 1. Create an empty prefixGcd list.
#
# 2. Find the running maximum.
#
# 3. Store gcd(nums[i], running maximum).
#
# 4. Sort prefixGcd.
#
# 5. Initialize two pointers:
#    left = 0
#    right = n-1
#
# 6. While left < right:
#      sum += gcd(prefixGcd[left], prefixGcd[right])
#      left++
#      right--
#
# 7. Return sum.

from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        prefixGcd = []

        maximum = 0

        for num in nums:
            maximum = max(maximum, num)
            prefixGcd.append(gcd(num, maximum))

        prefixGcd.sort()

        left = 0
        right = len(prefixGcd) - 1

        answer = 0

        while left < right:
            answer += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return answer
    
# Interview Explanation:
#
# 1. I maintained the maximum element while traversing the array.
#
# 2. For every element,
#    I computed gcd(current element, running maximum)
#    and stored it in prefixGcd.
#
# 3. Then I sorted the prefixGcd array.
#
# 4. Using two pointers,
#    I paired the smallest and largest elements.
#
# 5. I calculated the gcd of each pair
#    and added it to the answer.
#
# 6. Finally, I returned the total sum.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)