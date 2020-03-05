class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        ans = [0] * num_people
        give = 0
        while candies > 0:
            ans[give % num_people] += min(give + 1, candies)
            give += 1
            candies -= give
        return ans


if __name__ == "__main__":
    print(Solution().distributeCandies(7, 4))
