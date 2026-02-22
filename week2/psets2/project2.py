import webbrowser
from pygame import mixer

music = "piano.mp3"

def main():
    mixer.init()

    stories = {
        "feminism": {
            "name": "The Story of an Hour",
            "link": "https://americanliterature.com/author/kate-chopin/short-story/the-story-of-an-hour"
        },
        "horror": {
            "name": "The Tell-Tale Heart",
            "link": "https://americanliterature.com/author/edgar-allan-poe/short-story/the-tell-tale-heart"
        },
        "classic": {
            "name": "The Cactus",
            "link": "https://americanliterature.com/author/o-henry/short-story/the-cactus"
        }
    }

    genre = input("What kind of story do you want? (Feminism, Horror, Classic): ").lower()

    if genre in stories:
        story = stories[genre]

        try:
            mixer.music.load(music)
            mixer.music.play(-1)
        except:
            print("")

        print(f"I recommend {story['name']}.")
        print(f"Read it here: {story['link']}")

        webbrowser.open(story['link'])

        input("Enter to stop the music and exit.")
        mixer.music.stop()
        
    else:
        print("Sorry I don't have a recommendation for that genre yet.")


main()