# 283. Move Zeroes
#
# Approach: Two Pointer Approach
#
# We use two pointers:
#
# i -> traverses the array
# j -> keeps track of the position where the next non-zero element should be placed
#
# We iterate through the array, and whenever we find a non-zero element,
# we swap it with the element at index j, then increment j.
#
# This ensures:
# - All non-zero elements are moved to the front
# - Their relative order remains the same
# - All zeroes automatically move to the end
#
# Logic:
# The main idea is to place all non-zero elements at the beginning of the array
# while maintaining their original order.
#
# j always points to the next correct position for a non-zero element.
# i checks every element in the array.
# If nums[i] != 0, we swap nums[i] with nums[j].
# Then we move j forward.
#
# Time Complexity: O(n)
# Space Complexity: O(1)




class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
                
       