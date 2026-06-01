class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i in range(len(nums)):
            need = target - nums[i]
            print(mp)
            print("need:", need)
            if need in mp:
                return [mp[need], i]
            mp[nums[i]] = i
        return []