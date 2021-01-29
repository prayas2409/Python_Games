
def main():
    print("In the main function")

# bad practice
print("calling main from outside")
main()

# good practice
if __name__ == "__main__": 
    # checks if running current file only then executes below code
    print("calling main method from inside")
    main()