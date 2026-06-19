class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []
        freq = {}
        for i in nums: 
            freq[i] = freq.get(i, 0) + 1
        print(freq)

        res = [[] for i in range(len(nums) + 1)]
        print(res)

        for key,value in freq.items():
            res[value].append(key)
        print(res)

        for i in range(len(res) - 1, -1, -1):
            for j in res[i]:
                topK.append(j)
                if len(topK) == k: 
                    return topK

