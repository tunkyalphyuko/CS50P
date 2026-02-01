def main():
    ans = input("What is the answer to the great question? ").lower().strip()
    if not (ans == "42" or ans == "forty-two" or ans == "forty two"):
        print("No")
    else:
        print("Yes")
main()