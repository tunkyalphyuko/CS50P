months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)

            elif "," in date:
                month, day, year = date.split(",")
                month, day, year = int(month), int(day), int(year)

            elif "." in date:
                month, day, year = date.split(".")
                month, day, year = int(month), int(day), int(year)
                
            else:
                continue

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        except (ValueError, IndexError):
            pass

main()