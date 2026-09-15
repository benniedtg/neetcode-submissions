class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for n in numbers:
            if n - 1 not in numbers:
                current_num = n
                current_len = 1

                while current_num + 1 in numbers:
                    current_num += 1
                    current_len += 1
                longest = max(longest, current_len)
        return longest