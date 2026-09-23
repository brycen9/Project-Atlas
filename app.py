from asteroid_api import get_data

def main():
    greeting()

def greeting():
    text = "Project Atlas"
    centered_text = text.center(40)
    print("=" * 40)
    print(centered_text)
    print("=" * 40)
    print()
    print("Welcome, Commander.")
    print()
    print("Current Version: 0.1")
    print()
    print("-" * 40)
    print()
    print("1. Search Asteroid")
    print()
    print("2. Exit")
    print()
    print("-" * 40)
    print()

    user_input = 0
    while user_input != 1 and user_input != 2:
        try:
            user_input = int(input("Enter your selection: "))
        except ValueError:
            print("Must enter 1 or 2.")
            print()
            continue

        if (user_input == 1):
            print()
            search_asteroid()
            return
            
        elif (user_input == 2):
            print("Shutting down...Goodbye")
            return

        else:
            print()
            print("Error! Please enter 1 or 2.")
            print()

def search_asteroid():
    text = "Asteroid Database"
    centered_text = text.center(27)
    print("=" * 27)
    print(centered_text)
    print("=" * 27)
    print()

    asteroid_name = input("Enter the asteroid name: ")
    print()
    print(f"Searching for {asteroid_name}...")

    data = get_data(asteroid_name)

    if "object" in data:
        text = "ASTEROID FOUND"
        centered_text = text.center(28)
        print("=" * 28)
        print(centered_text)
        print("=" * 28)
        print()
        print(f"Name: {data["object"]["shortname"]}")
        print(f"Designation: {data["object"]["des"]}")
        print(f"Near-Earth Object: {data["object"]["neo"]}")
        print(f"Potentially Hazardous: {data["object"]["pha"]}")
        print()

    else:
        print()
        text = "ASTEROID NOT FOUND"
        centered_text = text.center(28)
        print("=" * 28)
        print(centered_text)
        print("=" * 28)
        print()

    
if __name__ == "__main__":
    main()