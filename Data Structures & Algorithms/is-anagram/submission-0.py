class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) +  1
        
        for char in t:
            if char not in frequency:
                return False

            frequency[char] -= 1
            if frequency[char] == 0:
                del frequency[char]
        
        return len(frequency) == 0