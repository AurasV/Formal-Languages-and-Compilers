import os
import platform

def main():
    print("Operating System:", os.name)
    print("Detailed OS Name:", platform.system(), platform.release())
    print("Current Directory:", os.getcwd())
    print("Files and directories in the current directory:", os.listdir('.'))


if __name__ == "__main__":
    main()
