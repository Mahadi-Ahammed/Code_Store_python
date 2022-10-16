def containsDuplicate(self, nums: List[int]) -> bool:
        conv = set(nums)
        if len(conv)!=len(nums):
            return True
        return False