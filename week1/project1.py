def main():
    fav = input("Your favorite genre: ").capitalize()

    if fav == "Fantasy":
        print("You might enjoy The Poet Empress.")
    elif (fav == "Science Fiction" or fav == "Sci-Fi" or fav == "Sci Fi"):
        print("You might enjoy Platform Decay.")
    elif fav == "Mystery":
        print("You might enjoy The Keeper.")
    elif fav == "Thriller":
        print("You might enjoy It's Not Her.")
    elif fav == "Romance":
        print("You might enjoy The Night We Met.")
    elif fav == "Horror":
        print("You might enjoy Wolf Worm.")
    elif fav == "Biography":
        print("You might enjoy A Hymn to Life.")
    else:
        print("Please enter a valid genre.")

main()