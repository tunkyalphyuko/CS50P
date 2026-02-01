def main():
    ans = input("What time is it? ").strip()

    time = convert(ans)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    h, min = time.split(":")

    h2 = float(h)
    min2 = float(min)

    return h2 + (min2/60)
    

if __name__ == "__main__":
    main()
