// Logic:
//
// 1. Create a HashMap.
//
// 2. Generate a unique ID for each URL.
//
// 3. Store:
//    ID -> Original URL.
//
// 4. Return:
//    http://tinyurl.com/ID
//
// 5. During decoding,
//    extract the ID.
//
// 6. Return the original URL
//    from the HashMap.

// Algorithm:
//
// 1. Create a HashMap.
//
// 2. Initialize an ID counter.
//
// 3. Encode:
//    - Convert ID to String.
//    - Store ID and URL in HashMap.
//    - Return short URL.
//    - Increment ID.
//
// 4. Decode:
//    - Extract ID from short URL.
//    - Return original URL from HashMap.


import java.util.HashMap;

public class Codec {

    private HashMap<String, String> map = new HashMap<>();
    private int id = 0;

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {

        String key = String.valueOf(id);
        map.put(key, longUrl);
        id++;

        return "http://tinyurl.com/" + key;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {

        String key = shortUrl.substring(shortUrl.lastIndexOf("/") + 1);
        return map.get(key);
    }
}

// Interview Explanation:
//
// 1. I used a HashMap to store
//    the mapping between a unique ID
//    and the original URL.
//
// 2. During encoding,
//    I generate a unique ID,
//    store the URL,
//    and return a tiny URL.
//
// 3. During decoding,
//    I extract the ID from the tiny URL
//    and retrieve the original URL
//    from the HashMap.
//
// Time Complexity:
// Encode -> O(1)
// Decode -> O(1)
//
// Space Complexity: O(n)