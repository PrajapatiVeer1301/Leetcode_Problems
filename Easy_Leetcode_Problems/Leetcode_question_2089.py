
# ## TARGET INDICES AFTER SORTING ARRAY_2089

# ## LOGIC:
# ## First, sort the array in non-decreasing order.
# ## Then, check every index of the sorted array.
# ## If nums[i] == target, store index i in the result list.
# ## Since we traverse from left to right, the indices are
# ## automatically stored in increasing order.
# ## If the target is not found, return an empty list.

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        # ## Step 1: Sort the array in non-decreasing order.
        nums.sort()

        # ## Step 2: Create an empty list to store target indices.
        result = []

        # ## Step 3: Traverse the sorted array using indices.
        for i in range(len(nums)):

            # ## Step 4: Check whether the current element equals target.
            if nums[i] == target:

                # ## Step 5: Store the index if the target is found.
                result.append(i)

        # ## Step 6: Return all target indices in increasing order.
        return result


# ## EXAMPLE:
# ## Input: nums = [1, 2, 5, 2, 3], target = 2
# ## After sorting: [1, 2, 2, 3, 5]
# ## Output: [1, 2]


# ## DRY RUN:
# ## Original array: [1, 2, 5, 2, 3]
# ## Target: 2
# ##
# ## Step 1: Sort the array.
# ## Sorted array = [1, 2, 2, 3, 5]
# ##
# ## Step 2: Check each index.
# ## Index 0, value 1 -> Target not found, ignore.
# ## Index 1, value 2 -> Target found, append index 1.
# ## Index 2, value 2 -> Target found, append index 2.
# ## Index 3, value 3 -> Target not found, ignore.
# ## Index 4, value 5 -> Target not found, ignore.
# ##
# ## Final result = [1, 2]


# ## ALGORITHM:
# ## Step 1: Sort nums using nums.sort().
# ## Step 2: Create an empty list named result.
# ## Step 3: Traverse the array from index 0 to len(nums) - 1.
# ## Step 4: If nums[i] == target, append i to result.
# ## Step 5: Return result.


# ## INTERVIEW EXPLANATION:
# ## I first sort the given array in non-decreasing order.
# ## Then, I traverse the sorted array from left to right.
# ## At each index, I compare the current element with the target.
# ## If the element equals the target, I add its index to the result.
# ## If the target occurs multiple times, I collect every matching index.
# ## Since I traverse the array in increasing index order,
# ## the returned indices are already sorted.
# ## If no element matches the target, the result remains empty.
# ## Finally, I return the result list.


# ## KEY TRICK:
# ## nums.sort() arranges the elements in non-decreasing order.
# ## nums[i] == target checks whether the current element matches.
# ## result.append(i) stores the index, not the element.
# ## Traversing from left to right keeps the indices in increasing order.


# ## TIME AND SPACE COMPLEXITY:
# ## Let n be the number of elements in nums.
# ##
# ## Time Complexity: O(n log n)
# ## Sorting takes O(n log n), and traversing takes O(n).
# ##
# ## Auxiliary Space Complexity: O(n) in the worst case
# ## Sorting may use implementation-dependent extra space.
# ## The result list can contain up to n indices.
