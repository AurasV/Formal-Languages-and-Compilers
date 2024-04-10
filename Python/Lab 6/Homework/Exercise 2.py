class RomanToInteger:
    def roman_to_int(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                integer += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                integer += roman[s[i]]
        return integer


def main():
    roman_numeral = input("Enter a Roman numeral: ")
    converter = RomanToInteger()
    print(f"The integer value is: {converter.roman_to_int(roman_numeral)}")


if __name__ == "__main__":
    main()
