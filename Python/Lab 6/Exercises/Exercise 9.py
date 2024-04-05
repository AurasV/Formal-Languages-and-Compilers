from math import pi


def deg_to_rad():
    deg = float(input("Enter a number to convert to radians: "))
    rad = deg * (pi/180)
    print(rad)


def rad_to_deg():
    rad = float(input("Enter a number to convert to degrees: "))
    deg = rad * (180/pi)
    print(deg)


def main():
    while True:
        n = input("'1' for degrees to radians, '2' for radians to degrees, 'e' to exit: ")
        if n == '1':
            deg_to_rad()
        elif n == '2':
            rad_to_deg()
        elif n == 'e':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()