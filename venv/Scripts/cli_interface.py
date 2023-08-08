# Define a simple command-line interface (CLI) for user interaction
def main():
    print("Welcome to Zomato Chronicles!")
    print("1. Search for restaurants")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        location = input("Enter the city name: ")  # Allow users to enter location
        cuisine = input("Enter the cuisine: ")      # Allow users to enter cuisine
        # Implement restaurant search logic using Zomato API
        print("Searching for restaurants...")
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
