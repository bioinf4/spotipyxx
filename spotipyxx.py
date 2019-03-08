import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get username from the terminal
username = "227qkpgpadng3pu55qxnt7yoa?si=4hgx6DtSTICVgE8jBhYTjA"
try: 
    token = util.prompt_for_user_token(username)
    
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our SpotifyObject
spotifyObject = spotipy.Spotify(auth=token)


user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']

print()
print(">>> Welcome " + displayName + "!")
print(">>> You have " + str(followers) + " followers!")
print()
print("0 - Search for cue points")
print("1 - exit")
print()
choice = input("Enter your choice to continue: ")

while choice != "1":
    #Search for artist
    if choice == "0":
            searchQuery = input("Enter the name of the song: ")
            artist_name = input("Enter the artist name: ")
            print()
            
            #Get search results   
            trackResults = spotifyObject.search(searchQuery,10,0,"track","US")
            tracks = trackResults["tracks"]["items"]
            id = (tracks[0]['id'])
            aa = spotifyObject.audio_analysis(id)
            sbars_in = aa["bars"][8]
            ebars_in = aa["bars"][16]
            ebars_out = aa["bars"][40]
            sbars_out = aa["bars"][32]
            print()
            print("For 16 Bars Before First Drop, Set a cue point at: ")
            print(sbars_in)
            print()
            print("For 8 Bars Before First Drop, Set a cue point at: ")
            print(ebars_in)
            print()
            print("For 16 Bars After First Drop, Set a cue point at: ")
            print(sbars_out)
            print()
            print("For 8 Bars After First Drop, Set a cue point at: ")
            print(ebars_out)
            print()
            print()
            print("0 - Search for cue points")
            print("1 - exit")
            print()
            choice = input("Enter your choice to continue: ")
            #Each track is a 2 element dictionary with 'album'
            #track_ids = []
            #for track in trackResults:
                
            #print(json.dumps(searchResults, sort_keys=True, indent=4))
     
#End the program
print("Program Terminated")