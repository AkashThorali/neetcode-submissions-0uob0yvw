class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else: 
                freq[i] = 1
        
        sorted_numbers = list(sorted(freq.keys()))
        print(sorted_numbers)

        count = 1
        longest = 1

        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i + 1] - sorted_numbers[i] == 1:
                count += 1
            else:
                longest = max(longest, count)
                count = 1

        longest = max(longest, count)
        return longest
        
            