import sys


if __name__ == "__main__":
    print("Executable module " , __name__)
else: 
    print("Non-executable module" , __name__)

def main():
    print("main function")

main()