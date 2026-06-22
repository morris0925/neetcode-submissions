class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #[1,2,4,5] t=6
        # |     |
        
        l, r = 0, len(numbers) -1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
        
        return [] # if there's no answer (despite no such case)
            