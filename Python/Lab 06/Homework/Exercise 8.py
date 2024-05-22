def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


def main():
    lst = list(map(int, input("Enter elements of the list separated by space: ").split()))
    print("List after removing duplicates:", remove_duplicates(lst))


if __name__ == "__main__":
    main()