from kanye_songs import kanye_list
import random
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    album: str
    length: int
    plays: str
    tracklist: int
    year: int

#assign a random index for the correct song
correct_song_index = random.randint(0, 205)
correct_song = kanye_list[correct_song_index]

print(correct_song)
print("Welcome to the Kanye West Song Guessing Game")

user_guess = kanye_list[206]

total_guesses = 0

def compare_albums( user_song: Song ) -> str:
    if int(user_song.album[:2]) > int(correct_song.album[:2]):
        return "Older Album"
    elif int(user_song.album[:2]) < int(correct_song.album[:2]):
        return "Newer Album"
    else:
        return "Correct Album"
    
def compare_tracklist( user_song: Song) -> str:
    if user_song.tracklist > correct_song.tracklist:
        return "Earlier in the Album"
    if user_song.tracklist < correct_song.tracklist:
        return "Later in the Album"
    else:
        return "Correct Track Number"

def remove_commas ( plays: str) -> int:
    new_string = ""
    for character in plays:
        if "," not in character:
            new_string = new_string + character
    return int(new_string)
    
def compare_lengths( user_song: Song) -> str:
    if user_song.length > correct_song.length:
        return "Shorter Song"
    elif user_song.length < correct_song.length:
        return "Longer Song"
    else:
        return "Correct Song Length"

def compare_plays ( user_song: Song) -> str:
    if remove_commas(user_song.plays) > remove_commas(correct_song.plays):
        return "Less Popular Song"
    elif remove_commas(user_song.plays) < remove_commas(correct_song.plays):
        return "More Popular Song"
    else:
        return "Correct Amount of Plays"

def convert_to_minute( length: int ) -> str:
    hours = str(length // 60)
    minutes = str(length % 60)
    if len(minutes) == 1:
        minutes = "0" + hours
    return hours + ":" + minutes

def comapre_years( user_song: Song) -> str:
    if user_song.year > correct_song.year:
        return "Older Song"
    elif user_song.year < correct_song.year:
        return "Newer Song"
    else:
        return "Correct Year"

while correct_song.title != user_guess.title:

    print("_____________________________________________________________")
    print("")

    user_guess = kanye_list[206]

    song_title_guess = input("Enter the name of a Kanye West song as your guess: ")

    for song in kanye_list:
        if song_title_guess == song.title:
            user_guess = song

    if user_guess.title == "":
        print("")
        print("Song name invalid please guess again")
        print("")
    else:
        print("")
        print("Your Guess: " + user_guess.title)
        print("")
        print("Your Guess Album: " + user_guess.album[2:] + "   ///////   " + compare_albums(user_guess))
        print("")
        print("Your Guess length " + convert_to_minute(user_guess.length) + "   ///////    "  + compare_lengths(user_guess))
        print("")
        print("Your Guess Plays: " + user_guess.plays + "    ///////     " + compare_plays(user_guess))
        print("")
        print("Your Guess Tracklist: " + str(user_guess.tracklist) + "    ///////     " + compare_tracklist(user_guess))
        print("")
        print("Your Guess Year: " + str(user_guess.year) + "      ///////       " + comapre_years(user_guess))
        print("")
        total_guesses = total_guesses + 1

print("_____________________________________________________________")
print("")
print("You Guessed the Correct Song of: " + correct_song.title)
print("")
print("You took " + str(total_guesses) + " total guesses")