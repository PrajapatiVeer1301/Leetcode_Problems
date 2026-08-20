# -------- 💡 Logic -----------

# 1. Create a dictionary.
#
#       key   → sorted version of string
#       value → list of anagrams
#
# 2. Take each string.
#
# 3. Sort the characters of the string.
#
# 4. Convert the sorted characters into a string.
#    This becomes the key.
#
# 5. Add the original string to that key's list.
#
# 6. Finally, return all values of the dictionary.


# -------- 🔄 Algorithm --------

# Step 1: Create an empty dictionary.
#
# Step 2: Traverse every string in strs.
#
# Step 3: Sort the characters of the string.
#
# Step 4: Create a string key from the sorted characters.
#
# Step 5: If the key does not exist,
#         create an empty list for that key.
#
# Step 6: Add the original string to the group.
#
# Step 7: Return all dictionary values.


# -------- 🧪 Dry Run ----------

# Input:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# --------------------------------
#
# word = "eat"
#
# Sorted:
# "eat" → "aet"
#
# Dictionary:
# aet → [eat]
#
# --------------------------------
#
# word = "tea"
#
# Sorted:
# "tea" → "aet"
#
# Dictionary:
# aet → [eat, tea]
#
# --------------------------------
#
# word = "tan"
#
# Sorted:
# "tan" → "ant"
#
# Dictionary:
# aet → [eat, tea]
# ant → [tan]
#
# --------------------------------
#
# word = "ate"
#
# Sorted:
# "ate" → "aet"
#
# Dictionary:
# aet → [eat, tea, ate]
# ant → [tan]
#
# --------------------------------
#
# word = "nat"
#
# Sorted:
# "nat" → "ant"
#
# Dictionary:
# aet → [eat, tea, ate]
# ant → [tan, nat]
#
# --------------------------------
#
# word = "bat"
#
# Sorted:
# "bat" → "abt"
#
# Dictionary:
# aet → [eat, tea, ate]
# ant → [tan, nat]
# abt → [bat]
#
# --------------------------------
#
# Final Output:
#
# [[eat, tea, ate],
#  [tan, nat],
#  [bat]]
#
# Order does not matter.


# -------- 🐍 Python Code ----------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

            # Sort characters and create the key
            key = ''.join(sorted(word))

            # Create a new group if key does not exist
            if key not in groups:
                groups[key] = []

            # Add the original word to its group
            groups[key].append(word)

        # Return all anagram groups
        return list(groups.values())


# -------- 🎯 Interview Explanation -----------

# I use a dictionary to group anagrams.
#
# For every string, I sort its characters.
# Anagrams always produce the same sorted string.
#
# For example:
#
# "eat" → "aet"
# "tea" → "aet"
# "ate" → "aet"
#
# Therefore, "aet" can be used as the key.
#
# All strings having the same key are stored
# in the same list.
#
# Finally, I return all the values of the dictionary.
#
# Time Complexity:
# O(n * k log k)
#
# n = number of strings
# k = maximum length of a string
#
# Space Complexity:
# O(n * k)
#
# because we store the strings in the dictionary.


# -------- ⭐ Key Trick -----------

# Anagrams → Same Sorted Key
#
# "eat" → "aet"
# "tea" → "aet"
# "ate" → "aet"
#
# Same key
#    ↓
# Same group