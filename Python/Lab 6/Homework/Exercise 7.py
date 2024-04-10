def intersection(arr1, arr2):
    return list(filter(lambda x: x in arr1, arr2))


def main():
    arr1 = list(map(int, input("Enter elements of the first array separated by space: ").split()))
    arr2 = list(map(int, input("Enter elements of the second array separated by space: ").split()))
    print("The intersection of the two arrays is:", intersection(arr1, arr2))


if __name__ == "__main__":
    main()
