import argparse
import csv


def compute_sum_and_product(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)

        first_row = next(reader)
        while not any(cell.isdigit() for cell in first_row):
            first_row = next(reader)

        header = first_row
        index_of_integer_column = None
        for i, col in enumerate(header):
            try:
                int(col)
                index_of_integer_column = i
                break
            except ValueError:
                pass

        if index_of_integer_column is None:
            print("Error: No int column found in the input")
            return

        numbers = []
        for row in reader:
            try:
                numbers.append(int(row[index_of_integer_column]))
            except ValueError:
                pass

    if not numbers:
        print("Error: No ints found in the input")
        return

    sum_result = sum(numbers)
    product_result = 1
    for num in numbers:
        product_result *= num

    with open(output_file, 'w') as result_file:
        result_file.write(f"Sum: {sum_result}\n")
        result_file.write(f"Product: {product_result}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute sum and product of integers from a CSV file")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output file to store results")
    args = parser.parse_args()

    compute_sum_and_product(args.input_file, args.output_file)
