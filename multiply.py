class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "":
            return "0"
        if num1 == "0" or num2 == "0":
            return "0"

        results = []
        for i in range(len(num1) - 1, -1, -1):
            n1 = num1[i]
            move = 0
            cur = ""
            for j in range(len(num2) - 1, -1, -1):
                n2 = num2[j]
                sum = move + int(n1) * int(n2)
                move = int(sum / 10)
                cur = cur + str(sum % 10)
            cur = cur + str(move if move != 0 else "")
            results.append(''.join(reversed(cur))+(Solution().generateZero(len(num1)-i-1)))

        res = results[0]
        for i in range(1, len(results)):
            res = Solution().addStrings(res, results[i])
        return res

    def generateZero(self, n):
        ans = ""
        for i in range(n):
            ans = ans + "0"
        return ans

    def addStrings(self, num1, num2):
        res = ""
        move = 0
        i = len(num1)-1
        j = len(num2)-1
        while (i >= 0 or j >= 0 or move!=0):
            n1 = num1[i] if i >= 0 else 0
            n2 = num2[j] if j >= 0 else 0
            sum = move + int(n1) + int(n2)
            move = int(sum / 10)

            res = res + str(sum % 10)

            if i >= 0:
                i = i-1
            if j >= 0:
                j = j-1

        return ''.join(reversed(res))


if __name__ == '__main__':
    print(Solution().multiply("456","123"))
    # print(Solution().addStrings('738','6150'))

