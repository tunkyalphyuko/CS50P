userInput = input("Input: ")

print("Output: ", end="")

for i in userInput:
    if i.lower() not in ["a", "e", "i", "o", "u"]:
        print(i, end="")

print()