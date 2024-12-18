from kanye_songs import kanye_list
import random
from dataclasses import dataclass

#Initialize Song dataclass
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

print("Welcome to the Kanye West Song Guessing Game")

#Initialze user_guess to Song with empty fields
user_guess = kanye_list[206]

#Initialize the total amount of guesses that it takes for a user to correctly guess the song
total_guesses = 0

#Compares the user's guess album to the correct album and returns the comparison
def compare_albums( user_song: Song ) -> str:
    if int(user_song.album[:2]) > int(correct_song.album[:2]):
        return "Older Album"
    elif int(user_song.album[:2]) < int(correct_song.album[:2]):
        return "Newer Album"
    else:
        return "Correct Album"

#Compares the user's guess track number to the correct track number and returns the comparison
def compare_tracklist( user_song: Song) -> str:
    if user_song.tracklist > correct_song.tracklist:
        return "Earlier in the Album"
    if user_song.tracklist < correct_song.tracklist:
        return "Later in the Album"
    else:
        return "Correct Track Number"

#Consumes a string that contains commas and produces an integers of that string without the commas
def remove_commas ( plays: str) -> int:
    new_string = ""
    for character in plays:
        if "," not in character:
            new_string = new_string + character
    return int(new_string)
    
#Compares the user's guess length to the correct length and returns the comparison
def compare_lengths( user_song: Song) -> str:
    if user_song.length > correct_song.length:
        return "Shorter Song"
    elif user_song.length < correct_song.length:
        return "Longer Song"
    else:
        return "Correct Song Length"

#Compares the user's guess plays to the correct plays and returns the comparison
def compare_plays ( user_song: Song) -> str:
    if remove_commas(user_song.plays) > remove_commas(correct_song.plays):
        return "Less Popular Song"
    elif remove_commas(user_song.plays) < remove_commas(correct_song.plays):
        return "More Popular Song"
    else:
        return "Correct Amount of Plays"

#Consumes an integer representing an amount of time and returns that time as a string expresses as analog time
def convert_to_minute( length: int ) -> str:
    hours = str(length // 60)
    minutes = str(length % 60)
    if len(minutes) == 1:
        minutes = "0" + hours
    return hours + ":" + minutes

#Compares the user's guess year to the correct year and returns the comparison
def comapre_years( user_song: Song) -> str:
    if user_song.year > correct_song.year:
        return "Older Song"
    elif user_song.year < correct_song.year:
        return "Newer Song"
    else:
        return "Correct Year"

#Main
while correct_song.title != user_guess.title:

    print("_____________________________________________________________")
    print("")

    #Returns the player's guess back to the empty state after they have guesses incorrectly
    user_guess = kanye_list[206]

    #Takes user input on what song they want to guess
    song_title_guess = input("Enter the name of a Kanye West song as your guess: ")

    # Takes the user;s song guess and turns it into the correct instance of the dataclass based on the kanye_songs list
    for song in kanye_list:
        if song_title_guess == song.title:
            user_guess = song

    #Checks to make sure user's guess is a valid song by checking to see if the song is still the empty instance
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

        #Add to the total guess count if song is valid
        total_guesses = total_guesses + 1

#End win text
print("_____________________________________________________________")
print("")
print("You Guessed the Correct Song of: " + correct_song.title)
print("")
print("You took " + str(total_guesses) + " total guesses")