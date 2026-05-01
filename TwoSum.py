from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumHash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in twoSumHash:
                return [twoSumHash[complement], i]
            
            twoSumHash[num]=i
        
        return []

if __name__ == "__main__":
    solution = Solution()
    test_list = [2,5,5,11]
    target = 10
    print(solution.twoSum(test_list,target))