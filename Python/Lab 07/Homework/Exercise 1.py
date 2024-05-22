import argparse
import os


def create_file(path, filename):
    filepath = os.path.join(path, filename)

    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write("New file\n")
            file.write("ahahasgasgasgasgahsh.\n")
            file.write("RaNdOm TeXt.\n")
        print(f"File '{filename}' created at '{path}'.")
    else:
        print(f"File '{filename}' already exists at '{path}'.")


def main():
    parser = argparse.ArgumentParser(description='Create a file if it does not exist.')
    parser.add_argument('--path', type=str, help='The path to the folder', required=True)
    parser.add_argument('--filename', type=str, help='The name of the file', required=True)

    args = parser.parse_args()

    create_file(args.path, args.filename)


if __name__ == "__main__":
    main()

# Test command
# python "Exercise 1.py" --path "path\to\folder" --filename "test_file.txt"
