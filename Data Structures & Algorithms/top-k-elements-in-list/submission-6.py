class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for i in nums: 
            if i in res: 
                res[i] += 1
            else: 
                res[i] = 1
        for key, value in res.items(): 
            bucket[value].append(key)
        
        output = []
        for i in range(len(bucket)-1, 0 , -1):
            for num in bucket[i]:
                output.append(num)
                if (len(output) == k):
                    return output

