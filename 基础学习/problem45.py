class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.len == 1:
            return 0
        curdistance = 0
        ans = 0
        nextdistance = 0
        i = 0
        for num in nums:
            nextdistance = max(num + i, nextdistance)
            if i == curdistance:
                if curdistance != (nums.len - 1):
                    ans += 1
                    curdistance = nextdistance
                    if nextdistance >= nums.len - 1:
                        break
                else:
                    break

        return ans
