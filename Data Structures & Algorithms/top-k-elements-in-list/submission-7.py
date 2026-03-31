class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for i in nums: 
            res[i] = 1 + res.get(i, 0)
        for key, value in res.items(): 
            bucket[value].append(key)
        
        output = []
        for i in range(len(bucket)-1, 0 , -1):
            for num in bucket[i]:
                output.append(num)
                if (len(output) == k):
                    return output

