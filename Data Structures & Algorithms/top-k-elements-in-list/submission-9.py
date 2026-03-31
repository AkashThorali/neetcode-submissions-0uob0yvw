class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)

        bucket = [[] for i in range(len(nums) + 1)]
        
        for number in set(nums): 
            index = count[number]
            bucket[index].append(number)
        
        res = []
        for arr in range(len(bucket) - 1, -1, -1):
            for value in bucket[arr]:
                res.append(value)
                if len(res) == k: 
                    return res
