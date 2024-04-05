def palindrome_list(l):
    l_rev = l
    l_rev.reverse()
    if l == l_rev:
        return True
    else:
        return False


def main():
    n = int(input("Enter number of elements in list: "))
    l = []
    for i in range(0,n):
        x = input("Enter element: ")
        l.append(x)
    print("List:", l)

    if palindrome_list(l):
        print("List is a palindrome.")
    else:
        print("List is not a palindrome.")

if __name__ == "__main__":
    main()