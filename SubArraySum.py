class Solution:
    def subarraySum(self, arr, target):
        i = 0
        sum = 0

        for j in range(len(arr)):
            sum += arr[j]

            while sum > target:
                sum -= arr[i]
                i += 1

            if sum == target:
                return [i + 1, j + 1]

        return [-1]
