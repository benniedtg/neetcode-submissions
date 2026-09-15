class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                # Convert Python's 0-based indexes to 1-based indexes.
                return [left + 1, right + 1]
            if current_sum < target:
                left += 1
            else:
                right -=1
        return []