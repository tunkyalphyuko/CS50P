def main():
    user_input = input("Enter an emoticon! ")
    result = convert(user_input)
    print(result)

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()