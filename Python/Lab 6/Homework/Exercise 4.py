class SimplifiedThreeSumZero:
    def three_sum(self, nums):
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result


def main():
    nums = list(map(int, input("Enter array elements separated by space: ").split()))
    finder = SimplifiedThreeSumZero()
    result = finder.three_sum(nums)
    if result:
        print("Three elements that sum to zero are:", result)
    else:
        print("No three elements found that sum to zero.")


if __name__ == "__main__":
    main()
