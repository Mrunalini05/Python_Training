#longest palindrome
#ip: abdbsdabca
#op: bdb

def longest_palindrome(s):
    if not s:  # If the string is empty, return an empty string
        return ""

    start, end = 0, 0  # These will hold the start and end indices of the longest palindrome

    for i in range(len(s)):
        # Check for odd-length palindromes centered at `i`
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start, end = left, right
            left -= 1
            right += 1

        # Check for even-length palindromes centered between `i` and `i+1`
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start, end = left, right
            left -= 1
            right += 1

    return s[start:end + 1]

# Example usage:
input_string = "abdbsdabca"
print(longest_palindrome(input_string))  # Output: "bdb"
