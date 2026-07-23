# Logic:
#
# 1. Create a dictionary.
#
# 2. Generate a unique ID
#    for every URL.
#
# 3. Store:
#
#       ID -> Original URL
#
# 4. Return:
#
#       http://tinyurl.com/ID
#
# 5. During decoding,
#    extract the ID.
#
# 6. Return the URL
#    stored in the dictionary.

# Algorithm:
#
# 1. Create an empty dictionary.
#
# 2. Initialize a counter.
#
# 3. Encode:
#      Store URL using counter.
#      Return tiny URL.
#
# 4. Decode:
#      Extract ID.
#      Return stored URL.

class Codec:

    def __init__(self):
        self.url_map = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        self.url_map[str(self.id)] = longUrl
        shortUrl = "http://tinyurl.com/" + str(self.id)
        self.id += 1
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.split("/")[-1]
        return self.url_map[key]

# Interview Explanation:
#
# 1. I used a dictionary to store
#    the mapping between an ID
#    and the original URL.
#
# 2. Every new URL gets a unique ID.
#
# 3. During encoding,
#    I return a tiny URL using that ID.
#
# 4. During decoding,
#    I extract the ID from the tiny URL
#    and return the original URL
#    from the dictionary.
#
# Time Complexity:
# Encode -> O(1)
# Decode -> O(1)
#
# Space Complexity: O(n)