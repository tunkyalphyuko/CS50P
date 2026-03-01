# S U V A T

def main():

    while True:

        find = input("What are you finding (S/U/V/A/T)? ").lower()

        try:

            if find == "s":
                u = float(input("Initial Velocity (m/s): "))
                a = float(input("Acceleration (m/s2): "))
                t = float(input("Time Taken (s): "))

                s = (u*t) + ((1/2)*a*(t*t))
                print(f"Displacement: {s:.1f} m")
                break

            elif find == "u":
                a = float(input("Acceleration (m/s2): "))
                t = float(input("Time Taken (s): "))
                s = float(input("Displacement (m): "))

                u = (s/t) - ((1/2)*a*t)
                print(f"Initial Velocity: {u:.1f} m/s")
                break

            elif find == "a":
                u = float(input("Initial Velocity (m/s): "))
                t = float(input("Time Taken (s): "))
                s = float(input("Displacement (m): "))

                a = (2/(t*t))*(s-(u*t))
                print(f"Acceleration: {a:.1f} m/s2")
                break

            elif find == "v":
                u = float(input("Initial Velocity (m/s): "))
                t = float(input("Time Taken (s): "))
                a = float(input("Acceleration (m/s2): "))

                v = u + (a*t)
                print(f"Final Velocity: {v:.1f} m/s")
                break

            elif find == "t":
                u = float(input("Initial Velocity (m/s): "))
                v = float(input("Final Velocity (m/s): "))
                a = float(input("Acceleration (m/s2): "))

                t = (v - u)/a
                print(f"Time Taken: {t:.1f} s")
                break

            else:
                print("The system does not support your input.")

        except Exception:
            print("Enter a valid number.")

main()
