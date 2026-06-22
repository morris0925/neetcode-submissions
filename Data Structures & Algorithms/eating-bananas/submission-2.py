class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Brute Force: piles.length <= h, so speed k can iterate through 1 ~ max(pile#) to find minimal
        => O(m*n)
        Optimize: Loop through 1 ~ max(pile) as speed using BINARY SEARCH!
        => O(logm*n)
        """
        l, r = 1, max(piles)
        # [3,6,7,11] different speed to test
        minSpeed = r
        while l <= r:
            mid = (r+l) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b / mid) #math.ceil = 無條件進位
            if hours <= h:
                if mid <= minSpeed:
                    minSpeed = mid
                    r = mid - 1
            else:
                l = mid + 1
        
        return minSpeed



