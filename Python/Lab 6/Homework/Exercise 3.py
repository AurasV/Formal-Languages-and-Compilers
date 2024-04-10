class FindPair:
    def two_sum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []


def main():
    nums = list(map(int, input("Enter array elements separated by space: ").split()))
    target = int(input("Enter target sum: "))
    finder = FindPair()
    result = finder.two_sum(nums, target)
    if result:
        print(f"Pair at indices: {result[0]} and {result[1]}")
    else:
        print("No pair")


if __name__ == "__main__":
    main()
