def main():
     
    while True:
        fraction = input("Fraction: ")

        try:
            parts = fraction.split("/")

            x = int(parts[0])
            y = int(parts[1])

            percentage = (x/y) * 100

            if percentage <= 1:
                print("E")
                break

            elif percentage >= 99:
                print("F")
                break

            else:
                print(f"{round(percentage)}%")
                break

        except ValueError:
            pass
        
        except ZeroDivisionError:
            pass

main()