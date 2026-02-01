def main():
    exp = input("Expression: ").strip()

    x, y, z = exp.split(" ")

    x = int(x)
    z = int(z)

    if y == "+":
        result = float(x+z)
    elif y == "-":
        result = float(x-z)
    elif y == "*":
        result = float(x*z)
    elif y == "/":
        result = float(x/z)
    
    print(result)

main()