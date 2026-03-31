class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = [[] for i in range(len(nums) + 1)]

        for i in nums:

            # adds 1 to perviously existing count
            # when there is no pervious count sets it to 1
            count[i] = 1 + count.get(i, 0)

        for i, c in count.items():
            result[c].append(i)

        
        total = []
        for i in range(len(result) - 1, 0 , -1):
            for num in result[i]:
                total.append(num)
                if (len(total) == k):
                    return total
                
