
# Interview / Viva Short Answer:

# Reverse Vowels of a String me hum two pointers use karte hain.
# Ek pointer start se aur ek end se chalta hai.
# Dono sides se vowels find karte hain.
# Jab dono vowels mil jate hain to unhe swap kar dete hain.
# Fir pointers ko aage aur peeche move karte hain.
# End me updated string return kar dete hain.

# Logic:

# 1. Sabhi vowels ko ek set me store karo for fast lookup.
# 2. String ko list me convert karo because Python strings immutable hoti hain.
# 3. Do pointers lo:
#    - left = start se
#    - right = end se
# 4. left pointer ko tab tak move karo jab tak vowel na mile.
# 5. right pointer ko tab tak move karo jab tak vowel na mile.
# 6. Dono vowels milne par unhe swap karo.
# 7. left ko +1 aur right ko -1 karo.
# 8. Jab tak left < right, process repeat karo.
# 9. Last me list ko join karke final string return karo.

# Approach:

# 1. Store all vowels in a set/string.
# 2. Convert string into list because strings are immutable in Python.
# 3. Use two pointers:
#    - left starts from beginning
#    - right starts from end
# 4. Move left until a vowel is found.
# 5. Move right until a vowel is found.
# 6. Swap both vowels.
# 7. Move both pointers inward.
# 8. Continue until left < right.
# 9. Join list back into string and return.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)   # string ko list me convert kiya because string immutable hoti hai
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            # left pointer ko vowel tak le jao
            while left < right and s[left] not in vowels:
                left += 1
            
            # right pointer ko vowel tak le jao
            while left < right and s[right] not in vowels:
                right -= 1
            
            # dono vowels mil gaye to swap
            s[left], s[right] = s[right], s[left]
            
            # pointers update
            left += 1
            right -= 1
        
        return "".join(s)
    