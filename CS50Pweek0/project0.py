# Create a small Python program that uses functions, variables, return values, and at least one string method to solve a simple problem.

# Ask user for their interested A Level subjects. Tell them they will fail no matter what :>> 

def joke(x):
    subjects = x.lower().strip()
    return "You're failing " + subjects + " lol"

def main():
    user_input = input("Which A Level subjects you'd like to study? ")
    result = joke(user_input)

    print(result)

main()