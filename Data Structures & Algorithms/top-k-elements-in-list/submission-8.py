class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # dictionary to store intial keys and values (i.e. number and it's frequency)
        res = {}

        # we need to account for when all numbers in the list are the same
        bucket = [[] for i in range(len(nums) + 1)]
        
        # increments the frequency of i by 1 if it already exists in the dict 1 otherwise
        for i in nums:
            res[i] = 1 + res.get(i, 0)
        for key, value in res.items():
            bucket[value].append(key)

        output = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                output.append(j)
                if len(output) == k:
                    return output
        